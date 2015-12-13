$(document).ready(function () {
    $("#btn3").click(function () {

        var send_order = $("#after").html();
        $.ajax({
            type: "post",
            dataType: "json",
            url: "/send_order",

            data: {
                "send_order": send_order,
            },
            success: function (data) {
                $("#return").html(data.resp_body);
            }
        })
    });
});