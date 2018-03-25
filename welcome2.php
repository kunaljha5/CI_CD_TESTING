<html>
<body>

Welcome  <?php
    $item1=$_POST["name"];
	echo "$item1";
    $item2=$_POST["Height"];
    $item3=$_POST["Weight"];
    $item4=$_POST["Msisdn"];
    exec("python BMI.py --n '$item1' --h '$item2' --w '$item3' --m '$item4'", $xout);
	    echo "<pre>";
    print_r($xout);
    echo "</pre>";

?>
<br>

</body>
</html> 
