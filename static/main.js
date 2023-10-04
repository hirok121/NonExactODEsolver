var y = 3;
var x = 5;



function showEnterXY() {
  // x = 6;

  var button2id = document.getElementById("button2id");
  var resetFormit = document.getElementById("resetForm");

  var newMarginLeft = "-140px";
  var newMarginLeft2 = "240px";
  var newMarginLeft4 = "179px";

}









// ----------------------------------------------------------

function handleButtonClick(event) {
  event.preventDefault();
  f1();
}

function f1() {
  if (y === 2) {
    document.getElementById("xy").style.visibility = "hidden";
    document.getElementById("cnd").style.backgroundColor = "#d9c8f0";
    clearInput();
    y = 3;
  } else {
    document.getElementById("xy").style.visibility = "visible";
    document.getElementById("cnd").style.backgroundColor = "#b68deb";
    clearInput();
    y = 2;
  }
}

function clearInput() {
  document.getElementById("x").value = "";
  document.getElementById("y").value = "";
}

function f2() {
  y = 2;
}

//==========================================================

function solveAnother() {
  document.getElementById("solveforms").reset();

  document.getElementById("xyFormid").style.display = "none";

}

function toggleDivs() {
  var waitingdiv = document.getElementById("waitingdiv");
  var solutionDiv = document.getElementById("solutionDiv");

  if (waitingdiv.style.display !== "none") {
    waitingdiv.style.display = "none";
    solutionDiv.style.display = "block";
  }
}

function xyFormShow() {
  document.getElementById("xyFormid").style.display = "block";
  var div4 = document.getElementById("div4");
  var div5 = document.getElementById("div5");

  if (div5.style.display !== "none" && x == 6) {
    div5.style.display = "none";
    div4.style.display = "block";
  }
}

function backtostart() {
  var waitingdiv = document.getElementById("waitingdiv");
  var solutionDiv = document.getElementById("solutionDiv");

  if (solutionDiv.style.display !== "none") {
    waitingdiv.style.display = "block";
    solutionDiv.style.display = "none";
  }
}

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

function checkXAndToggle(button) {
  if (x === 5) {
    button.disabled = true;
    button.style.cursor = "not-allowed";
  } else {
    button.disabled = false;
    button.style.cursor = "pointer";
  }
}