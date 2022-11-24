<?php

$usuario=$_POST["usuario"];
$contraseña=$_POST["contraseña"];

$conexion = mysqli_connect("localhost","root","","login");

$insertar= "INSERT INTO usuarios VALUES (NULL,'$usuario', '$contraseña')";

$query = mysqli_query($conexion,$insertar);

if ($query){
    header("location: ../../index.php");
}else{
    echo "incorrecto";
}