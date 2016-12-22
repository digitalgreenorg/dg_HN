from django.core.management.base import BaseCommand
from django.core.mail import EmailMultiAlternatives
from activities.models import Screening, PersonAdoptPractice, PersonMeetingAttendance

import csv
import datetime
import dg.settings

class Command(BaseCommand):

    def send_mail(self,reporting_file_path):
        today_date = datetime.datetime.now().strftime("%Y-%m-%d")
        subject = "Health & Nutrition (West Africa): Data received till %s"%(today_date)
        from_email = dg.settings.EMAIL_HOST_USER
        to_email = ['system@digitalgreen.org', 'avinash@digitalgreen.org', 'vikas@digitalgreen.org', 'vivek@digitalgreen.org', 'abhishekchandran@digitalgreen.org']
        body = "Dear Team,\n\nPlease find the attached Health & Nutrition (West Africa) data entered till %s.\nPlease contact system@digitalgreen.org for any question or clarification.\n\nThank you."%(today_date)
        msg = EmailMultiAlternatives(subject, body, from_email, to_email)
        msg.attach_file(reporting_file_path, 'text/csv' )
        msg.send()

    def check_dict(self,data,year,month,country,state,district,block,village,video):
        if year not in data:
            data[year] = dict()
        if month not in data[year]:
            data[year][month] = dict()
        if country not in data[year][month]:
            data[year][month][country] = dict()
        if state not in data[year][month][country]:
            data[year][month][country][state] = dict()
        if district not in data[year][month][country][state]:
            data[year][month][country][state][district] = dict()
        if block not in data[year][month][country][state][district]:
            data[year][month][country][state][district][block] = dict()
        if village not in data[year][month][country][state][district][block]:
            data[year][month][country][state][district][block][village] = dict()
        if video not in data[year][month][country][state][district][block][village]:
            data[year][month][country][state][district][block][village][video] = dict()

    def handle(self, *args, **options):
        data = dict()
        data_list = []
        reporting_file_path = 'files/health_data.csv'
        months_dic = dict(January=1, February=2, March=3, April=4, May=5, June=6, July=7,
              August=8, September=9, October=10, November=11, December=12)

        all_screening = Screening.objects.filter(date__isnull=False)
        for screening in all_screening:
            year = str(screening.date.strftime('%Y'))
            month = str(screening.date.strftime('%B'))
            country = str(screening.village.block.district.state.country.country_name.encode('utf-8'))
            state = str(screening.village.block.district.state.state_name.encode('utf-8'))
            district = str(screening.village.block.district.district_name.encode('utf-8'))
            block = str(screening.village.block.block_name.encode('utf-8'))
            village = str(screening.village.village_name.encode('utf-8'))
            videos = screening.videoes_screened.all()    
            for video in videos:
                self.check_dict(data,year,month,country,state,district,block,village,video)
                if 'TOTAL_SCREENING' not in data[year][month][country][state][district][block][village][video]:
                    data[year][month][country][state][district][block][village][video]['TOTAL_SCREENING'] = 0
                if 'UNIQUE_MEMBER' not in data[year][month][country][state][district][block][village][video]:
                    data[year][month][country][state][district][block][village][video]['UNIQUE_MEMBER'] = set()
                if 'UNIQUE_GROUP' not in data[year][month][country][state][district][block][village][video]:
                    data[year][month][country][state][district][block][village][video]['UNIQUE_GROUP'] = set()
                if 'PREG_WOMEN' not in data[year][month][country][state][district][block][village][video]:
                    data[year][month][country][state][district][block][village][video]['PREG_WOMEN'] = set()
                if 'MOTHER_CHILD' not in data[year][month][country][state][district][block][village][video]:
                    data[year][month][country][state][district][block][village][video]['MOTHER_CHILD'] = set()
                if 'ADOLE_GIRL' not in data[year][month][country][state][district][block][village][video]:
                    data[year][month][country][state][district][block][village][video]['ADOLE_GIRL'] = set()
                if 'OTHER_FEMALE' not in data[year][month][country][state][district][block][village][video]:
                    data[year][month][country][state][district][block][village][video]['OTHER_FEMALE'] = set()
                if 'MALE' not in data[year][month][country][state][district][block][village][video]:
                    data[year][month][country][state][district][block][village][video]['MALE'] = set()
                data[year][month][country][state][district][block][village][video]['TOTAL_SCREENING'] += 1
                for farmer in screening.farmers_attendance.all():
                    data[year][month][country][state][district][block][village][video]['UNIQUE_MEMBER'].add(farmer.id)
                for group in screening.farmer_groups_targeted.all():
                    data[year][month][country][state][district][block][village][video]['UNIQUE_GROUP'].add(group.id)
                person_category = PersonMeetingAttendance.objects.filter(screening=screening)
                preg_women = person_category.filter(category='0').values_list('person_id',flat=True)
                mother_child = person_category.filter(category='1').values_list('person_id',flat=True)
                adole_girl = person_category.filter(category='2').values_list('person_id',flat=True)
                other_female = person_category.filter(category='3').values_list('person_id',flat=True)
                male = person_category.filter(category='4').values_list('person_id',flat=True)
                for women in preg_women:
                    data[year][month][country][state][district][block][village][video]['PREG_WOMEN'].add(women)
                for mother in mother_child:
                    data[year][month][country][state][district][block][village][video]['MOTHER_CHILD'].add(mother)
                for girl in adole_girl:
                    data[year][month][country][state][district][block][village][video]['ADOLE_GIRL'].add(mother)
                for female in other_female:
                    data[year][month][country][state][district][block][village][video]['OTHER_FEMALE'].add(mother)
                for m in male:
                    data[year][month][country][state][district][block][village][video]['MALE'].add(m)
        del all_screening

        all_adoption = PersonAdoptPractice.objects.filter(date_of_verification__isnull=False)
        for adoption in all_adoption:
            year = str(adoption.date_of_verification.strftime('%Y'))
            month = str(adoption.date_of_verification.strftime('%B'))
            country = str(adoption.person.village.block.district.state.country.country_name.encode('utf-8'))
            state = str(adoption.person.village.block.district.state.state_name.encode('utf-8'))
            district = str(adoption.person.village.block.district.district_name.encode('utf-8'))
            block = str(adoption.person.village.block.block_name.encode('utf-8'))
            village = str(adoption.person.village.village_name.encode('utf-8'))
            video = adoption.video
            self.check_dict(data,year,month,country,state,district,block,village,video)
            if 'UNIQUE_ADOPTION' not in data[year][month][country][state][district][block][village][video]:
                data[year][month][country][state][district][block][village][video]['UNIQUE_ADOPTION'] = set()
            if 'UNIQUE_PROMOT' not in data[year][month][country][state][district][block][village][video]:
                data[year][month][country][state][district][block][village][video]['UNIQUE_PROMOT'] = set()
            if 'RECALL_ALL_NEGO' not in data[year][month][country][state][district][block][village][video]:
                data[year][month][country][state][district][block][village][video]['RECALL_ALL_NEGO'] = set()
            if adoption.adopt_practice == 1:
                data[year][month][country][state][district][block][village][video]['UNIQUE_ADOPTION'].add(adoption.person_id)
            if adoption.promote_practice == 1:
                data[year][month][country][state][district][block][village][video]['UNIQUE_PROMOT'].add(adoption.person_id)
            if adoption.n_one == 1 and adoption.n_two == 1 and adoption.n_three == 1 and adoption.n_four == 1 and adoption.n_five == 1:
                data[year][month][country][state][district][block][village][video]['RECALL_ALL_NEGO'].add(adoption.person_id)
        del all_adoption

        for year in data:
            for month in data[year]:
                for country in data[year][month]:
                    for state in data[year][month][country]:
                        for district in data[year][month][country][state]:
                            for block in data[year][month][country][state][district]:
                                for village in data[year][month][country][state][district][block]:
                                    for video in data[year][month][country][state][district][block][village]:
                                        if 'TOTAL_SCREENING' not in data[year][month][country][state][district][block][village][video]:
                                            data[year][month][country][state][district][block][village][video]['TOTAL_SCREENING'] = 0
                                        else:
                                            pass
                                        if 'UNIQUE_MEMBER' not in data[year][month][country][state][district][block][village][video]:
                                            data[year][month][country][state][district][block][village][video]['UNIQUE_MEMBER'] = 0
                                        else:
                                            data[year][month][country][state][district][block][village][video]['UNIQUE_MEMBER'] = len(data[year][month][country][state][district][block][village][video]['UNIQUE_MEMBER'])
                                        if 'UNIQUE_GROUP' not in data[year][month][country][state][district][block][village][video]:
                                            data[year][month][country][state][district][block][village][video]['UNIQUE_GROUP'] = 0
                                        else:
                                            data[year][month][country][state][district][block][village][video]['UNIQUE_GROUP'] = len(data[year][month][country][state][district][block][village][video]['UNIQUE_GROUP'])
                                        if 'PREG_WOMEN' not in data[year][month][country][state][district][block][village][video]:
                                            data[year][month][country][state][district][block][village][video]['PREG_WOMEN'] = 0
                                        else:
                                            data[year][month][country][state][district][block][village][video]['PREG_WOMEN'] = len(data[year][month][country][state][district][block][village][video]['PREG_WOMEN'])
                                        if 'MOTHER_CHILD' not in data[year][month][country][state][district][block][village][video]:
                                            data[year][month][country][state][district][block][village][video]['MOTHER_CHILD'] = 0
                                        else:
                                            data[year][month][country][state][district][block][village][video]['MOTHER_CHILD'] = len(data[year][month][country][state][district][block][village][video]['MOTHER_CHILD'])
                                        if 'ADOLE_GIRL' not in data[year][month][country][state][district][block][village][video]:
                                            data[year][month][country][state][district][block][village][video]['ADOLE_GIRL'] = 0
                                        else:
                                            data[year][month][country][state][district][block][village][video]['ADOLE_GIRL'] = len(data[year][month][country][state][district][block][village][video]['ADOLE_GIRL'])
                                        if 'OTHER_FEMALE' not in data[year][month][country][state][district][block][village][video]:
                                            data[year][month][country][state][district][block][village][video]['OTHER_FEMALE'] = 0
                                        else:
                                            data[year][month][country][state][district][block][village][video]['OTHER_FEMALE'] = len(data[year][month][country][state][district][block][village][video]['OTHER_FEMALE'])
                                        if 'MALE' not in data[year][month][country][state][district][block][village][video]:
                                            data[year][month][country][state][district][block][village][video]['MALE'] = 0
                                        else:
                                            data[year][month][country][state][district][block][village][video]['MALE'] = len(data[year][month][country][state][district][block][village][video]['MALE'])
                                        if 'UNIQUE_ADOPTION' not in data[year][month][country][state][district][block][village][video]:
                                            data[year][month][country][state][district][block][village][video]['UNIQUE_ADOPTION'] = 0
                                        else:
                                            data[year][month][country][state][district][block][village][video]['UNIQUE_ADOPTION'] = len(data[year][month][country][state][district][block][village][video]['UNIQUE_ADOPTION'])
                                        if 'UNIQUE_PROMOT' not in data[year][month][country][state][district][block][village][video]:
                                            data[year][month][country][state][district][block][village][video]['UNIQUE_PROMOT'] = 0
                                        else:
                                            data[year][month][country][state][district][block][village][video]['UNIQUE_PROMOT'] = len(data[year][month][country][state][district][block][village][video]['UNIQUE_PROMOT'])
                                        if 'RECALL_ALL_NEGO' not in data[year][month][country][state][district][block][village][video]:
                                            data[year][month][country][state][district][block][village][video]['RECALL_ALL_NEGO'] = 0
                                        else:
                                            data[year][month][country][state][district][block][village][video]['RECALL_ALL_NEGO'] = len(data[year][month][country][state][district][block][village][video]['RECALL_ALL_NEGO'])    
                                        video_title = str(video.title.encode('utf-8'))
                                        total_screening = data[year][month][country][state][district][block][village][video]['TOTAL_SCREENING']
                                        unique_member= data[year][month][country][state][district][block][village][video]['UNIQUE_MEMBER'] 
                                        unique_group = data[year][month][country][state][district][block][village][video]['UNIQUE_GROUP']
                                        preg_women =  data[year][month][country][state][district][block][village][video]['PREG_WOMEN']
                                        mother_child = data[year][month][country][state][district][block][village][video]['MOTHER_CHILD']
                                        adole_girl = data[year][month][country][state][district][block][village][video]['ADOLE_GIRL']
                                        other_female = data[year][month][country][state][district][block][village][video]['OTHER_FEMALE']
                                        male = data[year][month][country][state][district][block][village][video]['MALE']
                                        unique_adoption = data[year][month][country][state][district][block][village][video]['UNIQUE_ADOPTION']
                                        unique_promt = data[year][month][country][state][district][block][village][video]['UNIQUE_PROMOT']
                                        recall_all_nego = data[year][month][country][state][district][block][village][video]['RECALL_ALL_NEGO']
                                        data_list.append({'YEAR':year,'MONTH':month,'COUNTRY':country,'REGION':state,'DEPARTMENT':district,'COMMUNE':block,'VILLAGE':village,'VIDEO':video_title,'TOTAL SCREENING':total_screening,'UNIQUE_GROUP':unique_group,'UNIQUE_MEMBER':unique_member,'Pregnant Woman':preg_women,'Mother of child < 5 years old':mother_child,'Adolescent girls (10-19 years old)':adole_girl,'Other females':other_female,'Males':male,'UNIQUE MEMBER REPORT ADOPT PRACTICE':unique_adoption,'UNIQUE MEMBER REPORT PROMOT PRACTICE':unique_promt,'UNIQUE MEMBER REPORT RECALL ALL NON-NEGOTIABLES':recall_all_nego})
        del data
        data_list = sorted(data_list,key=lambda ele: (ele['YEAR'],months_dic[ele['MONTH']]),reverse=True)
        headers = ['YEAR','MONTH', 'COUNTRY', 'REGION', 'DEPARTMENT', 'COMMUNE', 'VILLAGE', 'VIDEO', 'TOTAL SCREENING', 'UNIQUE_GROUP', 'UNIQUE_MEMBER', 'Pregnant Woman', 'Mother of child < 5 years old', 'Adolescent girls (10-19 years old)', 'Other females', 'Males', 'UNIQUE MEMBER REPORT ADOPT PRACTICE', 'UNIQUE MEMBER REPORT PROMOT PRACTICE', 'UNIQUE MEMBER REPORT RECALL ALL NON-NEGOTIABLES']
        with open(reporting_file_path,'wb') as final_output:
            dict_writer = csv.DictWriter(final_output,headers)
            dict_writer.writeheader()
            dict_writer.writerows(data_list)
        self.send_mail(reporting_file_path)
