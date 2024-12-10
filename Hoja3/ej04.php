<?php
function tablaMultiplicar($numero)
{
    if (is_int($numero) && $numero > 0) {
        for ($i = 0; $i <= 10; $i++) {
            echo "$numero x $i = " . ($numero * $i) . "\n";
        }
    } else {
        throw new Exception("El número debe ser un entero positivo.");
    }
}

try {
    echo tablaMultiplicar(5);
    echo tablaMultiplicar(-2);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
