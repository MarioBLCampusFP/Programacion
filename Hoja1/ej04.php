<?php
$numeroAleatorio = rand(1, 100);
do {
    $numeroUsuario = readline("Dame un número: ");
    if ($numeroUsuario < $numeroAleatorio) {
        echo "Es un número mayor.\n";
    } elseif ($numeroUsuario > $numeroAleatorio) {
        echo "Es un número menor.\n";
    } else {
        echo "Has acertado!";
    }
} while ($numeroAleatorio != $numeroUsuario);
