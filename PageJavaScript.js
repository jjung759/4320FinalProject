var oldHeight = 14;
var isEnlarged = false;
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

