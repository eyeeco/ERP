$(document).ready(refresh);
$("#search_user_button").click(refresh);

function refresh() {
    getList("1")
}

function getList(page) {
    var search_user = $("#search_user").val();
    Dajaxice.management.searchUser(searchUserCallBack, {
                                                     "search_user": search_user,
                                                     "page": page,
    });

}
$(document).on("click", ".item_page", function() {
    var page = $(this).attr("arg");   
    getList(page);
});

function createUserCallBack(data) {
    if(data == "fail") {
	        alert("用户重名,添加失败!");
    }
    else {
        refresh();
    }
}

function searchUserCallBack(data){
    $("#widget-content").html(data);
}
$("#user-add").click(function() {
    $("#titleLabel").html("新建用户");

});

$("#user-save").click(function() {
    var user_name = $("#user_name").val();
    var user_password = $("#user_password").val();
    var user_fullname = $("#user_fullname").val();
    Dajaxice.management.createUser(createUserCallBack, {
                                                    "user_name": user_name,
                                                    "user_password": user_password,
                                                    "user_fullname": user_fullname,  
                                            });
});


$(document).on("click", ".btn-set-title", function() {
     user_id = $(this).parent().parent().attr("iid");
     location.href = "/management/titleSetting?user_id=" + user_id;
});


$(document).on("click", ".btn-delete", function() {
    user_id = $(this).parent().parent().attr("iid");
    if(confirm("你确定删除该用户？")) {
        Dajaxice.management.deleteUser(refresh, {"user_id": user_id});
    }
});
