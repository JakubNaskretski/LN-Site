
// shows after click image
// // Get the button, and when the user clicks on it, execute myFunction
// document.getElementById("klikprodukt").onclick = function() {myFunction()};
//
// /* myFunction toggles between adding and removing the show class, which is used to hide and show the dropdown content */
// function myFunction() {
//   document.getElementById("productphoto").classList.toggle("show");
// }

// When the user scrolls down 50px from the top of the document, resize the header's font size
window.onscroll = function() {
  scrollFunction1();
  scrollFunction2();
}

function scrollFunction1() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    document.getElementById("center").style.fontSize = "30px";
  } else {
    document.getElementById("center").style.fontSize = "90px";
  }
}

function scrollFunction2() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    document.getElementById("imagebackground").setAttribute(
    "style", "width: 50%; height: 50%; opacity: 0.2");
  } else {
    document.getElementById("imagebackground").setAttribute(
    "style","display: block; height: 100%; width: 100%; margin-left: auto; margin-right: auto; opacity: 0.5;");
  }
}
