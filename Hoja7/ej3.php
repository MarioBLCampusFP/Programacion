<?php
class Animal
{
    public $especie;
    public function emitirSonido()
    {
        if (get_class($this) === "Perro") {
            echo "Guau!\n";
        } else {
            echo "...\n";
        }
    }
}

class Perro extends Animal
{
    public $raza;
}

$miPerro = new Perro();
$miPerro->especie = "Canino";
$miPerro->raza = "Labrador";

echo "Especie: " . $miPerro->especie . "\n";
echo "Raza: " . $miPerro->raza . "\n";

$miPerro->emitirSonido();
