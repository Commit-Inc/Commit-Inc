$(document).ready(function () {
  $(".second-button").on("click", function () {
    $(".animated-icon2").toggleClass("open");
  });

  $("#hamb").click(function () {
    var navbar_obj = $($(this).data("target"));
    navbar_obj.toggleClass("open");
  });
});

function isScrolledIntoView($elem, $window) {
  var docViewTop = $window.scrollTop();
  var docViewBottom = docViewTop + $window.height();

  var elemTop = $elem.offset().top;
  var elemBottom = elemTop + $elem.height();

  return elemBottom <= docViewBottom;
}

var $window = $(window);
var $elem = $(".draw");

$(document).on("scroll", function () {
  if (isScrolledIntoView($elem, $window)) {
    for (let i = 1; i < 7; i++) {
      document.querySelectorAll(`.o-${i}`).forEach((element) => {
        element.classList.add(`outline-${i}`);
      });
    }

    document.querySelectorAll(".evo").forEach((element) => {
      element.classList.add("evolve");
    });
  }

  for (let i = 1; i < 7; i++) {
    let outline = document.querySelectorAll(".outline-" + i);

    if (i == 2 || i == 5) {
      let length = outline[0].getTotalLength();
      outline[0].style.strokeDasharray = length;
      outline[0].style.strokeDashoffset = length;
      length = outline[1].getTotalLength();
      outline[1].style.strokeDasharray = length;
      outline[1].style.strokeDashoffset = "-" + length;
    } else if (i == 4) {
      outline.forEach((out) => {
        let length = out.getTotalLength();
        out.style.strokeDasharray = length;
        out.style.strokeDashoffset = "-" + length;
      });
    } else {
      outline.forEach((out) => {
        let length = out.getTotalLength();
        out.style.strokeDasharray = length;
        out.style.strokeDashoffset = length;
      });
    }
  }
});
