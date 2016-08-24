import urllib2
import unicodecsv as csv
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from people.models import *
from programs.models import *

class Command(BaseCommand):
	def handle(self, *args, **options):
		group_error = ""
		dg_partner_obj = Partner.objects.using('digitalgreen').filter(id='35').values('id','partner_name')
		for partner in dg_partner_obj:
			hn_partner_obj = Partner(partner_name=partner['partner_name'],original_coco_id=partner['id'])
			hn_partner_obj.save()


