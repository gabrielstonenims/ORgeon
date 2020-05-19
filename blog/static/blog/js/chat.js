$(function () {
  $(".msg_card_body").animate({ scrollTop: +100000 }, 2000);
  $("#action_menu_btn").click(function () {
    $(".action_menu").toggle();
  });


  // for user private chats
  $(document).on("submit",".private-chat-form",function(event){
    event.preventDefault()
    $.ajax({
      type: "POST",
      url: $(this).attr("action"),
      data: $(this).serialize(),
      dataType: "json",
      success: function(response){
        $(".private-message-display").html(response["form"]);
        $("#directmessage").val("");
        $(".msg_card_body").animate({ scrollTop: +100000 }, 2000);
        // console.log("it is working or?")
      },
      error: function(rs, e){
        console.log(rs.responseText);
      }
    })
  })
  
  // for group messages
  $(document).on("submit", ".group-chat-form", function (event) {
    event.preventDefault();
    $.ajax({
      type: "POST",
      url: $(this).attr("action"),
      data: $(this).serialize(),
      dataType: "json",
      success: function (response) {
        $(".group-message-display").html(response["form"]);
        $("#directmessage").val("");
        // console.log(response["all_messages"]);
      },
      error: function (rs, e) {
        console.log(rs.responseText);
      },
    });
  });
});
