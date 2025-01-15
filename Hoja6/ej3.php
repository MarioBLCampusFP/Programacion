<?php
class Vehiculo
{
    public $marca;
    public function encender()
    {
        echo "El coche está arrancando...\n";
    }
}

class Coche extends Vehiculo
{
    public $modelo;
    public function mostrarInfo()
    {
        echo "Coche: $this->marca $this->modelo\n";
    }
}

$miCoche = new Coche();
$miCoche->marca = "Marca A";
$miCoche->modelo = "Modelo B";
$miCoche->encender();
$miCoche->mostrarInfo();
