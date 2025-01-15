<?php
require_once "mapeo_datos.php";
$tipo = $_GET["tipo"] ?? null;

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $datos = [];
    foreach ($camposEntrada[$tipo] as $name) {
        $datos[] = $_POST[$name] ?? "";
    }
    $linea = implode(',', $datos) . "\n";
    file_put_contents("../datos/{$tipoPlural[$tipo]}.csv", $linea, FILE_APPEND);

    header("Location: ../index.php?opcion={$tipoPlural[$tipo]}");
    exit();
}
