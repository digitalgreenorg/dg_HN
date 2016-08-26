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
		
		dg_screening_obj = Screening.objects.using('digitalgreen').filter(partner_id=35).values('id','date','start_time','location','village_id','animator_id','observation_status','screening_grade','observer')
		for screening in dg_screening_obj:
			print screening['id']
			hn_village_obj = Village.objects.filter(original_coco_id=screening['village_id'])
			hn_village_obj = hn_village_obj[0] if len(hn_village_obj) > 0 else None
			if screening['animator_id'] == 16625:
				screening['animator_id'] = 19544
			hn_animator_obj = Animator.objects.filter(original_coco_id=screening['animator_id'])
			hn_animator_obj = hn_animator_obj[0] if len(hn_animator_obj) > 0 else None
			hn_screening_obj = Screening(original_coco_id=screening['id'],village=hn_village_obj,animator=hn_animator_obj,partner_id=1,date=screening['date'],start_time=screening['start_time'],location=screening['location'],observation_status=screening['observation_status'],screening_grade=screening['screening_grade'],observer=screening['observer'])
			try:
				hn_screening_obj.save()
			except Exception as e:
				continue

			dg_group_obj = Screening.objects.using('digitalgreen').filter(id=screening['id']).values('farmer_groups_targeted')
			for group in dg_group_obj:
				print "group ",group['farmer_groups_targeted']
				hn_group_obj = PersonGroup.objects.filter(original_coco_id=group['farmer_groups_targeted'])
				hn_screening_obj.farmer_groups_targeted.add(hn_group_obj[0])

			dg_video_obj = Screening.objects.using('digitalgreen').filter(id=screening['id']).values('videoes_screened')
			for video in dg_video_obj:
				print "video ",video['videoes_screened']
				hn_video_obj = Video.objects.filter(original_coco_id=video['videoes_screened'])
				hn_screening_obj.videoes_screened.add(hn_video_obj[0])

			dg_attend_obj = PersonMeetingAttendance.objects.using('digitalgreen').filter(screening_id=screening['id']).values('id','person_id')
			for attend in dg_attend_obj:
				print "attend ",attend['id']
				hn_person_obj = Person.objects.filter(original_coco_id=attend['person_id'])
				if len(hn_person_obj):
					hn_person_obj = hn_person_obj[0]
				else:
					continue
				hn_attend_obj = PersonMeetingAttendance(original_coco_id=attend['id'],screening=hn_screening_obj,person=hn_person_obj)
				hn_attend_obj.save()

