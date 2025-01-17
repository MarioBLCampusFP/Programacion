<?php
class Tarea
{
    public $nombre;
    public $descripcion;
    public $fechaLimite;
    public $estado;

    public function marcarComoCompletada()
    {
        $this->estado = "completada";
    }

    public function editarDescripcion($nuevaDescripcion)
    {
        $this->descripcion = $nuevaDescripcion;
    }

    public function mostrarTarea()
    {
        echo "Nombre: $this->nombre\n";
        echo "Descripcion: $this->descripcion\n";
        echo "Fecha límite: $this->fechaLimite\n";
        echo "Estado: $this->estado\n";
    }
}

// Crear una lista de tareas
$tareas = [];

// Agregar tareas a la lista
$tarea1 = new Tarea();
$tarea1->nombre = "Tarea 1";
$tarea1->descripcion = "Descripción de la tarea 1";
$tarea1->fechaLimite = "2025-10-01";
$tarea1->estado = "pendiente";
$tareas[] = $tarea1;

$tarea2 = new Tarea();
$tarea2->nombre = "Tarea 2";
$tarea2->descripcion = "Descripción de la tarea 2";
$tarea2->fechaLimite = "2025-10-05";
$tarea2->estado = "pendiente";
$tareas[] = $tarea2;

$tarea3 = new Tarea();
$tarea3->nombre = "Tarea 3";
$tarea3->descripcion = "Descripción de la tarea 3";
$tarea3->fechaLimite = "2025-10-10";
$tarea3->estado = "pendiente";
$tareas[] = $tarea3;

// Marcar la primera tarea como completada
$tareas[0]->marcarComoCompletada();

// Mostrar todas las tareas
echo "Lista de Tareas:\n";
foreach ($tareas as $tarea) {
    $tarea->mostrarTarea();
    echo "\n";
}
