<?php
// Registro de errores
$archivo_log = "errores.log";
ini_set("log_errors", 1);
ini_set("error_log", $archivo_log);

function validarEmail($email)
{
    global $archivo_log;
    if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return "Válido";
    } else {
        echo "Error registrado en $archivo_log";
        error_log("El correo electrónico $email es inválido.");
    }
}

echo validarEmail("correo@ejemplo.com");
echo validarEmail("correo_invalido");
