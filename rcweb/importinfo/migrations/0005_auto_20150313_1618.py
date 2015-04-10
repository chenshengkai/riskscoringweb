# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('importinfo', '0004_auto_20150312_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='BureauLoanDetail',
            fields=[
                ('detail_id', models.AutoField(serialize=False, primary_key=True)),
                ('loan_type', models.CharField(max_length=20, null=True, verbose_name='\u8d37\u6b3e\u7c7b\u578b', blank=True)),
                ('account_status', models.CharField(max_length=20, null=True, verbose_name='\u8d26\u6237\u72b6\u6001', blank=True)),
                ('service_no', models.CharField(max_length=20, null=True, verbose_name='\u4e1a\u52a1\u53f7', blank=True)),
                ('lender', models.CharField(max_length=50, null=True, verbose_name='\u8d37\u6b3e\u673a\u6784', blank=True)),
                ('guarantee', models.CharField(max_length=20, null=True, verbose_name='\u62c5\u4fdd\u65b9\u5f0f', blank=True)),
                ('currency', models.CharField(max_length=20, null=True, verbose_name='\u5e01\u79cd', blank=True)),
                ('repayment_fq', models.CharField(max_length=20, null=True, verbose_name='\u8fd8\u6b3e\u9891\u7387', blank=True)),
                ('repayment_month', models.CharField(max_length=20, null=True, verbose_name='\u8fd8\u6b3e\u6708\u6570', blank=True)),
                ('release_date', models.DateField(null=True, verbose_name='\u53d1\u653e\u65e5\u671f')),
                ('due_date', models.DateField(null=True, verbose_name='\u5230\u671f\u65e5\u671f')),
                ('amount', models.FloatField(null=True, verbose_name='\u5408\u540c\u91d1\u989d')),
                ('balance', models.DecimalField(null=True, verbose_name='\u8d37\u6b3e\u4f59\u989d', max_digits=20, decimal_places=2)),
                ('remaining_month', models.IntegerField(null=True, verbose_name='\u5269\u4f59\u8fd8\u6b3e\u6708\u6570')),
                ('recent_repayment', models.DateField(null=True, verbose_name='\u6700\u8fd1\u4e00\u6b21\u5b9e\u9645\u8fd8\u6b3e\u65e5\u671f')),
                ('repayment_current', models.DecimalField(verbose_name='\u672c\u6708\u5e94\u8fd8\u6b3e\u91d1\u989d', max_digits=15, decimal_places=2)),
                ('repayment_actual_current', models.DecimalField(verbose_name='\u672c\u6708\u5b9e\u9645\u8fd8\u6b3e\u91d1\u989d', max_digits=15, decimal_places=2)),
                ('overdue_times', models.IntegerField(verbose_name='\u5f53\u524d\u903e\u671f\u671f\u6570')),
                ('overdue_amount', models.DecimalField(verbose_name='\u5f53\u524d\u903e\u671f\u603b\u989d', max_digits=15, decimal_places=2)),
                ('overdue_times_cumulate', models.IntegerField(verbose_name='\u7d2f\u8ba1\u903e\u671f\u6b21\u6570')),
                ('overdue_times_max', models.IntegerField(verbose_name='\u6700\u9ad8\u903e\u671f\u671f\u6570')),
                ('over_31', models.DecimalField(verbose_name='\u903e\u671f31\u81f360\u5929\u672a\u5f52\u8fd8\u8d37\u6b3e\u672c\u91d1', max_digits=15, decimal_places=2)),
                ('over_61', models.DecimalField(verbose_name='\u903e\u671f61\u81f390\u5929\u672a\u5f52\u8fd8\u8d37\u6b3e\u672c\u91d1', max_digits=15, decimal_places=2)),
                ('over_91', models.DecimalField(verbose_name='\u903e\u671f91\u81f3180\u5929\u672a\u5f52\u8fd8\u8d37\u6b3e\u672c\u91d1', max_digits=15, decimal_places=2)),
                ('over_180', models.DecimalField(verbose_name='\u903e\u671f180\u5929\u4ee5\u4e0a\u672a\u5f52\u8fd8\u8d37\u6b3e\u672c\u91d1', max_digits=15, decimal_places=2)),
                ('insert_date', models.DateTimeField(default=datetime.datetime(2015, 3, 13, 8, 18, 19, 938096, tzinfo=utc))),
                ('customer_id', models.ForeignKey(to='importinfo.BaseInfo')),
            ],
            options={
                'db_table': 'BUREAU_LOAN_D',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BureauLoanRepayment',
            fields=[
                ('repayment_id', models.AutoField(serialize=False, primary_key=True)),
                ('billing_date', models.DateField(verbose_name='\u7ed3\u7b97\u5e74\u6708')),
                ('month_no', models.IntegerField()),
                ('status', models.CharField(max_length=2, verbose_name='\u72b6\u6001\u4ee3\u7801')),
                ('insert_date', models.DateTimeField(default=datetime.datetime(2015, 3, 13, 8, 18, 19, 938938, tzinfo=utc))),
                ('customer_id', models.ForeignKey(to='importinfo.BaseInfo')),
            ],
            options={
                'db_table': 'BUREAU_LOAN_REPAYMENT',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BureauPFund',
            fields=[
                ('fund_id', models.AutoField(serialize=False, primary_key=True)),
                ('company', models.CharField(max_length=50, verbose_name='\u5355\u4f4d\u540d\u79f0')),
                ('account_date', models.DateField(verbose_name='\u5f00\u6237\u65e5\u671f')),
                ('payment_date_b', models.DateField(verbose_name='\u521d\u7f34\u5e74\u6708')),
                ('payment_date_e', models.DateField(verbose_name='\u7f34\u81f3\u5e74\u6708')),
                ('payment_date_l', models.DateField(verbose_name='\u6700\u8fd1\u4e00\u6b21\u4ea4\u7f34\u65e5\u671f')),
                ('company_ratio', models.DecimalField(verbose_name='\u5355\u4f4d\u7f34\u5b58\u6bd4\u4f8b', max_digits=5, decimal_places=2)),
                ('personal_ratio', models.DecimalField(verbose_name='\u4e2a\u4eba\u7f34\u5b58\u6bd4\u4f8b', max_digits=5, decimal_places=2)),
                ('amount_monthly', models.DecimalField(verbose_name='\u6708\u7f34\u5b58\u989d', max_digits=15, decimal_places=2)),
                ('data_date', models.DateField(verbose_name='\u4fe1\u606f\u83b7\u53d6\u65f6\u95f4')),
                ('insert_date', models.DateTimeField(default=datetime.datetime(2015, 3, 13, 8, 18, 19, 939617, tzinfo=utc))),
                ('customer_id', models.ForeignKey(to='importinfo.BaseInfo')),
            ],
            options={
                'db_table': 'BUREAU_P_FUND',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='baseinfo',
            name='annual_income',
            field=models.IntegerField(default=0, null=True, verbose_name='\u5e74\u6536\u5165'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='baseinfo',
            name='apply_quota',
            field=models.DecimalField(default=0, verbose_name='\u7533\u8bf7\u989d\u5ea6', max_digits=15, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='baseinfo',
            name='creditcard_quota',
            field=models.DecimalField(default=0, verbose_name='\u4fe1\u7528\u5361\u989d\u5ea6', max_digits=15, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='baseinfo',
            name='loan_purpose',
            field=models.CharField(max_length=50, null=True, verbose_name='\u501f\u6b3e\u7528\u9014', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 8, 18, 19, 936678, tzinfo=utc), verbose_name='\u5bfc\u5165\u65e5\u671f'),
            preserve_default=True,
        ),
    ]
