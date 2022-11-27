<!DOCTYPE html>
<html lang = "es">    
<head>
    <meta charset = "UTF-8">
    <meta name = "viewport" content = "width = device-width, initial-scale = 1-0">
    <title>Inicio de Sesión</title>
    <link rel="stylesheet" href="css/master2.css">
</head>
<body>
    <div class="login-box">
      <img src="../img/logo.jpg" class="avatar" alt="Avatar Image">
      <h1>Registrate</h1>

      <form action="validar2.php" method = "post">
        <!-- USERNAME INPUT -->
        <label for="username">Usuario</label>
        <input type ="text" placeholder = "Ingrese su Usuario (Texto)" name = "usuario">
        <!-- PASSWORD INPUT -->
        <label for="password">Password</label>
        <input type ="text" placeholder = "Ingrese su Contraseña (Números)" name = "contraseña">
        <input type="submit" value = "Ingresar">
        <a href="../../index.php">Inicia sesión</a>
      </form>
    </div>
</body>
</html>