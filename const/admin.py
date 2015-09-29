#!/usr/bin/env python
# coding=utf-8

from django.contrib import admin
from const.models  import *

RegisterClass = (
    BidFormStatus,
    WorkOrder,
    Materiel,
    Material,
    CirculationRoute,
    CirculationName,
)

for item in RegisterClass:
    admin.site.register(item)
