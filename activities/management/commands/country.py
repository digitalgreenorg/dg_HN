import urllib2
import unicodecsv as csv
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from geographies.models import *

class Command(BaseCommand):
	def handle(self, *args, **options):
		file_path = "data/geographies.csv"
		csv_reader = ""
		logfile = "logs"
		logs = "\nName : Value : Exception"
		with open(file_path,'r') as csvfile:
			csv_reader = csv.DictReader(csvfile, delimiter = ',', quotechar = '|')	
			for row in csv_reader:
				row['country_name'] = row['country_name'].strip().strip('"')
				row['state_name'] = row['state_name'].strip().strip('"')
				row['district_name'] = row['district_name'].strip().strip('"')
				row['block_name'] = row['block_name'].strip().strip('"')
				row['village_name'] = row['village_name'].strip().strip('"')
				print row['country_name'],row['state_name'],row['district_name'],row['block_name'],row['village_name']
				try:
					coun_obj = Country.objects.get(country_name = row['country_name'])
				except Exception as e:
					logs += "Country: " + row['country_name'] + " : " + str(e) + "\n"
					coun_obj = Country(country_name = row['country_name'])
					coun_obj.save()

				try:
					state_obj = State.objects.get(state_name = row['state_name'],country__country_name=row['country_name'])
				except Exception as e:
					logs += "state: " + row['state_name'] + " : " + str(e) + "\n"
					state_obj = State(state_name = row['state_name'],country=coun_obj)
					state_obj.save()

				try:
					district_obj = District.objects.get(district_name = row['district_name'],state__state_name = row['state_name'])
				except Exception as e:
					logs += "District: " + row['district_name'] + " : " + str(e) + "\n"
					district_obj = District(district_name = row['district_name'],state=state_obj)
					district_obj.save()

				try:
					block_obj = Block.objects.get(block_name = row['block_name'], district__district_name = row['district_name'])
				except Exception as e:
					logs += "Block: " + row['block_name'] + " : " + str(e) + "\n"
					block_obj = Block(block_name = row['block_name'],district=district_obj)
					block_obj.save()
					
				try:
					village_obj = Village.objects.get(village_name = row['village_name'],block__block_name = row['block_name'])
				except Exception as e:
					logs += "Village: " + row['village_name'] + " : " + str(e) + "\n"
					village_obj = Village(village_name = row['village_name'],block=block_obj)
					village_obj.save()


