<?php
function leerDatos($archivo)
{
    $datos = [];
    if (($handle = fopen($archivo, "r")) !== false) {
        while (($fila = fgetcsv($handle, 1000, ",")) !== false) {
            $datos[] = $fila;
        }
        fclose($handle);
    }
    return $datos;
}

function escribirDatos($archivo, $datos)
{
    if (($handle = fopen($archivo, "w")) !== false) {
        foreach ($datos as $fila) {
            fputcsv($handle, $fila);
        }
        fclose($handle);
    }
}
