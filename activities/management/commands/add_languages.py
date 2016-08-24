import urllib2
import unicodecsv as csv
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from videos.models import *

class Command(BaseCommand):
	def handle(self, *args, **options):
		dg_language_obj = Language.objects.using('digitalgreen').values('id','language_name')
		for language in dg_language_obj:
			hn_language_obj = Language(language_name=language['language_name'],original_coco_id=language['id'])
			hn_language_obj.save()
