<?php
require_once "funciones.php";
require_once "mapeo_datos.php";

$id = $_POST["id"] ?? null;
$tipo = $_GET["tipo"] ?? null;

if ($tipo && $id) {
    $archivo = "../datos/{$tipoPlural[$tipo]}.csv";
    $datos = leerDatos($archivo);
    $datoSeleccionado = null;

    foreach ($datos as $index => $dato) {
        if ($index > 0 && $dato[0] == $id) {
            $datoSeleccionado = $dato;
            break;
        }
    }

    if ($datoSeleccionado !== null):
?>
        <!DOCTYPE html>
        <html lang="es">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
            <title>Editar <?= $tipo ?></title>
        </head>

        <body>
            <div class="container mt-4">
                <h1>Editar <?= $tipo ?></h1>
                <form action="actualizar.php?tipo=<?= $tipo ?>" method="POST">
                    <input type="hidden" name="id" value="<?= $datoSeleccionado[0] ?>">
                    <?php
                    // Generar entradas según el tipo
                    if (array_key_exists($tipo, $camposEntrada)) {
                        foreach ($camposEntrada[$tipo] as $index => $name) {
                            // Omitir cambiar el ID
                            if ($index === 0) {
                                continue;
                            }
                            $value = $datoSeleccionado[$index];
                            echo "<div class='mb-3'>";
                            echo "<label for='{$name}' class='form-label'>" . ucfirst($name) . ":</label>";
                            // Tipo por defecto
                            $inputType = "text";
                            if ($name === "correo") {
                                $inputType = "email";
                            } elseif ($name === "precio" || $name === "stock") {
                                $inputType = "number";
                            }
                            echo "<input type='{$inputType}' class='form-control' name='{$name}' id='{$name}' value='{$value}' required>";
                            echo "</div>";
                        }
                    }
                    ?>
                    <button type="submit" class="btn btn-primary mb-2">Actualizar</button>
                </form>
        </body>

        </html>
<?php
    else:
        echo "<h1>Error: " . ucfirst($tipo) . " no encontrado.</h1>";
    endif;
} else {
    echo "<h1>Error: Tipo o ID no especificado</h1>";
}
echo "<a href='../index.php?opcion={$tipoPlural[$tipo]}'>Volver al listado</a>";
?>
</div>