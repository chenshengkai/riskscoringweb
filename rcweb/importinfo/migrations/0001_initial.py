# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseInfo',
            fields=[
                ('customer_id', models.AutoField(serialize=False, verbose_name='\u5ba2\u6237ID', primary_key=True)),
                ('customer_name', models.CharField(max_length=20, null=True, verbose_name='\u5ba2\u6237\u540d\u79f0', blank=True)),
                ('idno', models.CharField(max_length=20, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7\u7801', blank=True)),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='\u624b\u673a/\u7535\u8bdd', blank=True)),
                ('education', models.CharField(max_length=10, null=True, verbose_name='\u5b66\u5386', blank=True)),
                ('property', models.CharField(max_length=10, null=True, verbose_name='\u623f\u4ea7\u60c5\u51b5', blank=True)),
                ('property_location', models.CharField(max_length=100, null=True, verbose_name='\u623f\u4ea7\u6240\u5728\u5730', blank=True)),
                ('residential_address', models.CharField(max_length=100, null=True, verbose_name='\u5c45\u4f4f\u5730\u5740', blank=True)),
                ('living_conditions', models.CharField(max_length=20, null=True, verbose_name='\u5c45\u4f4f\u60c5\u51b5', blank=True)),
                ('company_name', models.CharField(max_length=50, null=True, verbose_name='\u516c\u53f8\u540d\u79f0', blank=True)),
                ('department', models.CharField(max_length=50, null=True, verbose_name='\u90e8\u95e8', blank=True)),
                ('recruit_time', models.CharField(max_length=50, null=True, verbose_name='\u5165\u804c\u65e5\u671f', blank=True)),
                ('marriage', models.CharField(max_length=10, null=True, verbose_name='\u5a5a\u59fb\u72b6\u51b5', blank=True)),
                ('vehicle', models.CharField(max_length=10, null=True, verbose_name='\u6709\u65e0\u8f66\u4ea7', blank=True)),
                ('residence_address', models.CharField(max_length=100, null=True, verbose_name='\u6237\u7c4d\u5730\u5740', blank=True)),
                ('residence_year', models.CharField(max_length=10, null=True, verbose_name='\u5c45\u4f4f\u5e74\u9650', blank=True)),
                ('company_address', models.CharField(max_length=100, null=True, verbose_name='\u5355\u4f4d\u5730\u5740', blank=True)),
                ('nature', models.CharField(max_length=100, null=True, verbose_name='\u5355\u4f4d\u6027\u8d28', blank=True)),
                ('position', models.CharField(max_length=10, null=True, verbose_name='\u804c\u4f4d', blank=True)),
                ('insert_date', models.DateTimeField(default=datetime.datetime(2015, 3, 12, 7, 57, 43, 905216, tzinfo=utc), verbose_name='\u5bfc\u5165\u65e5\u671f')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'base_info',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
