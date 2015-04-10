# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from data_importer.importers import XLSXImporter
from django.utils import timezone
from django.contrib.auth.models import User
from crum import get_current_user

class BaseInfo(models.Model):
    EDUCATION_CHOICE = (('初中及以下','初中及以下'),('中专','中专'),('大专','大专'),('大学','大学'),('研究生','研究生'),
                        ('博士及以上','博士及以上'),('其他','其他'))
    VEHICLE_CHOICE = (('0','无'),('1','有'))
    MARRIAGE_CHOICE = (('未婚','未婚'),('已婚','已婚'),('离异','离异'),('丧偶','丧偶'),('其他','其他'))
    PROPERTY_CHOICE = (('无房','无房'),('有房有贷款','有房有贷款'),('有房无贷款','有房无贷款'))
    NATURE_CHOICE = (('其他','其他'),('三资','三资'),('民资','民资'),('国企','国企'),('机关','机关'),('外资','外资'))
    POSITION_CHOICE = (('其他','其他'),('非正式员工','非正式员工'),('正式员工','正式员工'),('一般管理','一般管理'),
                       ('中级管理','中级管理'),('高级管理','高级管理'),('负责人','负责人'),('教师','教师'),
                       ('医生','医生'),('警察','警察'),('退休','退休'))
    SCORING_CHOICE = ((0,'评分未完成'), (1,'评分结果已出'))
    customer_id = models.AutoField(primary_key=True, verbose_name="客户ID")
    customer_name = models.CharField(max_length=20, blank=True, null=True, verbose_name="客户名称")
    idno = models.CharField(max_length=20, blank=True, null=True, verbose_name="身份证号码")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="手机/电话")
    annual_income = models.IntegerField(default=0, verbose_name="年收入")
    apply_quota = models.IntegerField(default=0, verbose_name="申请额度")
    loan_purpose = models.CharField(max_length=50, null=True, verbose_name="借款用途")
    creditcard_quota = models.IntegerField(default=0, verbose_name="信用卡额度")
    education = models.CharField(max_length=10, verbose_name="学历", choices=EDUCATION_CHOICE)
    marriage = models.CharField(max_length=10, default='未婚', verbose_name="婚姻状况", choices=MARRIAGE_CHOICE)
    property = models.CharField(max_length=10,  verbose_name="房产情况", choices=PROPERTY_CHOICE)
    property_location = models.CharField(max_length=100, blank=True, null=True, verbose_name="房产所在地")
    residence_address = models.CharField(max_length=100, blank=True, null=True, verbose_name="户籍地址")
    residence_year = models.CharField(max_length=10, blank=True, null=True, verbose_name="居住年限")
    vehicle = models.CharField(max_length=10, default='0', null=True, verbose_name="有无车产", choices=VEHICLE_CHOICE)
    residential_address = models.CharField(max_length=100, blank=True, null=True, verbose_name="居住地址")
    living_conditions = models.CharField(max_length=20, blank=True, null=True, verbose_name="居住情况")
    company_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="单位名称")
    company_address = models.CharField(max_length=100, blank=True, null=True, verbose_name="单位地址")
    nature = models.CharField(max_length=100, verbose_name="单位性质", choices=NATURE_CHOICE)
    department = models.CharField(max_length=50, blank=True, null=True, verbose_name="部门")
    position = models.CharField(max_length=10, verbose_name="职位", choices=POSITION_CHOICE)
    recruit_time = models.CharField(max_length=50, blank=True, null=True, verbose_name="入职日期")
    insert_date = models.DateTimeField(default=timezone.now(), verbose_name="导入日期")
    scoring_status = models.IntegerField(default=0, verbose_name="评分状态", choices=SCORING_CHOICE)
    create_by = models.ForeignKey(User)
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        user = get_current_user()
        self.create_by = user
        if self.customer_name is None:
            self.customer_name = '客户' + self.customer_id
        super(BaseInfo, self).save(force_insert, force_update, using, update_fields)
    def __unicode__(self):
        return self.customer_name
    class Meta:
        managed = True
        db_table = 'base_info'
