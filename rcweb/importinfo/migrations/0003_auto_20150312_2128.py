# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('importinfo', '0002_auto_20150312_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseinfo',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 12, 13, 28, 18, 375172, tzinfo=utc), verbose_name='\u5bfc\u5165\u65e5\u671f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
