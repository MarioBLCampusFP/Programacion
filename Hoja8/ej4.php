<?php
class Carrito
{
    public $productos = [];
    public function agregarProducto($nombre, $precio, $cantidad)
    {
        if (isset($this->productos[$nombre])) {
            echo "El producto '$nombre' ya está en el carrito.\n";
        } else {
            $this->productos[$nombre] = [
                "precio" => $precio,
                "cantidad" => $cantidad
            ];
        }
    }
    public function quitarProducto($nombre)
    {
        if (isset($this->productos[$nombre])) {
            unset($this->productos[$nombre]);
        } else {
            echo "El producto '$nombre' no está en el carrito.\n";
        }
    }
    public function calcularTotal()
    {
        $total = 0;
        foreach ($this->productos as $producto) {
            $total += $producto["precio"] * $producto["cantidad"];
        }
        return $total;
    }
    public function mostrarDetalleCarrito()
    {
        echo "Detalles del carrito:\n";
        foreach ($this->productos as $nombre => $producto) {
            echo "Producto: $nombre, Precio: {$producto['precio']}, Cantidad: {$producto['cantidad']}\n";
        }
    }
}

$carrito = new Carrito();

$carrito->agregarProducto("Manzana", 1.50, 3);
$carrito->agregarProducto("Banana", 0.75, 5);
$carrito->agregarProducto("Naranja", 1.00, 2);

$carrito->mostrarDetalleCarrito();

$total = $carrito->calcularTotal();
echo "Total del carrito: $total\n";
echo "\n";

$carrito->quitarProducto("Banana");

$carrito->mostrarDetalleCarrito();

$total = $carrito->calcularTotal();
echo "Total del carrito: $total\n";
