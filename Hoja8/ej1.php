<?php
class CuentaBancaria
{
    public $titular;
    public $saldo;
    public $tipoDeCuenta;
    public function depositar($cantidad)
    {
        if ($cantidad > 0) {
            $this->saldo += $cantidad;
        } else {
            echo "La cantidad a depositar debe ser mayor a cero.\n";
        }
    }
    public function retirar($cantidad)
    {
        if ($cantidad > 0 && $cantidad <= $this->saldo) {
            $this->saldo -= $cantidad;
        } else {
            echo "No se puede retirar $cantidad. Saldo insuficiente o cantidad inválida.\n";
        }
    }
    public function mostrarInfo()
    {
        echo "Titular: $this->titular\n";
        echo "Tipo de cuenta: $this->tipoDeCuenta\n";
        echo "Saldo actual: $this->saldo\n";
    }
}

$cuenta = new CuentaBancaria();
$cuenta->titular = "Juan Pérez";
$cuenta->tipoDeCuenta = "Ahorros";
$cuenta->saldo = 1000;
$cuenta->mostrarInfo();
$cuenta->depositar(500);
$cuenta->retirar(200);
$cuenta->retirar(1500);
$cuenta->mostrarInfo();
