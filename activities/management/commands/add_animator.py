import urllib2
import unicodecsv as csv
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from people.models import *
from geographies.models import *

class Command(BaseCommand):
	def handle(self, *args, **options):
		dg_animator_obj = Animator.objects.using('digitalgreen').filter(partner_id=35).values('id','name','gender','phone_no','district_id','total_adoptions')
		for animator in dg_animator_obj:
			print animator['id']
			hn_district_obj = District.objects.filter(original_coco_id=animator['district_id'])
			hn_animator_obj = Animator(partner_id=1,original_coco_id=animator['id'],name=animator['name'],gender=animator['gender'],phone_no=animator['phone_no'],district=hn_district_obj[0],total_adoptions=animator['total_adoptions'])
			try:
				hn_animator_obj.save()
			except Exception as e:
				continue
			dg_assigned_obj = AnimatorAssignedVillage.objects.using('digitalgreen').filter(animator_id=animator['id'])
			for village in dg_assigned_obj:
				hn_village_obj = Village.objects.filter(original_coco_id=village.village_id)
				hn_assigned_obj = AnimatorAssignedVillage(village=hn_village_obj[0],animator=hn_animator_obj)
				hn_assigned_obj.save()

		'''
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


