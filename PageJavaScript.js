var oldHeight = 20;
var isEnlarged = false;
var checkList = document.getElementById('sourcelist');
var items = document.getElementById('items');
function enlarge() {
    if (!isEnlarged) {
        var toEnlarge = document.getElementById("headertop");
        var height = toEnlarge.offsetHeight;
        var newHeight = height + 200;
        toEnlarge.style.height = newHeight + 'px';

        // display placeholder material
        displayMaterial();

    } else {
        var toEnlarge = document.getElementById("headertop");
        toEnlarge.style.height = oldHeight + '%';

        // hide placeholder material
        hideMaterial();

    }
    isEnlarged = !isEnlarged;
}

function toggleSelected(number) {
    var chk = document.getElementById("check"+number);
    if (chk.checked == true && isEnlarged) {
        // If just checked true
        document.getElementById("text"+number).style.display = "block";

    } else {
        // if just checked false
        document.getElementById("text"+number).style.display = "none";
    }
}

function displayMaterial() {
    var i;
    for (i = 1; i <= 10; i++) {
        var chk = document.getElementById("check"+i);
        var chkText = document.getElementById("text"+i);
        if (chk.checked == true) chkText.style.display = "block";
        else chkText.style.display = "none";
    }
}

function hideMaterial() {
    var i;
    for (i = 1; i <= 10; i++) {
        document.getElementById("text"+i).style.display = "none";
    }
}

checkList.getElementsByClassName('anchor')[0].onclick = function (evt) {
    if (items.classList.contains('visible')){
        items.classList.remove('visible');
        items.style.display = "none";
    }

    else {
        items.classList.add('visible');
        items.style.display = "block";
    }
}

items.onblur = function(evt) {
    items.classList.remove('visible');
}

// Testing function and boolean
var toggle = false;
function toggleNews() {
    for (i = 1; i <= 10; i++) {
        var text = document.getElementById("text"+i);
        if (!toggle) text.style.display = "block";
        else if (toggle) text.style.display = "none";
    }
    if (!toggle) document.getElementById("login-message-fav").style.display = "none";
    else if (toggle) document.getElementById("login-message-fav").style.display = "block";
    toggle = !toggle;
}

var password = document.getElementById("newPassword");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");

// When the user clicks on the password field, show the newPasswordRequirements box
newPassword.onfocus = function() {
  document.getElementById("newPasswordRequirements").style.display = "block";
}

// When the user clicks outside of the password field, hide the newPasswordRequirements box
newPassword.onblur = function() {
  document.getElementById("newPasswordRequirements").style.display = "none";
}

// When the user starts to type something inside the password field
newPassword.onkeyup = function() {
  // Validate lowercase letters
  var lowerCaseLetters = /[a-z]/g;
  if(newPassword.value.match(lowerCaseLetters)) {
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
}

  // Validate capital letters
  var upperCaseLetters = /[A-Z]/g;
  if(newPassword.value.match(upperCaseLetters)) {
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  // Validate numbers
  var numbers = /[0-9]/g;
  if(newPassword.value.match(numbers)) {
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }

  // Validate length
  if(newPassword.value.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }
}
