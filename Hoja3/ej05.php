<?php
// Registro de errores
$archivo_log = "errores.log";
ini_set("log_errors", 1);
ini_set("error_log", $archivo_log);

function convertirTemperatura($valor, $unidad)
{
    global $archivo_log;
    if ($unidad == "C") {
        return ($valor - 32) * 5 / 9;
    } elseif ($unidad == "F") {
        return ($valor * 9 / 5) + 32;
    } else {
        echo "Error registrado en $archivo_log";
        error_log("Unidad de conversión inválida.");
    }
}

echo convertirTemperatura(100, "C") . "\n";
echo convertirTemperatura(0, "F") . "\n";
echo convertirTemperatura(25, "X") . "\n";
