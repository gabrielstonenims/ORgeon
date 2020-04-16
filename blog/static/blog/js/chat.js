
$(function(){
  $(".msg_card_body").animate({ scrollTop: +400 }, 2000);
  console.log("scrolling");
  $("#action_menu_btn").click(function () {
    $(".action_menu").toggle();
  });
})