<?php
// Pedir al usuario que ingrese una contraseña
$password = readline("Ingrese una contraseña: ");

// Definir la expresión regular para validar la contraseña
$regex = "/^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$/";

// Verificar si la contraseña cumple con el patrón definido
if (preg_match($regex, $password)) {
    echo "Acceso concedido.\n";
} else {
    echo "La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.\n";
}
