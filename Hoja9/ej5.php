<?php
class Empleado
{
    private $nombre;
    private $sueldo;
    private $puesto;

    public function __construct($nombre, $sueldo, $puesto)
    {
        $this->nombre = $nombre;
        $this->sueldo = $sueldo;
        $this->puesto = $puesto;
    }

    public function setSueldo($nuevoSueldo)
    {
        $this->sueldo = $nuevoSueldo;
    }

    public function getSueldo()
    {
        return $this->sueldo;
    }

    public function getNombre()
    {
        return $this->nombre;
    }

    public function getPuesto()
    {
        return $this->puesto;
    }
}

class Manager extends Empleado
{
    private $departamento;

    public function __construct($nombre, $sueldo, $puesto, $departamento)
    {
        parent::__construct($nombre, $sueldo, $puesto);
        $this->departamento = $departamento;
    }

    public function revisarEmpleado(Empleado $empleado)
    {
        echo $empleado->getNombre() . ", " . $empleado->getPuesto() . "\n";
    }

    public function getDepartamento()
    {
        return $this->departamento;
    }

    public function mostrarDetalles()
    {
        echo "Gerente: " . $this->getNombre() . "\n";
        echo "Sueldo: " . $this->getSueldo() . "\n";
        echo "Puesto: " . $this->getPuesto() . "\n";
        echo "Departamento: " . $this->getDepartamento() . "\n";
    }
}

// Prueba de las clases
$empleado1 = new Empleado("Juan Pérez", 3000, "Desarrollador");
$empleado2 = new Empleado("Ana Gómez", 3500, "Diseñadora");

$manager = new Manager("Carlos López", 5000, "Gerente", "Tecnología");

// Mostrar detalles del empleado antes de cambiar el sueldo
echo "Sueldo de " . $empleado1->getNombre() . ": " . $empleado1->getSueldo() . "\n";

// Cambiar el sueldo del empleado
$empleado1->setSueldo(3200);
echo "Nuevo sueldo de " . $empleado1->getNombre() . ": " . $empleado1->getSueldo() . "\n";
echo "\n";

// Revisar empleados
echo "Empleados:\n";
$manager->revisarEmpleado($empleado1);
$manager->revisarEmpleado($empleado2);
echo "\n";

// Detalles del manager
$manager->mostrarDetalles();
