import urllib2
import unicodecsv as csv
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from geographies.models import *
from activities.models import *

class Command(BaseCommand):
	def handle(self, *args, **options):
		country_obj = Country.objects.all()
		#print country_obj
		#import pdb;pdb.set_trace()
		#dg_country_obj = Country.objects.using('digitalgreen').all()
		#scra = PersonAdoptPractice.objects.using('digitalgreen').values('video','partner')
		#print scra[0]
		#for item in scra:
		#	ff = PersonAdoptPractice(video_id=item.video.id,partner_id=item.partner.id)
		#	print "demo:    ". ff
		#print scra[0].values()
		dg_country_obj = Country.objects.using('digitalgreen').filter(country_name__in=['Niger','Burkina Faso','Senegal']).values('id','country_name','start_date')
		for country in dg_country_obj:
			hn_country_obj = Country(country_name=country['country_name'],start_date=country['start_date'],original_coco_id=country['id'])
			hn_country_obj.save()
			dg_state_obj = State.objects.using('digitalgreen').filter(country_id=country['id']).values('id','state_name','start_date')
			for state in dg_state_obj:
				hn_state_obj = State(state_name=state['state_name'],start_date=state['start_date'],country=hn_country_obj,original_coco_id=state['id'])
				hn_state_obj.save()
				dg_district_obj = District.objects.using('digitalgreen').filter(state_id=state['id']).values('id','district_name','start_date')
				for district in dg_district_obj:
					hn_district_obj = District(district_name=district['district_name'],start_date=district['start_date'],state=hn_state_obj,original_coco_id=district['id'])
					hn_district_obj.save()
					dg_block_obj = Block.objects.using('digitalgreen').filter(district_id=district['id']).values('id','block_name','start_date')
					for block in dg_block_obj:
						hn_block_obj = Block(block_name=block['block_name'],start_date=block['start_date'],district=hn_district_obj,original_coco_id=block['id'])
						hn_block_obj.save()
						dg_village_obj = Village.objects.using('digitalgreen').filter(block_id=block['id']).values('id','village_name','start_date')
						for village in dg_village_obj:
							hn_village_obj = Village(village_name=village['village_name'],start_date=village['start_date'],block=hn_block_obj,original_coco_id=village['id'])
							hn_village_obj.save()

