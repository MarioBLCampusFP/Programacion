<?php
function calculadora($a, $b, $operador)
{
    if ($operador == "+") {
        return $a + $b;
    } elseif ($operador == "-") {
        return $a - $b;
    } elseif ($operador == "*") {
        return $a * $b;
    } elseif ($operador == "/") {
        if ($b == 0) {
            throw new Exception("No se puede dividir entre cero.");
        }
        return $a / $b;
    }
}

try {
    echo calculadora(10, 2, "/");
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
