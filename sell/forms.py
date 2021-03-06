#!/usr/bin/env python
# coding=utf-8
from django import forms
from const import REVIEW_COMMENTS_CHOICES
from sell.models import Product
from const.models import WorkOrder

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {"name"}
        widgets = {
            "mame" : forms.TextInput(attrs = {
                "class" : "input-medium"
            })
        }

class BidFileAuditForm(forms.Form):
    status = forms.ChoiceField(choices = REVIEW_COMMENTS_CHOICES, widget = forms.Select(attrs = {"class" : "input-medium"}))
    bid = forms.CharField(widget = forms.TextInput(attrs = {"style" : "display : none"}))

class WorkOrderGenerateForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        exclude = {"id", "product_name", "is_finish"}
        widgets = {
            "order_index" : forms.TextInput(attrs = {"class" : "input-medium"}),
            "sell_type" : forms.Select(attrs = {"class" : "input-medium"}),
            "client_name" : forms.TextInput(attrs = {"class" : "input-medium"}),
            "project_name" : forms.TextInput(attrs = {"class" : "input-medium"}),
            "count" : forms.TextInput(attrs = {"class" : "input-medium"}),
        }
