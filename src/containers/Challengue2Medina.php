
<?php


$a = 0;
$b = 1;
    

for ( $i= 0; $i < 50; $i++) { 
    $c = $a + $b; 
    $a = $b;
    $b = $c; 
    echo $b;
}

?>