<?php
class Calculadora
{
    public function sumar($a, $b)
    {
        return $a + $b;
    }
    public function restar($a, $b)
    {
        return $a - $b;
    }
    public function multiplicar($a, $b)
    {
        return $a * $b;
    }
    public function dividir($a, $b)
    {
        if ($b == 0) {
            return "No se puede dividir por cero.";
        }
        return $a / $b;
    }
}

$calculadora = new Calculadora();
$a = readline("Primer número: ");
$b = readline("Segundo número: ");
echo "Suma: " . $calculadora->sumar($a, $b) . "\n";
echo "Resta: " . $calculadora->restar($a, $b) . "\n";
echo "Multiplicación: " . $calculadora->multiplicar($a, $b) . "\n";
echo "División: " . $calculadora->dividir($a, $b) . "\n";
