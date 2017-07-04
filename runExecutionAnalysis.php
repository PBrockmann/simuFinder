
<?php

//==================================================
$tmpfname = tempnam("tmp", "list_");
unlink($tmpfname);

$tmpfname1 = "tmp/" . basename($tmpfname) . ".txt";
$tmpfname2 = "tmp/" . basename($tmpfname) . ".html";

//==================================================
$handle = fopen($tmpfname1, "w");

// http POST simul1, simul2.... to this page
$i=1;
while (isset($_POST['simul'.$i])) {
	//print($_POST['simul'.$i]);
	fwrite($handle, $_POST['simul'.$i] . "\n");
        $i++;
}
fclose($handle);

exec("./runcard_01.py " . $tmpfname1 . " " . $tmpfname2, $return_code);
//exec("./runcard_01.py list1.txt " . $tmpfname2, $return_code);

$result = file_get_contents($tmpfname2);
echo $result;

//==================================================
unlink($tmpfname1);
unlink($tmpfname2);

?>