class Scoring(models.Model):
    sid = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(to=BaseInfo)
    scoring_status = models.IntegerField(default=0, verbose_name="评分状态")
    scoring = models.CharField(max_length=100, verbose_name="评分结果")
    scoring_detail = models.TextField(verbose_name="评分详细情况")
    class Meta:
        managed = True
        db_table = 'scoring'
class BureauLoanDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(BaseInfo)
    loan_type = models.CharField(max_length=20, null=True,blank=True, verbose_name= '贷款类型')
    account_status = models.CharField(max_length=20, null=True, blank=True, verbose_name= '账户状态')
    service_no = models.CharField(max_length=20, null=True, blank=True, verbose_name='业务号')
    lender = models.CharField(max_length=50, null= True, blank= True, verbose_name='贷款机构')
    guarantee = models.CharField(max_length=20, null=True, blank= True, verbose_name ='担保方式')
    currency = models.CharField(max_length= 20, null=True, blank=True, verbose_name = '币种')
    repayment_fq = models.CharField(max_length=20, null=True, blank=True, verbose_name='还款频率')
    repayment_month = models.CharField(max_length=20, null=True, blank=True, verbose_name= '还款月数')
    release_date = models.DateField(null=True, verbose_name= '发放日期')
    due_date = models.DateField(null=True, verbose_name='到期日期')
    amount = models.FloatField(null=True, verbose_name = '合同金额')
    balance = models.DecimalField(null=True, max_digits=20, decimal_places=2, verbose_name='贷款余额')
    remaining_month = models.IntegerField(null=True, verbose_name='剩余还款月数')
    recent_repayment = models.DateField(null=True, verbose_name= '最近一次实际还款日期')
    repayment_current = models.DecimalField(max_digits=15, decimal_places=2, verbose_name= '本月应还款金额')
    repayment_actual_current = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='本月实际还款金额')
    overdue_times = models.IntegerField(verbose_name='当前逾期期数')
    overdue_amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='当前逾期总额')
    overdue_times_cumulate = models.IntegerField(verbose_name='累计逾期次数')
    overdue_times_max = models.IntegerField(verbose_name='最高逾期期数')
    over_31 = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='逾期31至60天未归还贷款本金')
    over_61 = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='逾期61至90天未归还贷款本金')
    over_91 = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='逾期91至180天未归还贷款本金')
    over_180 = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='逾期180天以上未归还贷款本金')
    insert_date = models.DateTimeField(default=timezone.now())
    class Meta:
        managed = True
        db_table = 'BUREAU_LOAN_D'

#人行报告最近24个月贷款每月还款状态记录
class BureauLoanRepayment(models.Model):
    repayment_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(BaseInfo)
    billing_date = models.DateField(verbose_name='结算年月')
    month_no = models.IntegerField()
    status = models.CharField(max_length=2, verbose_name='状态代码')
    insert_date = models.DateTimeField(default=timezone.now())
    class Meta:
        managed = True
        db_table = "BUREAU_LOAN_REPAYMENT"

#人行报告个人住房公积金信息
class BureauPFund(models.Model):
    fund_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(BaseInfo)
    company = models.CharField(max_length=50, verbose_name = '单位名称')
    account_date = models.DateField(verbose_name='开户日期')
    payment_date_b = models.DateField(verbose_name='初缴年月')
    payment_date_e = models.DateField(verbose_name='缴至年月')
    payment_date_l = models.DateField(verbose_name='最近一次交缴日期')
    company_ratio = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='单位缴存比例')
    personal_ratio = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='个人缴存比例')
    amount_monthly = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='月缴存额')
    data_date = models.DateField(verbose_name='信息获取时间')
    insert_date = models.DateTimeField(default=timezone.now())
    class Meta:
        managed = True
        db_table = "BUREAU_P_FUND"

class BaseInfoImporterModel(XLSXImporter):

    class Meta:
        model = BaseInfo
        ignore_first_line = True
        ignore_empty_lines = True
        exclude = ['customer_id', 'insert_date', 'user']
