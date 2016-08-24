import urllib2
import unicodecsv as csv
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from people.models import *
from geographies.models import *

class Command(BaseCommand):
	def handle(self, *args, **options):
		group_error = ""
		dg_group_obj = PersonGroup.objects.using('digitalgreen').filter(partner_id='35').values('id','village_id','group_name')
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

		#with open('dup_group','w') as g_file:
		#	g_file.write(group_error.encode('utf8'))
		

