$(function() {
  setTimeout(function() {
    $(".alert").slideUp(3000);
  }, 5000);



    $(document).on("submit",".post-comment-form",function(event){
      event.preventDefault()
      $.ajax({
        type:"POST", 
        url:$(this).attr('action'),
        data:$(this).serialize(),
        dataType:'json',
        success:function(response){
          $(".main-comment-section").html(response['form'])
          $("textarea").val("")
        },
        error:function(rs,e){
          console.log(rs.responseText)
        }
      })
    })

    // svg get stroke dash array
    const logo = document.querySelectorAll("#logo path")
    for(let i=0;i<logo.length;i++){
      console.log(`Letter ${i} is ${logo[i].getTotalLength()}`)
    }
});

