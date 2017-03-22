# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Activity(models.Model):

    class Meta:
        db_table = 'activity'


class ActivityField(models.Model):
    id_activity = models.ForeignKey(Activity, models.DO_NOTHING, db_column='id_activity', blank=True, null=True)
    id_field = models.ForeignKey('Field', models.DO_NOTHING, db_column='id_field', blank=True, null=True)

    class Meta:
        db_table = 'activity__field'


class Field(models.Model):
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'field'


class Media(models.Model):
    media_type = models.ForeignKey('MediaType', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'media'


class MediaType(models.Model):
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'media_type'


class Report(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, related_name='reports', blank=True, null=True)
    activity = models.ForeignKey(Activity, models.DO_NOTHING, blank=True, null=True)
    media = models.ForeignKey(Media, models.DO_NOTHING, blank=True, null=True)
    pos = models.PointField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'report'


class ReportActivityField(models.Model):
    id_report = models.IntegerField()
    id_activity_field = models.ForeignKey(ActivityField, models.DO_NOTHING, db_column='id_activity__field')  # Field renamed because it contained more than one '_' in a row.
    payload = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'report__activity__field'
        unique_together = (('id_report', 'id_activity_field'),)

