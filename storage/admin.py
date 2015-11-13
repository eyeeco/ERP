#coding=UTF-8
from models import *

from django.contrib import admin
from storage.models import *

Registers = (
    WeldingMaterialApplyCard,
    StoreRoom,
    WeldingMaterialHumitureRecord,
    SteelMaterialPurchasingEntry,
    SteelMaterial,
    BoardSteelMaterialLedger,
    BarSteelMaterialLedger,
    CommonSteelMaterialReturnCardInfo,
    BoardSteelMaterialReturnCardContent,
    BarSteelMaterialReturnCardContent
    WeldRefund,
    AuxiliaryTool,
    AuxiliaryToolApplyCard,
)

for reg in Registers:
    admin.site.register(reg)
