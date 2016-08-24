import urllib2
import unicodecsv as csv
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from videos.models import *

class Command(BaseCommand):
	def handle(self, *args, **options):

		print "sector"
		dg_sector_obj = PracticeSector.objects.using('digitalgreen').values('id','name')
		for sector in dg_sector_obj:
			hn_sector_obj = PracticeSector(name=sector['name'],original_coco_id=sector['id'])
			hn_sector_obj.save()

		print "subsector"
		dg_subsector_obj = PracticeSubSector.objects.using('digitalgreen').values('id','name')
		for subsector in dg_subsector_obj:
			hn_subsector_obj = PracticeSubSector(name=subsector['name'],original_coco_id=subsector['id'])
			hn_subsector_obj.save()

		print "topic"
		dg_topic_obj = PracticeTopic.objects.using('digitalgreen').values('id','name')
		for topic in dg_topic_obj:
			hn_topic_obj = PracticeTopic(name=topic['name'],original_coco_id=topic['id'])
			hn_topic_obj.save()

		print "subtopic"
		dg_subtopic_obj = PracticeSubtopic.objects.using('digitalgreen').values('id','name')
		for subtopic in dg_subtopic_obj:
			hn_subtopic_obj = PracticeSubtopic(name=subtopic['name'],original_coco_id=subtopic['id'])
			hn_subtopic_obj.save()

		print "subject"
		dg_subject_obj = PracticeSubject.objects.using('digitalgreen').values('id','name')
		for subject in dg_subject_obj:
			hn_subject_obj = PracticeSubject(name=subject['name'],original_coco_id=subject['id'])
			hn_subject_obj.save()

		print "practice"
		dg_practice_obj = Practice.objects.using('digitalgreen').values('id','practice_name','practice_sector_id','practice_subsector_id','practice_topic_id','practice_subtopic_id','practice_subject_id')
		for practice in dg_practice_obj:
			hn_sector_obj = PracticeSector.objects.filter(original_coco_id=practice['practice_sector_id'])
			hn_sector_obj = hn_sector_obj[0] if len(hn_sector_obj) > 0 else None
			hn_subsector_obj = PracticeSubSector.objects.filter(original_coco_id=practice['practice_subsector_id'])
			hn_subsector_obj = hn_subsector_obj[0] if len(hn_subsector_obj) > 0 else None
			hn_topic_obj = PracticeTopic.objects.filter(original_coco_id=practice['practice_topic_id'])
			hn_topic_obj = hn_topic_obj[0] if len(hn_topic_obj) > 0 else None
			hn_subtopic_obj = PracticeSubtopic.objects.filter(original_coco_id=practice['practice_subtopic_id'])
			hn_subtopic_obj = hn_subtopic_obj[0] if len(hn_subtopic_obj) > 0 else None
			hn_subject_obj = PracticeSubject.objects.filter(original_coco_id=practice['practice_subject_id'])
			hn_subject_obj = hn_subject_obj[0] if len(hn_subject_obj) > 0 else None
			hn_practice_obj = Practice(original_coco_id=practice['id'],practice_name=practice['practice_name'],practice_sector=hn_sector_obj,practice_subsector=hn_subsector_obj,practice_topic=hn_topic_obj,practice_subtopic=hn_subtopic_obj,practice_subject=hn_subject_obj)
			hn_practice_obj.save()

		print "category"
		dg_category_obj = Category.objects.using('digitalgreen').values('id','category_name')
		for category in dg_category_obj:
			hn_category_obj = Category(category_name=category['category_name'],original_coco_id=category['id'])
			hn_category_obj.save()

		print "subcategory"
		dg_subcategory_obj = SubCategory.objects.using('digitalgreen').values('id','category_id','subcategory_name')
		for subcategory in dg_subcategory_obj:
			hn_category_obj = Category.objects.filter(original_coco_id=subcategory['category_id'])
			hn_category_obj = hn_category_obj[0] if len(hn_category_obj) > 0 else None
			hn_subcategory_obj = SubCategory(category=hn_category_obj,subcategory_name=subcategory['subcategory_name'],original_coco_id=subcategory['id'])
			hn_subcategory_obj.save()


		print "videopractice"
		dg_practice_obj = VideoPractice.objects.using('digitalgreen').values('id','subcategory_id','videopractice_name')
		for practice in dg_practice_obj:
			hn_subcategory_obj = SubCategory.objects.filter(original_coco_id=practice['subcategory_id'])
			hn_subcategory_obj = hn_subcategory_obj[0] if len(hn_subcategory_obj) > 0 else None
			hn_practice_obj = VideoPractice(subcategory=hn_subcategory_obj,videopractice_name=practice['videopractice_name'],original_coco_id=practice['id'])
			hn_practice_obj.save()

