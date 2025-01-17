<?php
class Empleado
{
    public $nombre;
    public $sueldo;
    public $aniosExperiencia;
    public function calcularBonus()
    {
        return floor($this->aniosExperiencia / 2) * ($this->sueldo * 0.05);
    }
    public function mostrarDetalles()
    {
        echo "Nombre: $this->nombre\n";
        echo "Sueldo: $this->sueldo\n";
        echo "Años de experiencia: $this->aniosExperiencia\n";
        echo "Bonus: " . $this->calcularBonus() . "\n";
    }
}

class Consultor extends Empleado
{
    public $horasPorProyecto;
    public function calcularBonus()
    {
        $bonus = parent::calcularBonus();
        if ($this->horasPorProyecto > 100) {
            $bonus += $this->sueldo * 0.1;
        }
        return $bonus;
    }
}

// Instanciar un Empleado
$empleado = new Empleado();
$empleado->nombre = "Juan Pérez";
$empleado->sueldo = 3000;
$empleado->aniosExperiencia = 6;

// Instanciar un Consultor
$consultor = new Consultor();
$consultor->nombre = "Ana Gómez";
$consultor->sueldo = 4000;
$consultor->aniosExperiencia = 5;
$consultor->horasPorProyecto = 120;

// Mostrar detalles y bonificaciones
echo "Detalles del Empleado:\n";
$empleado->mostrarDetalles();
echo "\n";

echo "Detalles del Consultor:\n";
$consultor->mostrarDetalles();
