<?php
class Producto
{
    public $nombre;
    public $precio;
    public function mostrarDetalles()
    {
        echo "Nombre: " . $this->nombre . "\n";
        echo "Precio: " . $this->precio . "€\n";
    }
}

class Electrodomestico extends Producto
{
    public $consumo;
    public function mostrarDetalles()
    {
        parent::mostrarDetalles();
        echo "Consumo: " . $this->consumo . " kWh\n";
    }
}

$producto = new Producto();
$producto->nombre = "Silla";
$producto->precio = 45;

echo "Detalles del Producto:\n";
$producto->mostrarDetalles();
echo "\n";

$electrodomestico = new Electrodomestico();
$electrodomestico->nombre = "Lavadora";
$electrodomestico->precio = 350;
$electrodomestico->consumo = 1.5;

echo "Detalles del Electrodoméstico:\n";
$electrodomestico->mostrarDetalles();
