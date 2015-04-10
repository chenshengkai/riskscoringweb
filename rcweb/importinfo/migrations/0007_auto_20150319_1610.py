# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('importinfo', '0006_auto_20150313_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseinfo',
            name='scoring_status',
            field=models.IntegerField(default=0, verbose_name='\u8bc4\u5206\u72b6\u6001'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='company_name',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5355\u4f4d\u540d\u79f0', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='education',
            field=models.CharField(max_length=10, null=True, verbose_name='\u5b66\u5386', choices=[('\u521d\u4e2d\u53ca\u4ee5\u4e0b', '\u521d\u4e2d\u53ca\u4ee5\u4e0b'), ('\u4e2d\u4e13', '\u4e2d\u4e13'), ('\u5927\u4e13', '\u5927\u4e13'), ('\u5927\u5b66', '\u5927\u5b66'), ('\u7814\u7a76\u751f', '\u7814\u7a76\u751f'), ('\u535a\u58eb\u53ca\u4ee5\u4e0a', '\u535a\u58eb\u53ca\u4ee5\u4e0a'), ('\u5176\u4ed6', '\u5176\u4ed6')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 19, 8, 10, 9, 656182, tzinfo=utc), verbose_name='\u5bfc\u5165\u65e5\u671f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='loan_purpose',
            field=models.CharField(max_length=50, null=True, verbose_name='\u501f\u6b3e\u7528\u9014'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='marriage',
            field=models.CharField(default='\u672a\u5a5a', max_length=10, null=True, verbose_name='\u5a5a\u59fb\u72b6\u51b5', choices=[('\u672a\u5a5a', '\u672a\u5a5a'), ('\u5df2\u5a5a', '\u5df2\u5a5a'), ('\u79bb\u5f02', '\u79bb\u5f02'), ('\u4e27\u5076', '\u4e27\u5076'), ('\u5176\u4ed6', '\u5176\u4ed6')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='nature',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5355\u4f4d\u6027\u8d28', choices=[('\u5176\u4ed6', '\u5176\u4ed6'), ('\u4e09\u8d44', '\u4e09\u8d44'), ('\u6c11\u8d44', '\u6c11\u8d44'), ('\u56fd\u4f01', '\u56fd\u4f01'), ('\u673a\u5173', '\u673a\u5173'), ('\u5916\u8d44', '\u5916\u8d44')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='position',
            field=models.CharField(max_length=10, null=True, verbose_name='\u804c\u4f4d', choices=[('\u5176\u4ed6', '\u5176\u4ed6'), ('\u975e\u6b63\u5f0f\u5458\u5de5', '\u975e\u6b63\u5f0f\u5458\u5de5'), ('\u6b63\u5f0f\u5458\u5de5', '\u6b63\u5f0f\u5458\u5de5'), ('\u4e00\u822c\u7ba1\u7406', '\u4e00\u822c\u7ba1\u7406'), ('\u4e2d\u7ea7\u7ba1\u7406', '\u4e2d\u7ea7\u7ba1\u7406'), ('\u9ad8\u7ea7\u7ba1\u7406', '\u9ad8\u7ea7\u7ba1\u7406'), ('\u8d1f\u8d23\u4eba', '\u8d1f\u8d23\u4eba'), ('\u6559\u5e08', '\u6559\u5e08'), ('\u533b\u751f', '\u533b\u751f'), ('\u8b66\u5bdf', '\u8b66\u5bdf'), ('\u9000\u4f11', '\u9000\u4f11')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='property',
            field=models.CharField(max_length=10, null=True, verbose_name='\u623f\u4ea7\u60c5\u51b5', choices=[('\u65e0\u623f', '\u65e0\u623f'), ('\u6709\u623f\u6709\u8d37\u6b3e', '\u6709\u623f\u6709\u8d37\u6b3e'), ('\u6709\u623f\u65e0\u8d37\u6b3e', '\u6709\u623f\u65e0\u8d37\u6b3e')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='vehicle',
            field=models.CharField(default='0', max_length=10, null=True, verbose_name='\u6709\u65e0\u8f66\u4ea7', choices=[('0', '\u65e0'), ('1', '\u6709')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bureauloandetail',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 19, 8, 10, 9, 657757, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bureauloanrepayment',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 19, 8, 10, 9, 658643, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bureaupfund',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 19, 8, 10, 9, 659378, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
