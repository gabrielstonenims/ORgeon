$(function() {
  setTimeout(function() {
    $(".alert").slideUp(3000);
  }, 5000);

  $(document).on("submit", ".post-comment-form", function(event) {
    event.preventDefault();
    $.ajax({
      type: "POST",
      url: $(this).attr("action"),
      data: $(this).serialize(),
      dataType: "json",
      success: function(response) {
        $(".main-comment-section").html(response["form"]);
        $("textarea").val("");
      },
      error: function(rs, e) {
        console.log(rs.responseText);
      }
    });
  });

  // for the charts
 
});
