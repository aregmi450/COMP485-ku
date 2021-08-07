<?php 
include('conn.php'); //database connection
if($_SERVER['REQUEST_METHOD'] == "POST")
{
    //username and password sent from form
    $username = mysqli_real_escape_string($conn, $_POST['user']);
    $password = mysqli_real_escape_string($conn, $_POST['pass']);
    $password = md5($password); //password encrypted using md5
    $sql = "INSERT INTO userpass(user, pass) values ('$username', '$password')";

    $result = mysqli_query($conn, $sql);
    echo "Created Succesfully";
}
?>

<!doctype html>
<html>
    <head>
        <title> New User Login </title>  
    </head>
    <body>
        <h1>New User Login</h1>
        <form action="<?php $_SERVER['PHP_SELF'];?>"method="post">
        <label>Username</label>
        <input type="text" name="user"><br><br/>
        <label>Password</label>
        <input type="password" name="pass"><br><br/>
        <input type="submit" name="submit" value="Create"><br><br/>
        <p><a href="login.php">Log In</a></p>
        </form>
    </body>
</html>
