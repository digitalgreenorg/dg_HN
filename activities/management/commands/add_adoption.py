import urllib2
import unicodecsv as csv
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from videos.models import *
from geographies.models import *
from programs.models import *
from activities.models import *
from people.models import *

class Command(BaseCommand):
	def handle(self, *args, **options):
		
		dg_adoption_obj = PersonAdoptPractice.objects.using('digitalgreen').filter(partner_id=35).values('id','person_id','video_id','verification_status','non_negotiable_check','verified_by','date_of_verification','date_of_adoption')
		for adoption in dg_adoption_obj:
			print adoption['id']
			hn_video_obj = Video.objects.filter(original_coco_id=adoption['video_id'])
			hn_video_obj = hn_video_obj[0] if len(hn_video_obj) > 0 else None
			hn_person_obj = Person.objects.filter(original_coco_id=adoption['person_id'])
			hn_person_obj = hn_person_obj[0] if len(hn_person_obj) > 0 else None
			adoption['date_of_verification'] = adoption['date_of_adoption'] if adoption['date_of_verification'] is None else adoption['date_of_verification']
			hn_adoption_obj = PersonAdoptPractice(original_coco_id=adoption['id'],person=hn_person_obj,video=hn_video_obj,partner_id=1,verification_status=adoption['verification_status'],non_negotiable_check=adoption['non_negotiable_check'],verified_by=adoption['verified_by'],adopt_practice=1,date_of_verification=adoption['date_of_verification'])
			try:
				hn_adoption_obj.save()
			except Exception as e:
				continue
			
