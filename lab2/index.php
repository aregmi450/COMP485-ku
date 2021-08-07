<?php

?>

<!DOCTYPE html>
<html>

<head>
    <title>Login Registration with md5() encryption</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>

</head>
<body>
    <br> </br>
    <div class="container" style="width: 500px;">
    <h3 text-align="center">Registration</h3>
    <br>
    <form method="post">
        <label>Enter Username</label>
        <input type="text" name="username" class="form-control" />
        <br/>
        <label>Enter Password</label>
        <input type="password" name="password" class="form-control" />
        <br>
        <input type="submit" name="register" value="Register" />
        <br>
        <p text-align="center"><a href="index.php?action=login">Login</a></p>
    </form>
    </div>
</body>

</html>