<?php
class Usuario
{
    private $nombre;
    private $email;

    public function __construct($nombre, $email)
    {
        $this->nombre = $nombre;
        $this->email = $email;
    }

    public function mostrarInfo()
    {
        echo "Nombre: $this->nombre\n";
        echo "Email: $this->email\n";
    }
}

class Administrador extends Usuario
{
    private $nivelAcceso;

    public function __construct($nombre, $email, $nivelAcceso)
    {
        parent::__construct($nombre, $email);
        $this->nivelAcceso = $nivelAcceso;
    }

    public function mostrarInfo()
    {
        parent::mostrarInfo();
        echo "Nivel de acceso: $this->nivelAcceso\n";
    }
}

$usuario = new Usuario("Juan Pérez", "juan.perez@ejemplo.com");
$administrador = new Administrador("Ana Gómez", "ana.gomez@ejemplo.com", "Alto");

// Mostrar información del usuario
echo "Información del Usuario:\n";
$usuario->mostrarInfo();
echo "\n";

// Mostrar información del administrador
echo "Información del Administrador:\n";
$administrador->mostrarInfo();
