<?php
class Persona
{
    public $nombre;
    public $edad;
    public $genero;
    public function presentar()
    {
        echo "Nombre: $this->nombre\n";
        echo "Edad: $this->edad\n";
        echo "Genero: $this->genero\n";
    }
}

$persona = new Persona();
$persona->nombre = "Juan";
$persona->edad = 30;
$persona->genero = "Masculino";
$persona->presentar();
