<!DOCTYPE html>

<html>
  <head>
    <meta charset="utf-8" />
    <title>Raspberry Pi GPIO</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  
  <body>
    <div class="slidecontainer">
      <p id="demo"></p>
      <input type="range" min="0" max="255" value="50" class="slider" id="tiltSlider">
    </div>
    <!-- On/Off button's picture -->
    <?php
       $pin = 18;
       $val_array = array(0);
       // use the pin's mode to output and read it. use BSM 
       system("gpio -g mode ".$pin." output");
       exec ("gpio -g read ".$pin, $val_array[0], $return );

//       echo (print_r(array_values($array))." ");
//       echo ("value: ".$val_array[0][0]." ");
       //if off
       if ($val_array[0][0] == 0) {
         echo ("<img id='button' src='data/img/red/red.jpg' onclick='change_pin (".$pin.");'/>");
       }
       //if on
       else if ($val_array[0][0] == 1) {
          echo ("<img id='button' src='data/img/green/green.jpg'
          onclick='change_pin (".$pin.");'/>");
       }
       else {
          echo ("Something went wrong!");
       }
    ?>

    <!-- javascript -->
    <script src="script.js"></script>
    <script type="text/javascript" src="{{ url_for('static', filename='sliderscript.js') }}"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
  </body>
</html>
