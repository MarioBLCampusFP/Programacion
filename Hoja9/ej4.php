<?php
class Vehiculo
{
    protected $marca;
    protected $modelo;

    public function __construct($marca, $modelo)
    {
        $this->marca = $marca;
        $this->modelo = $modelo;
    }

    public function encender()
    {
        echo "El vehículo está encendido.\n";
    }
}

class Coche extends Vehiculo
{
    private $combustible;

    public function __construct($marca, $modelo, $combustible)
    {
        parent::__construct($marca, $modelo);
        $this->combustible = $combustible;
    }

    public function mostrarDetalles()
    {
        echo "Marca: $this->marca\n";
        echo "Modelo: $this->modelo\n";
        echo "Combustible: $this->combustible\n";
    }
}

$coche = new Coche("Toyota", "Corolla", "Gasolina");
$coche->encender();
$coche->mostrarDetalles();
