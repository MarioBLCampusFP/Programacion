<?php
$altura = readline("Altura: ");
// Filas
for ($i = 1; $i <= $altura; $i++) {
    // Espacios
    for ($j = $altura - $i; $j > 0; $j--) {
        echo " ";
    }
    // Números
    for ($k = 1; $k <= $i; $k++) {
        echo $k . " ";
    }
    // Salto de línea
    echo "\n";
}
