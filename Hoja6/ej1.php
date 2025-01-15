<?php
class Libro
{
    public $titulo;
    public $autor;
    public $paginas;
    public function mostrarInfo()
    {
        echo "Título: $this->titulo\n";
        echo "Autor: $this->autor\n";
        echo "Número de páginas: $this->paginas\n";
    }
}

$miLibro = new Libro();
$miLibro->titulo = "Libro A";
$miLibro->autor = "Autor A";
$miLibro->paginas = "100";
$miLibro->mostrarInfo();
