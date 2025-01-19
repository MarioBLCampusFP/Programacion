<?php
class CuentaBancaria
{
    private $titular;
    private $saldo;
    private $tipoCuenta;

    public function __construct($titular, $tipoCuenta)
    {
        $this->titular = $titular;
        $this->saldo = 0;
        $this->tipoCuenta = $tipoCuenta;
    }

    public function depositar($cantidad)
    {
        $this->saldo += $cantidad;
        echo "Se han añadido {$cantidad}€\n";
    }
    public function retirar($cantidad)
    {
        if ($this->verificarSaldoSuficiente($cantidad)) {
            $this->saldo -= $cantidad;
            echo "Se han retirado {$cantidad}€\n";
        } else {
            echo "Saldo insuficiente para retirar {$cantidad}€\n";
        }
    }
    private function verificarSaldoSuficiente($cantidad)
    {
        return $this->saldo >= $cantidad;
    }
    public function obtenerSaldo()
    {
        return $this->saldo;
    }
}

$miCuenta = new CuentaBancaria("Juan Pérez", "Ahorros");
$miCuenta->depositar(100);
$miCuenta->retirar(50);
$miCuenta->retirar(70);
echo "Saldo actual: " . $miCuenta->obtenerSaldo() . "€\n";
$miCuenta->depositar(200);
$miCuenta->retirar(100);
echo "Saldo final: " . $miCuenta->obtenerSaldo() . "€";
