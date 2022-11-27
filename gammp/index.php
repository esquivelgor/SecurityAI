<!DOCTYPE html>
<html lang = "es">    
<head>
    <meta charset = "UTF-8">
    <meta name = "viewport" content = "width = device-width, initial-scale = 1-0">
    <title>Inicio de Sesión</title>
    <link rel="stylesheet" href="1_login/css/master.css">
</head>
<body>
    <div class="login-box">
      <img src="1_login/img/logo.jpg" class="avatar" alt="Avatar Image">
      <h1>GAAMP CORPORATION</h1>

      <form action="1_login/validar.php" method = "post">
        <!-- USERNAME INPUT -->
        <label for="username">Usuario</label>
        <input type ="text" placeholder = "Ingrese su Usuario" name = "usuario">
        <!-- PASSWORD INPUT -->
        <label for="password">Password</label>
        <input type ="password" placeholder = "Ingrese su Contraseña" name = "contraseña">
        <input type="submit" value = "Ingresar">
        <a href="1_login/register/Z_Register.php">Don't have An account?</a>
      </form>
    </div>
</body>
</html>