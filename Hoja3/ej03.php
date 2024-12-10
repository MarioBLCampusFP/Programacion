<?php
// Manejador personalizado de errores
function manejadorErrores($nivel, $mensaje)
{
    echo "Error: $mensaje\n";
}

// Establecer el manejador de errores
set_error_handler("manejadorErrores");

function buscarElemento($array, $valor)
{
    $posicion = array_search($valor, $array);
    if ($posicion) {
        return $posicion . "\n";
    } else {
        // Generar un error
        trigger_error("El elemento no se encuentra en el array.", E_USER_ERROR);
    }
}

$array = ["manzana", "naranja", "pera"];
echo buscarElemento($array, "pera");
echo buscarElemento($array, "plátano");
