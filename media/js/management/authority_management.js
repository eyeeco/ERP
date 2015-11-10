$(document).ready(refresh);
$("#id_auth_type").change(refresh);

function refresh() {
    var auth_type = $("#id_auth_type").val();
    var title_id = $("#widget-content").attr("title_id");
    Dajaxice.management.getAuthList(refreshCallBack, {"auth_type": auth_type, "title_id": title_id});
}
function refreshCallBack(data) {
    $("#widget-content").html(data);
}

var touch;

$(document).on("click", ".btn-addorremove", function() {
    var auth_id = $(this).parent().parent().attr("iid");
    var title_id = $("#widget-content").attr("title_id");
    var flag = $(this).hasClass("btn-success");
    touch = $(this);
    Dajaxice.management.addOrRemoveAuth(dealCallBack, {"auth_id": auth_id, title_id: title_id, "flag": flag});
});
function dealCallBack(data) {
    if(data == "ok") {
        if(touch.hasClass("btn-success")) touch.removeClass("btn-success").addClass("btn-warning").html("取消");
        else touch.removeClass("btn-warning").addClass("btn-success").html("添加");
    }
    else {
        alert("fatal error!");
    }
}
