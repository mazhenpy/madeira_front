$(document).ready(function () {
    $("#btn1").click(function () {
        $.get("/rand_number", function (data) {
            $("#partnerno").html(data.partner_no);
            $("#contractid").html(data.contract_id);
            $("#key").html(data.key);
            $("#iv").html(data.iv);
            document.getElementById('contract_id').value = data.contract_id;
            document.getElementById('partner_no').value = data.partner_no;
            document.getElementById('timestamp').value = data.timestamp;
            document.getElementById('phone_id').value = data.phone_id;
            document.getElementById('facevalue').value = data.facevalue;
            document.getElementById('order_id').value = data.order_id;
            document.getElementById('plat_offer_id').value = data.plat_offer_id;
            document.getElementById('request_no').value = data.request_no;
            document.getElementById('effect_type').value = data.effect_type;
        });
    });
});