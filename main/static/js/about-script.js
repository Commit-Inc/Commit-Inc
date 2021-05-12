$(document).ready(function () {

 
    $('.second-button').on('click', function () {
  
      $('.animated-icon2').toggleClass('open');
    });



    $('#hamb').click(function(){
        var navbar_obj = $($(this).data("target"));
        navbar_obj.toggleClass("open");
      });


    

  });


  $(".get-in-touch").on("mouseenter", (event) => {
    console.log(event);
    document
      .querySelector(".get-in-touch-animation-container")
      .setAttribute(
        "style",
        "border-top-right-radius: 200px; border-top-left-radius: 200px; height: 12.5vw; width: 25vw; bottom:0;  "
      );
  
    document
      .querySelector(".get-in-touch-animation")
      .setAttribute(
        "style",
        "border-top-right-radius: 200px; border-top-left-radius: 200px;  "
      );
  
    document.querySelector(".arrow-text").setAttribute("style", "color:#EBEBEB");
  
    const headings = document.querySelectorAll(".animation-text");
  
    headings.forEach((heading) => {
      heading.setAttribute("style", "color: #646465; border-color:black");
    });
  
    const illustrations = document.querySelectorAll(".appear");
    illustrations.forEach((illustration) => {
      illustration.setAttribute("style", "opacity:1;");
    });
  });
  
  $(".get-in-touch").on("mouseleave", (event) => {
    console.log(event);
    document
      .querySelector(".get-in-touch-animation-container")
      .setAttribute(
        "style",
        "border-top-right-radius: 200px; border-top-left-radius: 200px;  height:80vw ;width: 120vw;"
      );
  
    document
      .querySelector(".get-in-touch-animation")
      .setAttribute(
        "style",
        "border-top-right-radius: 1100px; border-top-left-radius: 1100px;width: 120vw;"
      );
  
    document
      .querySelector(".arrow-text")
      .setAttribute("style", "color:rgb(31, 31, 31)");
  
    const headings = document.querySelectorAll(".animation-text");
  
    headings.forEach((heading) => {
      heading.setAttribute("style", "color: #EBEBEB; border-color:white");
    });
  
    const illustrations = document.querySelectorAll(".appear");
    illustrations.forEach((illustration) => {
      illustration.setAttribute("style", "opacity:0;");
    });
  });
  
  /////////////////////// Contact Form /////////////////////////////////
  
  const reqButton = document.querySelectorAll(".btn-check");
  reqButton.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      const label = event.target.nextElementSibling;
      console.log(label);
      const active = {
        bgColor: "#1E8038",
        textColor: "#F4F4F4",
      };
  
      const passive = {
        bgColor: "#EBEBEB",
        textColor: "#5A5A5A",
      };
  
      if (event.target.checked) {
        label.style.backgroundColor = active.bgColor;
        label.style.color = active.textColor;
      } else {
        label.style.backgroundColor = passive.bgColor;
        label.style.color = passive.textColor;
      }
    });
  });
