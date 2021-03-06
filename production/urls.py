from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.conf.urls.defaults import *
from production import views as production_views

urlpatterns=patterns('',
    url(
        r'^task_plan$',
        production_views.taskPlanViews,
    ),
    url(
        r'^task_allocation$',
        production_views.taskAllocationViews,
    ),
    url(
        r'^task_confirm$',
        production_views.taskConfirmViews,
    ),
    url(
        r'^materiel_use$',
        production_views.materielUseViews,
    ),
    url(
        r'^materiel_use_add$',
        production_views.materielUseAddViews,
    ),
    url(
        r'^synthesize_filelist$',
        production_views.synthesizeFileListViews,
    ),
    url(
        r'^man_hour_message$',
        production_views.man_hour_messageViews,
    ),
    url(
        r'^man_hour_summarize$',
        production_views.man_hour_summarizeViews,
    ),
    url(
        r'^production_plan$',
        production_views.production_planViews,
    ),
    url(
        r'^ledger$',
        production_views.ledgerViews,
    ),
    url(
        r'^production_user_manage$',
        production_views.production_user_manageViews,
    ),
    url(
        r'^materiel_refund$',
        production_views.materiel_refundViews,
    ),
)
