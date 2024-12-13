<?php
function generarTabla($csv, $tipo)
{
    $tabla = "<a href='vistas/formulario_" . $tipo . ".html' class='btn btn-primary mb-3'>Añadir Nuevo" . ucfirst($tipo) . "</a>";
    $tabla .= "<table class='table table-striped'>";
    if (($archivo = fopen($csv, "r"))) {
        $cabeceras = fgetcsv($archivo);
        $tabla .= "<thead><tr>";
        foreach ($cabeceras as $cabecera) {
            $tabla .= "<th>" . htmlspecialchars($cabecera) . "</th>";
        }
        $tabla .= "</tr></thead><tbody>";
        while (($fila = fgetcsv($archivo))) {
            $tabla .= "<tr>";
            foreach ($fila as $celda) {
                $tabla .= "<td>" . htmlspecialchars($celda) . "</td>";
            }
            $tabla .= "</tr>";
        }
        fclose($archivo);
    }
    $tabla .= "</tbody></table>";
    return $tabla;
}
