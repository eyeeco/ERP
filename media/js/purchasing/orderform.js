var pendingArray = Array();
var order_tr

$(document).ready(refresh);

function refresh() {
    var index = $("#index").val();
    var can_choose = (1 == $("#status").attr("args"));
    Dajaxice.purchasing.getOrderFormItems(getItemsCallBack, {
        "index": index,
        "can_choose": can_choose,
    });

    Dajaxice.purchasing.getOngoingBidList(getBidListCallBack, {});
}
function getBidListCallBack(data) {
    $(".bid-select").each(function() { 
        $(this).html(data);   
    });
}
function getItemsCallBack(data) {
    $("#item_table").html(data);
}

$("#btn-save").click(function() {
    var id = $("#bid_modal").attr("args");
    if(confirm("是否确认保存？")) {
        Dajaxice.purchasing.newBidSave(saveCallBack, {"id": id, "pendingArray": pendingArray, });
        return true;
    }
    return false;
});
function saveCallBack() {
    refresh();
}
$("#btn-finish").click(function() {
    var id = $("#bid_modal").attr("args");
    if(confirm("是否确认完成编制？")) {
        Dajaxice.purchasing.newBidFinish(finishCallBack, {"id": id});
        return true;
    }
    return false;
});
function finishCallBack() {
    refresh();
}

$(".btn-open").click(function() {
    if($(this).hasClass("clear")) {
        pendingArray = Array();
    }
    var id = $($(this).attr("data-source")).val(); // datatable index not bid_id
    Dajaxice.purchasing.getBidForm(getBidCallBack, {"bid_id": id, "pendingArray": pendingArray, })
});

$("#new_purchase_btn").click(function() {
    Dajaxice.purchasing.newBidCreate(getBidCallBack, {});
});

function getBidCallBack(data) {
    $("input#bid_id").val(data.bid_id);
    $("div.table-div").html(data.html);
    $("#bid_modal").attr("args", data.id);
    Dajaxice.purchasing.getOngoingBidList(getBidListCallBack, {});
}
$(document).on("click", "input#select_all", function(){
    var target = this.checked;
    $("input[type='checkbox']").each(function(){
        this.checked = target; 
    });
});


$("#add_to_bid").click(function() {
    pendingArray = Array();
    $("input.checkbox").each(function() {
        if(this.checked) pendingArray.push($(this).attr("args"));
    });
});


$("#order_delete").click(function() {
    var id = $("#bid_modal").attr("args");
    if(confirm("是否确定删除？")) {
        Dajaxice.purchasing.newBidDelete(deleteCallBack, {"id": id});
        return true;
    }
    return false;
});
function deleteCallBack(data) {
    Dajaxice.purchasing.getOngoingBidList(getBidListCallBack, {});
}

$(document).on("click","#edit",function(){
    uid = $(this).attr("uid");
    $("#order_info_modal").modal();
    var tr=$(this).closest("tr");
    if($(tr).attr("mod")=="0"){
        $("#count").val($(tr).children("td:eq(5)").html());
        $("#purchasing").val($(tr).children("td:eq(6)").html());
    }
    else{
        $("#count").val($(tr).children("td:eq(6)"));
    }
    // order_uid = $(this).parent().parent();
   // Dajaxice.purchasing.GetOrderInfoForm(Edit_Order_Callback,{'uid':uid});
});
function Edit_Order_Callback(data){
    $("#order_info_modal").modal();
    $("#order_form_div").html(data.form);
}

$("#order_info_modal #save_order").click(function(){
    //var name = $("#material").val();
    var count =  $("#count").val();
    var purchasing=$("#purchasing").val();
    Dajaxice.purchasing.OrderInfo(Order_Callback,{'uid':uid,'count':count,'purchasing':purchasing});
});
function Order_Callback(data){
    $("#order_info_modal").modal('hide');
    refresh();
}

$("#order_form_finish").click(function(){
    var index = $("#index").val();
    Dajaxice.purchasing.OrderFormFinish(function(data){
        window.location.reload();

    },{
        "index":index
    });

});

$("#save_tech_require").click(function(){
    var content=$("#tech_requirement_textarea").val();
    var order_id=$("#index").val();
    Dajaxice.purchasing.saveTechRequire(function(data){
    $("#tech_requirement_content").val(content);
    },{
        "order_id":order_id,
        "content":content
    });
});

$("#tech_add").click(function(){
    $("#tech_requirement_textarea").val($("#tech_requirement_content").val());
});

$("#generate_execute").click(function(){
    Dajaxice.purchasing.orderformToExecute(function(data){
        $("#execute_form").html(data.html);
    },{
            "orderform_id":$("#index").val()
        });
});

$("#save_materiel_execute").click(function(){
    form=$("#execute_form").children("form");
    Dajaxice.purchasing.saveOrderformExecute(function(data){
        alert(data.message);
        if(data.status=='0'){
            window.location.reload();
        }
    },{

            "orderform_id":$("#index").val(),
            'form':$(form).serialize(true)
    });
});
