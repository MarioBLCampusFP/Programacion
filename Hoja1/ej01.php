<?php
$numero1 = readline("Dame el primer número: ");
$numero2 = readline("Dame el segundo número: ");
$operacion = readline("Elije la operación (suma, resta, multiplicación, división): ");
if ($operacion == "suma") {
    echo "La suma de " . $numero1 . " y " . $numero2 . " es: " . $numero1 + $numero2;
} elseif ($operacion == "resta") {
    echo "La resta de " . $numero1 . " y " . $numero2 . " es: " . $numero1 - $numero2;
} elseif ($operacion == "multiplicación") {
    echo "La multiplicación de " . $numero1 . " y " . $numero2 . " es: " . $numero1 * $numero2;
} elseif ($operacion == "división") {
    echo "La resta de " . $numero1 . " y " . $numero2 . " es: " . $numero1 / $numero2;
} else {
    echo "Operación inválida.";
}
