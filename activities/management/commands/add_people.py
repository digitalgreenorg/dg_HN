import urllib2
import unicodecsv as csv
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from people.models import *
from geographies.models import *

class Command(BaseCommand):
	def handle(self, *args, **options):
		dg_person_obj = Person.objects.using('digitalgreen').filter(partner_id='35').values('id','person_name','father_name','age','gender','phone_no','village_id','group_id','image_exists','date_of_joining','partner_id')
		for person in dg_person_obj:
			print person['id']
			hn_village_obj = Village.objects.filter(original_coco_id=person['village_id'])
			hn_group_obj = PersonGroup.objects.filter(original_coco_id=person['group_id'])
			if len(hn_village_obj) > 0:
				hn_village_obj = hn_village_obj[0]
			else:
				hn_village_obj = None
			if len(hn_group_obj) > 0:
				hn_group_obj = hn_group_obj[0]
			else:
				hn_group_obj = None
			hn_person_obj = Person(village=hn_village_obj,group=hn_group_obj,partner_id=1,original_coco_id=person['id'],person_name=person['person_name'],father_name=person['father_name'],age=person['age'],gender=person['gender'],phone_no=person['phone_no'],image_exists=person['image_exists'],date_of_joining=person['date_of_joining'])
			hn_person_obj.save()


		'''
		for group in dg_group_obj:
			#dg_village_obj = Village.objects.using('digitalgreen').filter(id=group['village_id']).values('village_name','block_id')
			#dg_block_obj = Block.objects.using('digitalgreen').filter(id=dg_village_obj[0]['block_id']).values('block_name')
			#hn_block_obj = Block.objects.filter(block_name=dg_block_obj[0]['block_name']).values('id')
			#hn_village_obj = Village.objects.filter(village_name=dg_village_obj[0]['village_name'],block_id=hn_block_obj[0]['id'])
			hn_village_obj = Village.objects.filter(original_coco_id=group['village_id'])
			# duplicate log
			#group_error += dg_village_obj[0]['village_name'] + '   ' + str(hn_village_obj.count()) + '\n'
			hn_group_obj = PersonGroup(group_name=group['group_name'],village=hn_village_obj[0],partner_id=1,original_coco_id=group['id'])
			hn_group_obj.save()
		'''
		

