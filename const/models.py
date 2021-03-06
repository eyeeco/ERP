# coding: UTF-8
from django.db import models
from const import *
from django.contrib.auth.models import User

class WorkOrder(models.Model):
    order_index = models.CharField(blank = False, unique = True, max_length = 20, verbose_name = u"工作令编号")
    sell_type = models.IntegerField(blank = False, choices = SELL_TYPE, verbose_name = "销售类型")
    client_name = models.CharField(blank = False, max_length = 100, verbose_name = "客户名称")
    project_name = models.CharField(blank = False, max_length = 100, verbose_name = "项目名称")
    product_name = models.CharField(blank = False, max_length = 100, verbose_name = "产品名称")
    count = models.CharField(blank = False, max_length = 20, verbose_name = u"数量")
    is_finish = models.BooleanField(default = False, verbose_name = u"是否结束")
    class Meta:
        verbose_name = u"工作令"
        verbose_name_plural = u"工作令"

    def save(self, *args, **kwargs):
        super(WorkOrder, self).save(*args, **kwargs)
        if SubWorkOrder.objects.filter(order = self).count() > 0:
            return
        if self.count == "1":
            SubWorkOrder(order = self, index = "1",name = self.order_index).save()
        else:
            for i in xrange(int(self.count)):
                SubWorkOrder(order = self, index = str(i + 1),name=self.order_index+"-"+str(i+1)).save()
    def suffix(self):
        return self.order_index[2:]
    def __unicode__(self):
        return self.order_index
    def getSellType(self):
        return self.get_sell_type_display

class SubWorkOrder(models.Model):
    order = models.ForeignKey(WorkOrder, verbose_name = u"所属工作令")
    index = models.CharField(max_length = 100, verbose_name = "序号")
    name = models.CharField(max_length = 100, verbose_name = "工作令名")
    is_finish = models.BooleanField(default = False, verbose_name = u"是否结束")
    class Meta:
        verbose_name = u"子工作令"
        verbose_name_plural = u"子工作令"
    def __unicode__(self):
        if self.order.count == "1":
            return self.order.order_index
        return self.order.order_index + "-" + self.index

class Material(models.Model):
    name = models.CharField(blank = False, max_length = 50, verbose_name = u"材质名称")
    material_id= models.CharField(blank = True, null = True , max_length = 20, verbose_name = u"材质编号")
    categories =  models.CharField(blank = True, null = True , choices = MATERIAL_CATEGORY_CHOICES, max_length = 20, verbose_name = u"材料类别")
    class Meta:
        verbose_name = u"材料"
        verbose_name_plural = u"材料"
    def __unicode__(self):
        return self.name
    def display_material_name(self):
        return "%s" % (self.categories)

class InventoryType(models.Model):
    name = models.CharField(blank = False, max_length = 50, choices = INVENTORY_TYPE, verbose_name = u"明细表名称")
    class Meta:
        verbose_name = u"明细表类别"
        verbose_name_plural = u"明细表类别"
    def __unicode__(self):
        return self.get_name_display()

class Materiel(models.Model):
    order = models.ForeignKey(WorkOrder, blank = True, null = True, verbose_name = u"所属工作号")
    index = models.CharField(blank = True, max_length = 20, verbose_name = u"票号")
    sub_index = models.CharField(blank = True, null = True, max_length = 20, verbose_name = u"部件号")
    schematic_index = models.CharField(blank = True, null = True, max_length = 50, verbose_name = u"图号")
    parent_schematic_index = models.CharField(blank = True, null = True, max_length = 50, verbose_name = u"部件图号")
    parent_name = models.CharField(blank = True, null = True, max_length = 100, verbose_name = u"部件名称")
    material = models.ForeignKey(Material, blank = True, null = True, verbose_name = u"材质")
    name = models.CharField(blank = True, max_length = 100, verbose_name = u"名称")
    count = models.CharField(blank = True, max_length = 20, null = True, verbose_name = u"数量")
    net_weight = models.FloatField(blank = True, null = True, verbose_name = u"净重")
    total_weight = models.FloatField(blank = True, null = True, verbose_name = u"毛重")
    quota = models.FloatField(blank = True, null = True, verbose_name = u"定额")
    quota_coefficient = models.FloatField(blank = True, null = True, verbose_name = u"定额系数")
    remark = models.CharField(blank = True, null = True, max_length = 100, verbose_name = u"备注")
    specification = models.CharField(blank = True, null = True , max_length = 20, verbose_name = u"规格")
    standard = models.CharField(blank = True, null = True , max_length = 20, verbose_name = u"标准")
    unit = models.CharField(blank = True, null = True , max_length = 20, verbose_name = u"单位")
    status = models.CharField(blank = True, null = True , max_length = 20, verbose_name = u"状态")
    press=models.CharField(blank=True,null=True,max_length=20,verbose_name=u"受压")
    recheck=models.CharField(blank=True,null=True,max_length=20,verbose_name=u"复验")
    detection_level=models.CharField(blank=True,null=True,max_length=20,verbose_name=u"探伤级别")

    def total_weight_cal(self):
        if self.count and self.net_weight:
            return int(self.count) * self.net_weight
    def route(self):
        route_list = []
        for i in xrange(1, 11):
            step = getattr(self.circulationroute, "L%d" % i)
            if step == None: break
            route_list.append(step.get_name_display())
        return '.'.join(route_list)
    class Meta:
        verbose_name = u"物料"
        verbose_name_plural = u"物料"
    def __unicode__(self):
        return self.name


class BidFormStatus(models.Model):
    #status=models.IntegerField(blank=False,unique=True,choices=BIDFORM_STATUS_CHOICES,verbose_name=u"标单状态")
    main_status=models.IntegerField(blank=False,choices=BIDFORM_STATUS_CHOICES,verbose_name=u"标单状态")
    part_status=models.IntegerField(blank=False,unique=True,choices=BIDFORM_PART_STATUS_CHOICES,verbose_name=u"子状态")
    next_part_status=models.ForeignKey('self',null=True,blank=True)
    class Meta:
        verbose_name = u"标单状态"
        verbose_name_plural = u"标单状态"
    def __unicode__(self):
        return self.get_part_status_display()

class OrderFormStatus(models.Model):
    status = models.IntegerField(blank = False, choices = ORDERFORM_STATUS_CHOICES, verbose_name = u"订购单状态")
    next_status = models.ForeignKey('self', null = True, blank = True)
    class Meta:
        verbose_name = u"订购单状态"
        verbose_name_plural = u"订购单状态"
    def __unicode__(self):
        return self.get_status_display()

class ImplementClassChoices(models.Model):
    category = models.IntegerField(blank = False, choices = IMPLEMENT_CLASS_CHOICES, verbose_name = u"实施类别")
    class Meta:
        verbose_name = u"实施类别"
        verbose_name_plural = u"实施类别"
    def __unicode__(self):
        return self.get_category_display()
