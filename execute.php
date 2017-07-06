
<?php

$tmpfname1 = $_POST['list'];
$tmpfname2 = $_POST['html'];

//==================================================
exec("./runcard_01.py " . $tmpfname1 . " " . $tmpfname2, $return_code);
//exec("./runcard_01.py list1.txt " . $tmpfname2, $return_code);

$result = file_get_contents($tmpfname2);
print($result);

//==================================================
unlink($tmpfname1);
unlink($tmpfname2);

?>
