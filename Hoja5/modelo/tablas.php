<?php
function generarTabla($csv, $tipo)
{
    $tabla = "<a class='nav-link dropdown-toggle' href='#' role='button' data-bs-toggle='dropdown' aria-expanded='false'>Acciones</a>";
    $tabla .= "<ul class='dropdown-menu'>";
    $tabla .= "<li><a class='dropdown-item' href='vistas/insertar_" . $tipo . ".html'>Añadir</a></li>";
    $tabla .= "<li><a class='dropdown-item' href='vistas/modificar_" . $tipo . ".html'>Modificar</a></li>";
    $tabla .= "<li><a class='dropdown-item' href='vistas/eliminar_" . $tipo . ".html'>Eliminar</a></li></ul>";
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
