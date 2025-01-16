<?php
class Rectangulo
{
    public $base;
    public $altura;
    public function calcularArea()
    {
        return $this->base * $this->altura;
    }
}

$rectangulo = new Rectangulo();
$rectangulo->base = 10;
$rectangulo->altura = 5;
echo $rectangulo->calcularArea();
