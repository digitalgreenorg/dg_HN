import urllib2
import unicodecsv as csv
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from videos.models import *
from geographies.models import *
from programs.models import *

class Command(BaseCommand):
	def handle(self, *args, **options):
		
		dg_video_obj = Video.objects.using('digitalgreen').filter(partner_id=35).values('id','title','video_type','duration','language_id','benefit','production_date','village_id','category_id','subcategory_id','videopractice_id','approval_date','related_practice_id','youtubeid','partner_id','review_status','video_grade','reviewer')
		for video in dg_video_obj:
			print video['id']
			hn_language_obj = Language.objects.filter(original_coco_id=video['language_id'])
			hn_language_obj = hn_language_obj[0] if len(hn_language_obj) > 0 else None
			hn_village_obj = Village.objects.filter(original_coco_id=video['village_id'])
			hn_village_obj = hn_village_obj[0] if len(hn_village_obj) > 0 else None
			hn_category_obj = Category.objects.filter(original_coco_id=video['category_id'])
			hn_category_obj = hn_category_obj[0] if len(hn_category_obj) > 0 else None
			hn_subcategory_obj = SubCategory.objects.filter(original_coco_id=video['subcategory_id'])
			hn_subcategory_obj = hn_subcategory_obj[0] if len(hn_subcategory_obj) > 0 else None
			hn_videopractice_obj = VideoPractice.objects.filter(original_coco_id=video['videopractice_id'])
			hn_videopractice_obj = hn_videopractice_obj[0] if len(hn_videopractice_obj) > 0 else None
			hn_practice_obj = Practice.objects.filter(original_coco_id=video['related_practice_id'])
			hn_practice_obj = hn_practice_obj[0] if len(hn_practice_obj) > 0 else None
			hn_video_obj = Video(original_coco_id=video['id'],title=video['title'],video_type=video['video_type'],duration=video['duration'],language=hn_language_obj,benefit=video['benefit'],production_date=video['production_date'],village=hn_village_obj,category=hn_category_obj,subcategory=hn_subcategory_obj,videopractice=hn_videopractice_obj,approval_date=video['approval_date'],related_practice_id=video['related_practice_id'],youtubeid=video['youtubeid'],partner_id=1,review_status=video['review_status'],video_grade=video['video_grade'],reviewer=video['reviewer'])
			hn_video_obj.save()

			dg_team_obj = Video.objects.using('digitalgreen').filter(id=video['id']).values('production_team')
			for team in dg_team_obj:
				hn_animator_obj = Animator.objects.filter(original_coco_id=team['production_team'])
				hn_video_obj.production_team.add(hn_animator_obj[0])


		print "nonnego"
		dg_nonnego_obj = NonNegotiable.objects.using('digitalgreen').filter(video__partner_id=35).values('id','video_id','non_negotiable','physically_verifiable')
		for nonnego in dg_nonnego_obj:
			hn_video_obj = Video.objects.filter(original_coco_id=nonnego['video_id'])
			hn_video_obj = hn_video_obj[0] if len(hn_video_obj) > 0 else None
			hn_nonnego_obj = NonNegotiable(video=hn_video_obj,non_negotiable=nonnego['non_negotiable'],physically_verifiable=nonnego['physically_verifiable'],original_coco_id=nonnego['id'])
			hn_nonnego_obj.save()
		
