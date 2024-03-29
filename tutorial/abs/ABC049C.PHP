<?php
  fscanf(STDIN,"%s",$s);
  $str = str_replace("dream","",str_replace("dreamer","",str_replace("erase","",str_replace("eraser","",$s))));
  if(strlen($str)==0) {
    echo 'YES';
  }else {
    echo 'NO';
  }
?>