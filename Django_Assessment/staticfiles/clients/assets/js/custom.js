$(document).ready(function () {});

var video = document.getElementById("banner-video");
var btn = document.getElementById("video-button");

video.play();

function videoFunction() {
  if (video.paused) {
    video.play();
    btn.innerHTML = "<span class='video-icon-span pause-video-icon'>  </span> ";
  } else {
    video.pause();
    btn.innerHTML = "<span class='video-icon-span play-video-icon'> </span> ";
  }
}
$(".video-play-pause").on('click',function(){
   videoFunction()
})


//Get the button
let mybutton = document.getElementById("action-button");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (
    document.body.scrollBottom > 20 ||
    document.documentElement.scrollTop > 20
  ) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}


