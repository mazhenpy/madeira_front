$(document).ready(function () {
    $("#btn2").click(function () {
        var contract_id = $("#contract_id").val();
        var partner_no = $("#partner_no").val();
        var phone_id = $("#phone_id").val();
        var facevalue = $("#facevalue").val();
        var order_id = $("#order_id").val();
        var effect_type = $("#effect_type").val();
        var plat_offer_id = $("#plat_offer_id").val();
        var request_no = $("#request_no").val();
        var timestamp = $("#timestamp").val();

        $.ajax({
            type: "post",
            dataType: "json",
            url: "/send_msg",

            data: {
                "partner_no": partner_no,
                "contract_id": contract_id,
                "order_id": order_id,
                "facevalue": facevalue,
                "plat_offer_id": plat_offer_id,
                "phone_id": phone_id,
                "request_no": order_id,
                "timestamp": timestamp,
                "effect_type": effect_type
            },
            success: function (data) {
                $("#before").html(data.beforedata);
                $("#after").html(data.afterdata);
            }
        })
    });
});