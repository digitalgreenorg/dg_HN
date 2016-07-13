import json, datetime
import calendar
from django.db import models
from django.db.models.signals import pre_delete, post_save

from coco.data_log import delete_log, save_log
from coco.base_models import CocoModel
from geographies.models import Village
from programs.models import Partner
from people.models import Animator, Person, PersonGroup
from videos.models import Video
from coco.base_models import ADOPTION_VERIFICATION, SCREENING_OBSERVATION, SCREENING_GRADE, VERIFIED_BY, ATTENDED_PERSON_CATEGORY



class Screening(CocoModel):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    village = models.ForeignKey(Village)
    animator = models.ForeignKey(Animator)
    farmer_groups_targeted = models.ManyToManyField(PersonGroup)
    videoes_screened = models.ManyToManyField(Video)
    farmers_attendance = models.ManyToManyField(Person, through='PersonMeetingAttendance', blank='False', null='False')
    partner = models.ForeignKey(Partner)
    observation_status = models.IntegerField(max_length=1, choices=SCREENING_OBSERVATION, default=0)
    screening_grade = models.CharField(max_length=1,choices=SCREENING_GRADE,null=True,blank=True)
    observer = models.IntegerField(max_length=1, choices=VERIFIED_BY, null=True, blank=True)
    problem_faced = models.TextField(blank=True)

    class Meta:
        unique_together = ("date", "animator", "village")

    def __unicode__(self):
        return u'%s' % (self.village.village_name)

    def screening_location(self):
        return u'%s (%s) (%s) (%s)' % (self.village.village_name, self.village.block.block_name, self.village.block.district.district_name, self.village.block.district.state.state_name)

post_save.connect(save_log, sender=Screening)
pre_delete.connect(delete_log, sender=Screening)


class PersonMeetingAttendance(CocoModel):
    id = models.AutoField(primary_key=True)
    screening = models.ForeignKey(Screening)
    person = models.ForeignKey(Person)
    category = models.CharField(max_length=1, choices=ATTENDED_PERSON_CATEGORY)

    def __unicode__(self):
        return  u'%s' % (self.id)

class PersonAdoptPractice(CocoModel):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person)
    video = models.ForeignKey(Video)
    partner = models.ForeignKey(Partner)
    verification_status = models.IntegerField(max_length=1, choices=ADOPTION_VERIFICATION, default=0)
    non_negotiable_check = models.CharField(max_length=256, blank=True, null=True)
    verified_by = models.IntegerField(max_length=1, choices=VERIFIED_BY, null=True, blank=True)
    date_of_verification = models.DateField(null=True,blank=True)
    promote_practice = models.BooleanField(default=False)
    n_one = models.BooleanField(db_index=True,default=False)
    n_two = models.BooleanField(db_index=True,default=False)
    n_three = models.BooleanField(db_index=True,default=False)
    n_four = models.BooleanField(db_index=True,default=False)
    n_five = models.BooleanField(db_index=True,default=False)

    def __unicode__(self):
        return "%s (%s) (%s) (%s) (%s)" % (self.person.person_name, self.person.father_name, self.person.group.group_name if self.person.group else '', self.person.village.village_name, self.video.title)

    class Meta:
        unique_together = ("person", "video", "date_of_verification")
post_save.connect(save_log, sender=PersonAdoptPractice)
pre_delete.connect(delete_log, sender=PersonAdoptPractice)


class Influencers(CocoModel):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    village = models.ForeignKey(Village)
    mediator = models.ForeignKey(Animator)
    partner = models.ForeignKey(Partner)
    video = models.ManyToManyField(Video)
    group = models.ManyToManyField(PersonGroup)
    number_of_male = models.IntegerField(null=True, blank=True)
    number_of_female = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return  u'%s' % (self.id)
post_save.connect(save_log, sender=Influencers)
pre_delete.connect(delete_log, sender=Influencers)

