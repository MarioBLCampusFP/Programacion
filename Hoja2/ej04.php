<?php
$nombres = array("Juan", "María", "Pedro", "Ana", "Luis");
$apellidos = array("Pérez", "González", "López", "Martínez", "Sánchez");

// Generar números aleatorios
$indexNombre = rand(0, count($nombres) - 1);
$indexApellido = rand(0, count($apellidos) - 1);

// Concatenar el nombre y apellido
echo $nombres[$indexNombre] . " " . $apellidos[$indexApellido] . "\n";
