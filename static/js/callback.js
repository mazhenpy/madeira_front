$(document).ready(function () {
    $("#btn4").click(function () {

        var backurl = $("#backurl").val();
        var order_id = $("#order_id").val();
        $.ajax({
            type: "post",
            dataType: "json",
            url: "/callback_down",

            data: {
                "backurl": backurl,
                "order_id": order_id
            },
            success: function (data) {
                $("#callback").html(data.data);
            }
        })
    });
});