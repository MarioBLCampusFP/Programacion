<?php
$numero = readline("Dame un número: ");
$esPrimo = true;
for ($i = 2; $i < $numero / 2; $i++) {
    if ($numero % $i == 0) {
        $esPrimo = false;
        break;
    }
}

if ($esPrimo) {
    echo "Es primo.";
} else {
    echo "No es primo.";
}
