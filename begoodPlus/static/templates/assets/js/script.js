$("#productInp1").change(function () {
    var username = $(this).val();
    console.log('changed');

    $.ajax({
      url: '/api/products/',
/*      data: {
        'username': username
      },
*/
      dataType: 'json',
      success: function (data) {
        console.log(data)
      }
    });

  });


$(document).ready(function(){
    $.ajax({ url: "/api/products/",
        success: function(){
            console.log(data)

           alert("done");
        }});
});