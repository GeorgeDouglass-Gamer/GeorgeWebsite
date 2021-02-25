<?php
echo"poop";
//Example array.
$array = array('Ireland', 'England', 'Wales', 'Northern Ireland', 'Scotland');
echo"poop";
//Encode the array into a JSON string.
$encodedString = json_encode($array);
echo"poop";
//Save the JSON string to a text file.
file_put_contents('json_array.txt', $encodedString);
echo"poop";
//Retrieve the data from our text file.
$fileContents = file_get_contents('json_array.txt');
echo"poop";
//Convert the JSON string back into an array.
$decoded = json_decode($fileContents, true);
echo"poop";
//The end result.
var_dump($decoded);

echo"poop";
?>
