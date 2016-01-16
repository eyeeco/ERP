#!/usr/bin/env python
# coding=utf-8

from django.contrib import admin
from techdata.models  import *

RegisterClass = (
    Processing,
    CirculationRoute,
    CirculationName,
    ProcessReview,
    WeldSeam,
    WeldSeamType,
    WeldMethod,
    NondestructiveInspection,
    WeldListPageMark,
)

for item in RegisterClass:
    admin.site.register(item)
