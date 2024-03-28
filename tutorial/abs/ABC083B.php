<?php
    fscanf(STDIN,"%d %d %d",$n,$a,$b);


    $sum = 0;
    for($j=1;$j<=$n;$j++){
        $nc = str_split($j);
        $count = 0;
        for($i=0;$i<count($nc);$i++){
            $count += $nc[$i];
        }
        if($count >= $a and $count <= $b){
            $sum += $j;
        }        
    }
    echo $sum . PHP_EOL;