var slider = document.getElementById("tiltSlider");
var output = document.getElementById("demo");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    output.innerHTML = this.value;
    var request = new XMLHttpRequest();
    request.open("POST", "/phptest/", true);
    request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
    request.send('sliderValue='.concat(this.value));
}

