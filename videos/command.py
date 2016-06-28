import xlrd
import urllib2
from datetime import datetime 
from django.core.management.base import BaseCommand
from people.models import *
from programs.models import *
from videos.models import *
from activities.models import *


class Command(BaseCommand):

def read_data(path):
    sheet_index = 5
    starting_row = 2
    data = {}
    open_file = xlrd.open_workbook(path)
    sheet = open_file.sheet_by_index(sheet_index)
    total_rows = sheet.nrows
    row = starting_row
    while row<total_rows:
        column = 0
        if sheet.cell(row,column).value != '':
            category = sheet.cell(row,column).value
            if category not in data:
                data[category] = {}
            column = column + 1
            while row<total_rows and ((sheet.cell(row,column-1).value==category) or  (sheet.cell(row,column-1).value == '')):
                sub_column = column
                if sheet.cell(row,sub_column).value != '':
                    sub_category = sheet.cell(row,sub_column).value
                else:
                    row += 1
                    continue
                if sub_category not in data[category]:
                    data[category][sub_category] = []
                sub_column += 1
                while row<total_rows and (sheet.cell(row,sub_column-1).value==sub_category or  sheet.cell(row,sub_column-1).value == ''):
                    practice_column = sub_column
                    if sheet.cell(row,practice_column).value != '':
                        practice = sheet.cell(row,practice_column).value
                        data[category][sub_category].append(practice)
                    row += 1
        else:
            row += 1
    return data
 

	def handle(self, *args, **options):

		file_path = "test.xlsx"
		data = read_data(file_path)
		for category in data:
			try:
				cat_obj =	Category.objects.get(name = category)
			except Category.DoesNotExist as e:
				cat_obj = Category(name = category)
				cat_obj.save()
			for sub_category in data[Category]:
				try:
					sub_cat_obj = SubCategory.objects.get(name=sub_category,category__name=Category)
				except SubCategory.DoesNotExist as e:
						sub_cat_obj = SubCategory(name=sub_category,category__name=Category)
						sub_cat_obj.save()
				for practice in data[category][sub_category]:
					try:
						practice_obj = VideoPractice.objects.get(name=practice,sub_category__name=sub_category)
					except VideoPractice.DoesNotExist as e:
							practice_obj = VideoPractice(name=practice,sub_category__name=sub_category)
							practice_obj.save()