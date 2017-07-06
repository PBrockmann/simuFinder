<html>

<head>

<META NAME="author" CONTENT="Patrick Brockmann">
<META HTTP-EQUIV="Content-Type" CONTENT ="text/html;charset=ISO-8859-1">

<script src="lib/jquery.min.js"></script>

<style>
html {
  font-family: arial;
  font-size: 16px;
}
#loading {
  position: absolute;
  top: 40%;
  left: 50%;
}
#mesg {
  width: 120px;
  margin-top: 20px;
  text-align: center;
}
</style>

</head>

<body>

<div id="loading">
	<img src="loading.gif">
	<div id="mesg">Processing, please wait...</div>
</div>

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

?>

<script type="text/javascript">
$(document).ready(function() { 

$.ajax({ 
  type: "POST", 
  url: "execute.php",
  data: {'list': '<?php print($tmpfname1); ?>', 'html': '<?php print($tmpfname2); ?>'},
  dataType: "html",
  success: function(data){
	document.open("text/html", "replace");
	document.write(data);
	document.close();
  } 
}); 

});
</script>

</body>
</html>
