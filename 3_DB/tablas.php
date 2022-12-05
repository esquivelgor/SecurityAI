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

<br>
    <h1>Administradores</h1>
    <table border="1" class="body__table">
        <thead>
            <td>id</td>
            <td>usuario</td>
            <td>contraseña</td>
            <td> </td>
        </thead>

        <?php
        $sql = "SELECT * from admins";
        $result = mysqli_query($conexion,$sql );

        while($mostrar=mysqli_fetch_array($result)){
        ?>
        
        <tr>
            <td><?php echo $mostrar['id']?></td>
            <td><?php echo $mostrar['usuario']?></td>
            <td><?php echo $mostrar['contraseña']?></td>
            <td><?php echo "<a href = 'editar.php?id=".$mostrar['id']."'>Editar</a>";?></td>
        </tr> 
    
    <?php
    }
    ?>
    
    </table>


    <h1>Acceso de usuario</h1>
    <table border="1" class="body__table">
        <thead>
            <td>ID_Registro</td>
            <td>Acceso</td>
            <td>ID_Usuario</td>
            <td> </td>
        </thead>

        <?php
        $sql = "SELECT * from accesos";
        $result = mysqli_query($conexion,$sql );

        while($mostrar=mysqli_fetch_array($result)){
        ?>
        
        <tr>
            <td><?php echo $mostrar['ID_Registro']?></td>
            <td><?php echo $mostrar['Acceso']?></td>
            <td><?php echo $mostrar['ID_Usuario']?></td>
            <td><?php echo "<a href = 'editar.php?id=".$mostrar['id']."'>Editar</a>";?></td>
        </tr> 
    
    <?php
    }
    ?>

    </table>

    <h1>Usuarios</h1>
    <table border="1" class="body__table">
        <thead>
            <td>ID_Usuario</td>
            <td>Nombre</td>
            <td>Edad</td>
            <td>Tipo_Usuario</td>
            <td></td>
        </thead>

        <?php
        $sql = "SELECT * from usuarios";
        $result = mysqli_query($conexion,$sql );

        while($mostrar=mysqli_fetch_array($result)){
        ?>
        
        <tr>
            <td><?php echo $mostrar['ID_Usuario']?></td>
            <td><?php echo $mostrar['Nombre']?></td>
            <td><?php echo $mostrar['Edad']?></td>
            <td><?php echo $mostrar['Tipo_Usuario']?></td>
            <td><?php echo "<a href = 'editar.php?id=".$mostrar['id']."'>Editar</a>";?></td>
        </tr> 
    
    <?php
    }
    ?>

    </table>

    <h1>Imagenes</h1>
    <table border="1" class="body__table">
        <thead>
            <td>ID_Imagen</td>
            <td>Imagen</td>
            <td>ID_Usuario</td>
            <td></td>
        </thead>

        <?php
        $sql = "SELECT * from memorybank";
        $result = mysqli_query($conexion,$sql );

        while($mostrar=mysqli_fetch_array($result)){
        ?>
        
        <tr>
            <td><?php echo $mostrar['ID_Imagen']?></td>
            <td><?php echo $mostrar['Imagen']?></td>
            <td><?php echo $mostrar['ID_Usuario']?></td>
            <td><?php echo "<a href = 'editar.php?id=".$mostrar['id']."'>Editar</a>";?></td>
        </tr> 
    
    <?php
    }
    ?>

    </table>

    <?php
$conexion = mysqli_connect("localhost","root","","login");
?>

</body>
</html>