<?php
  $username = $_POST['nick'];
  $pass = $_POST['pass'];

  if ($pass == 'xyz')
  {
    header("Location: http://localhost/profile.php");
  }
  else
  {
    header("Location: http://localhost/index.php");
  }
 ?>
