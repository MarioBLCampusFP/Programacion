<?php
class Circulo
{
    public $radio;
    public function calcularArea()
    {
        return pi() * pow($this->radio, 2);
    }
}

$miCirculo = new Circulo();
$miCirculo->radio = 5;
echo $miCirculo->calcularArea();
