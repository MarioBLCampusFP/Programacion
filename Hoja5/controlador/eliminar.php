<?php
require_once "funciones.php";
require_once "mapeo_datos.php";

$id = $_POST["id"] ?? null;
$tipo = $_GET["tipo"] ?? null;

if ($tipo && $id) {
    $archivo = "../datos/{$tipoPlural[$tipo]}.csv";
    $datos = leerDatos($archivo);
    $idExiste = false;

    // Comprobar si el id es válido
    foreach ($datos as $index => $dato) {
        if ($index > 0 && $dato[0] == $id) {
            $idExiste = true;
            break;
        }
    }

    if ($idExiste) {
        $datosActualizados = array_filter($datos, function ($dato) use ($id) {
            return $dato[0] != $id;
        });
        escribirDatos($archivo, $datosActualizados);
        echo "<h1>" . ucfirst($tipo) . " eliminado con éxito</h1>";
    } else {
        echo "<h1>Error: " . ucfirst($tipo) . " no encontrado.</h1>";
    }
} else {
    echo "<h1>Error: Tipo o ID no especificado</h1>";
}
echo "<a href='../index.php?opcion={$tipoPlural[$tipo]}'>Volver al listado</a>";
