# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('importinfo', '0003_auto_20150312_2128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baseinfo',
            old_name='user_id',
            new_name='create_by',
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 12, 13, 30, 22, 958523, tzinfo=utc), verbose_name='\u5bfc\u5165\u65e5\u671f'),
            preserve_default=True,
        ),
    ]
