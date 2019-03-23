// When the user scrolls down 50px from the top of the document, resize the header's font size
window.onscroll = function() {
  scrollFunction1();
  scrollFunction2();
}

// calling function when click display image (for now alert)
displayImageOnClick();

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

function displayImageOnClick() {
    document.getElementById("btn1").addEventListener("click", function() {
    alert("Hello World!");
    }
  );
}
