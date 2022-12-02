<?php

$usuario=$_POST["usuario"];
$contraseña=$_POST["contraseña"];

$conexion = mysqli_connect("localhost","root","","login");

$insertar= "INSERT INTO admins VALUES (NULL,'$usuario', '$contraseña')";

$query = mysqli_query($conexion,$insertar);

if ($query){
    echo "<script language= 'JavaScript'>
                alert('Se ha registrado exitosamente');
                location.assign('../../index.php');
                </script>";
}else{
    echo "incorrecto";
}