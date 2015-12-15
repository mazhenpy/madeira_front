$(document).ready(function () {
    $("#btn4").click(function () {

        var callback_data = $("#callback").html();
        var backurl = $("#backurl").val();

        if (backurl.length==0){
            $("#callback_url").html('#请输入回调地址');
        }

        $.ajax({
            type: "post",
            dataType: "json",
            url: "/callback_down",

            data: {
                "backurl": backurl,
                "callback_data": callback_data
            },
            success: function (data) {
                $("#callback_url").html('#已发送');
            }

        })
    });
});