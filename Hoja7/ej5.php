<?php
class ConversorMoneda
{
    public $factorConversion;
    public function convertirDolaresAEuros($dolares)
    {
        return $dolares * $this->factorConversion;
    }
    public function convertirEurosADolares($euros)
    {
        return number_format($euros / $this->factorConversion, 2);
    }
}

$conversor = new ConversorMoneda();
$conversor->factorConversion = 0.85;
$dolares = 100;
$euros = 55;
echo "$dolares dólares son " . $conversor->convertirDolaresAEuros($dolares) . " euros.\n";
echo "$euros euros son " . $conversor->convertirEurosADolares($euros) . " dólares.\n";
