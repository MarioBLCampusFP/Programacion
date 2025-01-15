<?php
require_once "funciones.php";
require_once "mapeo_datos.php";

$id = $_POST["id"] ?? null;
$tipo = $_GET["tipo"] ?? null;

if ($tipo && $id) {
    $archivo = "../datos/{$tipoPlural[$tipo]}.csv";
    $datos = leerDatos($archivo);
    $datoActualizado = null;
    $indexFila = null;

    // Buscar el dato a actualizar
    foreach ($datos as $index => $dato) {
        if ($index > 0 && $dato[0] == $id) {
            $datoActualizado = $dato;
            $indexFila = $index; // Index de la fila a actualizar
            break;
        }
    }

    if ($datoActualizado !== null) {
        // Actualizar los campos con los nuevos valores
        foreach ($camposEntrada[$tipo] as $index => $name) {
            $datoActualizado[$index] = $_POST[$name];
        }

        // Reemplazar el dato actualizado en el array de datos
        $datos[$indexFila] = $datoActualizado;

        // Escribir los datos actualizados de nuevo en el archivo CSV
        $archivoEscritura = fopen($archivo, 'w');
        foreach ($datos as $linea) {
            fputcsv($archivoEscritura, $linea);
        }
        fclose($archivoEscritura);

        // Mensaje de éxito
        echo "<h1>Datos actualizados correctamente.</h1>";
        echo "<a href='../index.php?opcion={$tipoPlural[$tipo]}'>Volver al listado</a>";
    } else {
        echo "<h1>Error: " . ucfirst($tipo) . " no encontrado.</h1>";
    }
} else {
    echo "<h1>Error: Tipo o ID no especificado</h1>";
}
