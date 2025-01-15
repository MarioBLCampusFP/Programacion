<?php
class Empleado
{
    public $nombre;
    public $sueldo;
    public function mostrarDetalles()
    {
        echo "Nombre: $this->nombre\n";
        echo "Sueldo: $this->sueldo\n";
    }
}

class Gerente extends Empleado
{
    public $departamento;
    public function mostrarDetalles()
    {
        echo "Nombre: $this->nombre\n";
        echo "Sueldo: $this->sueldo\n";
        echo "Departamento: $this->departamento\n";
    }
}

$empleado = new Empleado();
$empleado->nombre = "Empleado A";
$empleado->sueldo = 1000;
$empleado->mostrarDetalles();

$gerente = new Gerente();
$gerente->nombre = "Gerente A";
$gerente->sueldo = 3000;
$gerente->departamento = "Departamento A";
$gerente->mostrarDetalles();
