<?php
$frase = readline("Ingrese una frase: ");
$contador = 0;
$longitud = strlen($frase);

if ($longitud) {
    // Recorrer frase
    for ($i = 0; $i < $longitud; $i++) {
        // Contar palabra
        if ($frase[$i] == " ") {
            $contador++;
        }
    }
    // Contar la última palabra
    $contador++;
}

echo "Total de palabras: {$contador}\n";
