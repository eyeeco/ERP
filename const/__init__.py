# coding: UTF-8

BIDFORM_STATUS_CREATE=10
BIDFORM_STATUS_SELECT_SUPPLIER=20
BIDFORM_STATUS_INVITE_BID=30
BIDFORM_STATUS_PROCESS_FOLLOW=40
BIDFORM_STATUS_CHECK_STORE=50
BIDFORM_STATUS_COMPLETE=60
BIDFORM_STATUS_STOP=-1

BIDFORM_PART_STATUS_CREATE=10
BIDFORM_PART_STATUS_ESTABLISHMENT=20
BIDFORM_PART_STATUS_APPROVED=30
BIDFORM_PART_STATUS_SELECT_SUPPLLER_APPROVED=40
BIDFORM_PART_STATUS_INVITE_BID_APPLY=50
BIDFORM_PART_STATUS_INVITE_BID_BRANCECORPOR_AOORIVED=60
BIDFORM_PART_STATUS_INVITE_BID_BINHAICORPOR_AOORIVED=70
BIDFORM_PART_STATUS_INVITE_BID_BIDINVITATION_AOORIVED=80
BIDFORM_PART_STATUS_INVITE_BID_WINBIDNOTICE_AOORIVED=90
BIDFORM_PART_STATUS_PROCESS_FOLLOW=100
BIDFORM_PART_STATUS_CHECK=110
BIDFORM_PART_STATUS_STORE=120
BIDFORM_PART_STATUS_COMPLETE=130
BIDFORM_PART_STATUS_STOP=-1


BIDFORM_STATUS_CHOICES=(

    (BIDFORM_STATUS_CREATE,u"标单生成"),
    (BIDFORM_STATUS_SELECT_SUPPLIER,u"供应商选择"),
    (BIDFORM_STATUS_INVITE_BID,u"招标"),
    (BIDFORM_STATUS_PROCESS_FOLLOW,u"过程跟踪"),
    (BIDFORM_STATUS_CHECK_STORE,u"检查入库"),
    (BIDFORM_STATUS_COMPLETE,u"标单完成"),
    (BIDFORM_STATUS_STOP,u"标单终止")
    
)

BIDFORM_PART_STATUS_CHOICES=(
    
    (BIDFORM_PART_STATUS_CREATE,u"标单创建"),
    (BIDFORM_PART_STATUS_ESTABLISHMENT,u"标单编制"),
    (BIDFORM_PART_STATUS_APPROVED,u"标单审批"),
    (BIDFORM_PART_STATUS_SELECT_SUPPLLER_APPROVED,u"供应商选择"),
    (BIDFORM_PART_STATUS_INVITE_BID_APPLY,u"招标申请"),
    (BIDFORM_PART_STATUS_INVITE_BID_BRANCECORPOR_AOORIVED,u"分公司领导批准"),
    (BIDFORM_PART_STATUS_INVITE_BID_BINHAICORPOR_AOORIVED,u"滨海公司领导批准"),
    (BIDFORM_PART_STATUS_INVITE_BID_BIDINVITATION_AOORIVED,u"滨海招标办领导批准"),
    (BIDFORM_PART_STATUS_INVITE_BID_WINBIDNOTICE_AOORIVED,u"中标通知书"),
    (BIDFORM_PART_STATUS_PROCESS_FOLLOW,u"进程跟踪"),
    (BIDFORM_PART_STATUS_CHECK,u"标单检验"),
    (BIDFORM_PART_STATUS_STORE,u"标单入库"),
    (BIDFORM_PART_STATUS_COMPLETE,u"标单完成"),
    (BIDFORM_PART_STATUS_STOP,u"标单终止")
)
IDENTITYERROR = "登录帐号或密码有错误！"


INVENTORY_TYPE = (
    (0, u"主材定额"),
    (1, u"辅料定额"),
    (2, u"先投件明细"),
    (3, u"外购件明细"),
    (4, u"铸锻件明细"),
)

SELL_TYPE = (
    (0, u"内销"),
    (1, u"外销"),
)
