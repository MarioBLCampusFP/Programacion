<?php
// Función para generar un array de números aleatorios
function generarNumeros($n)
{
    $array = [];
    for ($i = 0; $i < $n; $i++) {
        array_push($array, rand(1, 100));
    }
    return $array;
}

$numerosAleatorios = generarNumeros(10);
$longitud = count($numerosAleatorios);

echo "Números aleatorios: " . json_encode($numerosAleatorios) . "\n";

// Bubble Sort
for ($i = 0; $i < $longitud - 1; $i++) {
    for ($j = 0; $j < $longitud - $i - 1; $j++) {
        // Comparar elementos adyacentes
        if ($numerosAleatorios[$j + 1] < $numerosAleatorios[$j]) {
            // Intercambiar posiciones
            $tmp = $numerosAleatorios[$j];
            $numerosAleatorios[$j] = $numerosAleatorios[$j + 1];
            $numerosAleatorios[$j + 1] = $tmp;
        }
    }
}

echo "Array ordenado: " . json_encode($numerosAleatorios) . "\n";
