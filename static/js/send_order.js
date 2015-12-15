$(document).ready(function () {
    $("#btn3").click(function () {
        var phone_id = $("#phone_id").val();
        var facevalue = $("#facevalue").val();
        var order_id = $("#order_id").val();
        var plat_offer_id = $("#plat_offer_id").val();

        var send_order = $("#after").html();
        $.ajax({
            type: "post",
            dataType: "json",
            url: "/send_order",

            data: {
                "phone_id": phone_id,
                "facevalue": facevalue,
                "order_id": order_id,
                "plat_offer_id": plat_offer_id,
                "send_order": send_order,
            },
            success: function (data) {
                $("#return").html(data.resp_body);
                $("#callback").html(data.callback_data);
            }
        })
    });
});