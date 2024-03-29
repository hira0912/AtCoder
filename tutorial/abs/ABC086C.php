<?php
    fscanf(STDIN,"%d",$n);
    $t_p = 0;
    $x_p = 0;
    $y_p = 0;
    $result = "Yes";
    for($i=0;$i<$n;$i++){
        fscanf(STDIN,"%d %d %d",$t,$x,$y);
        if(abs($t-$t_p) < abs($x-$x_p)+abs($y-$y_p) || abs($t-$t_p)%2 != (abs($x-$x_p)+abs($y-$y_p))%2) {
            $result = "No";
            break;
        }
        $t_p = $t;
        $x_p = $x;
        $y_p = $y;
    }
    echo $result;