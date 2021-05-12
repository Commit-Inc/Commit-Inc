$(document).ready(function () {

 
    $('.second-button').on('click', function () {
  
      $('.animated-icon2').toggleClass('open');
    });



    $('#hamb').click(function(){
        var navbar_obj = $($(this).data("target"));
        navbar_obj.toggleClass("open");
      });


    

  });

