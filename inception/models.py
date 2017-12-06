# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class InceptionBackupInformation(models.Model):
    opid_time = models.CharField(primary_key=True, max_length=50)
    start_binlog_file = models.CharField(max_length=512, blank=True, null=True)
    start_binlog_pos = models.IntegerField(blank=True, null=True)
    end_binlog_file = models.CharField(max_length=512, blank=True, null=True)
    end_binlog_pos = models.IntegerField(blank=True, null=True)
    sql_statement = models.TextField(blank=True, null=True)
    host = models.CharField(max_length=64, blank=True, null=True)
    dbname = models.CharField(max_length=64, blank=True, null=True)
    tablename = models.CharField(max_length=64, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField()
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '$_$Inception_backup_information$_$'


class inc_test(models.Model):
    id = models.BigIntegerField(primary_key=True)
    rollback_statement = models.TextField(blank=True, null=True)
    opid_time = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inc_test'
##[jetbrains/Users/zhanghui/PycharmProjects/inception_web/inception/models.py

class inc_test2(models.Model):
    id = models.BigIntegerField(primary_key=True)
    rollback_statement = models.TextField(blank=True, null=True)
    opid_time = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inc_test2'