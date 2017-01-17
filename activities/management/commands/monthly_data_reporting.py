from django.core.management.base import BaseCommand
from django.core.mail import EmailMultiAlternatives

import pandas as pd
import pandas.io.sql as psql
import MySQLdb
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

    def run_query(self,query):
        mysql_cn = MySQLdb.connect(host='localhost', port=3306, 
            user=dg.settings.DATABASES['default']['USER'] ,
            passwd=dg.settings.DATABASES['default']['PASSWORD'],
            db=dg.settings.DATABASES['default']['NAME'],
            charset = 'utf8',
            use_unicode = True) 
        temp_df = psql.read_sql(query, con=mysql_cn)
        mysql_cn.close()
        return temp_df

    def handle(self, *args, **options):

        reporting_file_path = 'files/health_data.csv'
        screening_query = '''SELECT 
                YEAR(ascr.date) YEAR,
                MONTHNAME(ascr.date) MONTH,
                gc.country_name COUNTRY,
                gs.state_name REGION,
                gd.district_name DEPARTMENT,
                gb.block_name COMMUNE,
                gv.village_name VILLAGE,
                vv.title VIDEO,
                COUNT(DISTINCT ascr.id) 'TOTAL SCREENING',
                COUNT(DISTINCT fgt.persongroup_id) UNIQUE_GROUP,
                COUNT(DISTINCT pma.person_id) UNIQUE_MEMBER,
                COUNT(DISTINCT CASE pma.category
                        WHEN '0' THEN pma.person_id
                    END) 'Pregnant Woman',
                COUNT(DISTINCT CASE pma.category
                        WHEN '1' THEN pma.person_id
                    END) 'Mother of child < 5 years old',
                COUNT(DISTINCT CASE pma.category
                        WHEN '2' THEN pma.person_id
                    END) 'Adolescent girls (10-19 years old)',
                COUNT(DISTINCT CASE pma.category
                        WHEN '3' THEN pma.person_id
                    END) 'Other females',
                COUNT(DISTINCT CASE pma.category
                        WHEN '4' THEN pma.person_id
                    END) 'Males'
            FROM
                geographies_village gv
                    JOIN
                geographies_block gb ON gv.block_id = gb.id
                    JOIN
                geographies_district gd ON gd.id = gb.district_id
                    JOIN
                geographies_state gs ON gs.id = gd.state_id
                    JOIN
                geographies_country gc ON gc.id = gs.country_id
                    JOIN
                activities_screening ascr ON ascr.village_id = gv.id
                    JOIN
                activities_personmeetingattendance pma ON ascr.id = pma.screening_id
                    JOIN
                activities_screening_farmer_groups_targeted fgt ON ascr.id = fgt.screening_id
                    JOIN
                activities_screening_videoes_screened svs ON ascr.id = svs.screening_id
                    JOIN
                videos_video vv ON svs.video_id = vv.id
            GROUP BY YEAR(ascr.date) , MONTH(ascr.date) , gc.id , gs.id , gd.id , gb.id , gv.id , vv.title
            ORDER BY YEAR(ascr.date) DESC, MONTH(ascr.date) DESC '''

        adoption_query = '''SELECT 
                YEAR(pap.date_of_verification) YEAR,
                MONTHNAME(pap.date_of_verification) MONTH,
                gc.country_name COUNTRY,
                gs.state_name REGION,
                gd.district_name DEPARTMENT,
                gb.block_name COMMUNE,
                gv.village_name VILLAGE,
                vv.title VIDEO,
                COUNT(DISTINCT CASE pap.adopt_practice
                        WHEN '1' THEN pap.person_id
                    END) 'UNIQUE MEMBER REPORT ADOPT PRACTICE',
                COUNT(DISTINCT CASE pap.promote_practice
                        WHEN '1' THEN pap.person_id
                    END) 'UNIQUE MEMBER REPORT PROMOT PRACTICE',
                COUNT(DISTINCT CASE
                        WHEN
                            n_one = '1' AND n_two = '1'
                                AND n_three = '1'
                                AND n_four = '1'
                                AND n_five = '1'
                        THEN
                            pap.person_id
                    END) 'UNIQUE MEMBER REPORT RECALL ALL NON-NEGOTIABLES'
            FROM
                geographies_village gv
                    JOIN
                geographies_block gb ON gv.block_id = gb.id
                    JOIN
                geographies_district gd ON gd.id = gb.district_id
                    JOIN
                geographies_state gs ON gs.id = gd.state_id
                    JOIN
                geographies_country gc ON gc.id = gs.country_id
                    JOIN
                people_person pp ON pp.village_id = gv.id
                    JOIN
                activities_personadoptpractice pap ON pap.person_id = pp.id AND pap.video_id
                    JOIN
                videos_video vv ON pap.video_id = vv.id
            GROUP BY YEAR(pap.date_of_verification) , MONTH(pap.date_of_verification) , gc.id , gs.id , gd.id , gb.id , gv.id , vv.title
            ORDER BY YEAR(pap.date_of_verification) DESC, MONTH(pap.date_of_verification) DESC '''

        screening_df = self.run_query(screening_query)
        adoption_df = self.run_query(adoption_query)
        combine_df = pd.merge(screening_df, adoption_df, how='outer')
        combine_df.to_csv(reporting_file_path, sep=',', encoding='utf-8', index=False)
        self.send_mail(reporting_file_path)
