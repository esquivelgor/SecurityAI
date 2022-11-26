<?php
$usuario=$_POST["usuario"];
$contraseña=$_POST["contraseña"];
session_start();
$_SESSION["usuario"]= $usuario;

$conexion = mysqli_connect("localhost","root","","login");

$consulta="SELECT*FROM admins where usuario = '$usuario' and contraseña = '$contraseña'";

$resultado = mysqli_query($conexion,$consulta);

$filas=mysqli_num_rows($resultado);

if($filas){
    header("location: ../2_Indicee/aindice.html");
}else{
    ?>
    <?php
    header ("location: ../index.php");
}

mysqli_free_result($resultado);
mysqli_close($conexion);