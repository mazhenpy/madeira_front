$(function(){
     $("#contract_id").bind('blur',function(){
       var contract_id=$("#contract_id").val();
       $.ajax({
        type:"POST",
        url:"/ajax_contract_id",
        data:{'contract_id':contract_id},
        dataType:"json",
        success: function(data) {
          $("#error1").html(data.error);
        }
      });
     })
  });

$(function(){
     $("#partner_no").bind('blur',function(){
       var partner_no=$("#partner_no").val();
       $.ajax({
        type:"POST",
        url:"/ajax_partner_no",
        data:{'partner_no':partner_no},
        dataType:"json",
        success: function(data) {
          $("#error2").html(data.error);
        }
      });
     })
  });

$(function(){
     $("#phone_id").bind('blur',function(){
       var phone_id=$("#phone_id").val();
       $.ajax({
        type:"POST",
        url:"/ajax_phone_id",
        data:{'phone_id':phone_id},
        dataType:"json",
        success: function(data) {
          $("#error3").html(data.error);
        }
      });
     })
  });

$(function(){
     $("#plat_offer_id").bind('blur',function(){
       var plat_offer_id=$("#plat_offer_id").val();
       var phone_id=$("#phone_id").val();
       $.ajax({
        type:"POST",
        url:"/ajax_plat_offer_id",
        data:{'plat_offer_id':plat_offer_id,
                'phone_id':phone_id
        },
        dataType:"json",
        success: function(data) {
          $("#error4").html(data.error);
        }
      });
     })
  });

$(function(){
     $("#facevalue").bind('blur',function(){
       var phone_id=$("#phone_id").val();
       var facevalue=$("#facevalue").val();
       var plat_offer_id=$("#plat_offer_id").val();
       $.ajax({
        type:"POST",
        url:"/ajax_facevalue",
        data:{'facevalue':facevalue,
              'plat_offer_id':plat_offer_id,
              'phone_id':phone_id
        },
        dataType:"json",
        success: function(data) {
          $("#error5").html(data.error);
        }
      });
     })
  });

$(function(){
     $("#order_id").bind('blur',function(){
       var order_id=$("#order_id").val();
       $.ajax({
        type:"POST",
        url:"/ajax_order_id",
        data:{'order_id':order_id},
        dataType:"json",
        success: function(data) {
          $("#error6").html(data.error);
        }
      });
     })
  });

$(function(){
     $("#effect_type").bind('blur',function(){
       var effect_type=$("#effect_type").val();
       $.ajax({
        type:"POST",
        url:"/ajax_effect_type",
        data:{'effect_type':effect_type},
        dataType:"json",
        success: function(data) {
          $("#error7").html(data.error);
        }
      });
     })
  });

$(function(){
     $("#request_no").bind('blur',function(){
       var request_no=$("#request_no").val();
       $.ajax({
        type:"POST",
        url:"/ajax_request_no",
        data:{'request_no':request_no},
        dataType:"json",
        success: function(data) {
          $("#error8").html(data.error);
        }
      });
     })
  });

$(function(){
     $("#timestamp").bind('blur',function(){
       var timestamp=$("#timestamp").val();
       $.ajax({
        type:"POST",
        url:"/ajax_timestamp",
        data:{'timestamp':timestamp},
        dataType:"json",
        success: function(data) {
          $("#error9").html(data.error);
        }
      });
     })
  });