<?php
class Producto
{
    private $nombre;
    private $precio;
    private $cantidad;

    public function __construct($nombre, $precio, $cantidad)
    {
        $this->nombre = $nombre;
        $this->precio = $precio;
        $this->cantidad = $cantidad;
    }
    public function getNombre()
    {
        return $this->nombre;
    }
    public function getPrecio()
    {
        return $this->precio;
    }
    public function getCantidad()
    {
        return $this->cantidad;
    }
}

class ProductoImportado extends Producto
{
    public $impuestoAdicional;

    public function __construct($nombre, $precio, $cantidad, $impuestoAdicional)
    {
        parent::__construct($nombre, $precio, $cantidad);
        $this->impuestoAdicional = $impuestoAdicional;
    }

    public function calcularPrecioFinal()
    {
        return $this->getPrecio() + $this->impuestoAdicional;
    }
}

$producto = new Producto("Camiseta", 20.00, 5);
$productoImportado = new ProductoImportado("Reloj", 100.00, 2, 15.00);

// Mostrar detalles del Producto
echo "Producto: " . $producto->getNombre() . "\n";
echo "Precio: " . $producto->getPrecio() . "€\n";
echo "Cantidad: " . $producto->getCantidad() . "\n\n";

// Mostrar detalles del ProductoImportado
echo "Producto Importado: " . $productoImportado->getNombre() . "\n";
echo "Precio: " . $productoImportado->getPrecio() . "€\n";
echo "Cantidad: " . $productoImportado->getCantidad() . "\n";
echo "Impuesto Adicional: " . $productoImportado->impuestoAdicional . "€\n";
echo "Precio Final: " . $productoImportado->calcularPrecioFinal() . "€\n";
