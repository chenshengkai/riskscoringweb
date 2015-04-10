# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('importinfo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseinfo',
            name='user',
        ),
        migrations.AddField(
            model_name='baseinfo',
            name='user_id',
            field=models.CharField(max_length=20, null=True, verbose_name='\u7528\u6237', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 12, 12, 53, 40, 102413, tzinfo=utc), verbose_name='\u5bfc\u5165\u65e5\u671f'),
            preserve_default=True,
        ),
    ]
