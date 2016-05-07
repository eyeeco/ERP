$(document).ready(refresh);
$(document).on("click", "#order_search", refresh);
function refresh() {
    var id_work_order = $("#id_work_order").val();

    Dajaxice.techdata.getWeldQuotaList(refreshCallBack, {"id_work_order": id_work_order, });

        
}
function refreshCallBack(data) {
    $(".widget-box2").html(data.html);
    // $("#detail_table").html(data);
}
$(document).on("click", "#btn_weld_quota_write_confirm", function() {
    var id_work_order = $("#id_work_order").val();   
    Dajaxice.techdata.weldQuotaWriterConfirm(weldQuotaWriterConfirmCallBack, {"id_work_order": id_work_order})
});
function weldQuotaWriterConfirmCallBack(data) {
    if(data.ret) {
        $("#span_write").html("编制人：" + data.user);
    }
}

$(document).on("click", "#btn_weld_quota_review_confirm", function() {
    var id_work_order = $("#id_work_order").val();   
    Dajaxice.techdata.weldQuotaReviewerConfirm(weldQuotaReviewerConfirmCallBack, {"id_work_order": id_work_order})
});
function weldQuotaReviewerConfirmCallBack(data) {
    if(data.ret) {
        $("#span_review").html("审核人：" + data.user);
    }
    else {
        alert("未完成编制，无法审核！");
    }
}
$(document).on("dblclick", ".tr_materiel td", function() {
    if($(this).index() != 0) {
        var iid = $(this).parent().attr("iid");
        fill(iid);
        $("#card_modal").modal();
    }
});
function fill(iid) {
    $("#card_modal").attr("iid", iid);
    Dajaxice.techdata.getWeldQuotaCard(getCardCallBack, {"iid": iid});
}
function getCardCallBack(data) {
    $("#weld_quota_card").html(data);
}