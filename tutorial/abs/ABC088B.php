<?php
    fscanf(STDIN,"%d",$n);
    $a = explode(" ",fgets(STDIN));
    rsort($a);
    
    $value_a = 0;
    $value_b = 0;
    for($i=0;$i<$n;$i++){
        if($i%2 == 0){
            $value_a += $a[$i];
        }
        else{
            $value_b += $a[$i];
        }
    }
    echo $value_a - $value_b . PHP_EOL;