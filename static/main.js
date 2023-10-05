// document.addEventListener("DOMContentLoaded", function () {
  var y = 3;
  var toggleDivActive = 1;

  // For navigation
  function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
  }

  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }

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
  }

  function toggleDivs() {
    if (toggleDivActive) {
      var waitingdiv = document.getElementById("waitingdiv");
      var solutionDiv = document.getElementById("solutionDiv");
      var eqnField = document.getElementById("eqnField");
      eqnField.setAttribute.autofocus=true

      if (waitingdiv.style.display !== "none") {
        waitingdiv.style.display = "none";
        solutionDiv.style.display = "block";

      }
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
