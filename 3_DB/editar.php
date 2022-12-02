<?php
$conexion = mysqli_connect("localhost","root","","login");
?>

<!DOCTYPE html>
<html lang = "es">    
<head>
    <meta charset = "UTF-8">
    <meta name = "viewport" content = "width = device-width, initial-scale = 1-0">
    <title>Pagina_Web</title>
    <link rel = "stylesheet" href = "../2_Indicee/css/normalize.css">
    <link rel = "stylesheet" href = "css/estilo.css">
</head>
<body>
<header class = "hero" id = "Inicio">
        <div class="container">
            <nav class = "nav">
                <a href="../2_Indicee/aindice.html" class = "nav__items nav__items--cta">Inicio</a>
                <a href="../2_Indicee/aindice.html/#Indice" class = "nav__items">Indice</a>
                <a href="../2_Indicee/aindice.html/#Funcion" class = "nav__items">¿Cómo Funciona?</a>
            </nav>
        </div>
        <div class = "hero__wave" style="overflow: hidden;" ><svg viewBox="0 0 500 150" preserveAspectRatio="none" style="height: 100%; width: 100%;"><path d="M0.00,49.98 C149.99,150.00 349.20,-49.98 500.00,49.98 L500.00,150.00 L0.00,150.00 Z" style="stroke: none; fill: #fff;"></path></svg></div>
</header>
    
    <?php
        if(isset($_POST['enviar'])){
            $id=$_POST['id'];
            $usuario=$_POST['usuario'];
            $contraseña=$_POST['contraseña'];

            //Actualizar

            $sql = "UPDATE admins SET usuario = '".$usuario."', contraseña = '".$contraseña."' WHERE id = '".$id."'";
            $resultado=mysqli_query($conexion,$sql);

            if($resultado){
                echo "<script language= 'JavaScript'>
                        alert('Los Datos se han Actualizado');
                        location.assign('tablas.php');
                        </script>";
            }else{
                echo "<script language= 'JavaScript'>
                        alert('Los Datos NO se han Actualizado');
                        location.assign('tablas.php');
                        </script>";
            }
            mysqli_close($conexion);

        }else{
            $id=$_GET['id'];
            $sql="SELECT * FROM admins where id = '".$id."'";
            $resultado = mysqli_query($conexion,$sql);
            $fila= mysqli_fetch_assoc($resultado);
            $usuario = $fila['usuario'];
            $contraseña = $fila['contraseña'];

            mysqli_close($conexion);
    ?>

    <h1>Editar Datos de la Tabla</h1>
    <form action = "<?=$_SERVER['PHP_SELF']?>" method="post">
        <label>Usuario: </label>
        <input type = "text" name = "usuario" value ="<?php echo $usuario; ?>"> <br>
        
        <label>Contraseña: </label>
        <input type = "text" name = "contraseña" value ="<?php echo $contraseña; ?>"> <br>

        <input type="hidden" name = "id" value =  "<?php echo $id; ?>">

        <input type = "submit" name = "enviar" value ="Actualizar">
        <a href = "tablas.php">Regresar</a>
    
    </form>
    <?php
    }
    ?>
</body>
</html>