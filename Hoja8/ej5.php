<?php
class Personaje
{
    public $nombre;
    public $nivel;
    public $puntosVida;
    public $puntosAtaque;
    public function atacar(Personaje $objetivo)
    {
        $objetivo->puntosVida -= $this->puntosAtaque;
        echo "$this->nombre realiza un ataque a $objetivo->nombre y le quita $this->puntosAtaque puntos de vida.\n";
        if ($objetivo->puntosVida <= 0) {
            echo "$objetivo->nombre ha sido derrotado por $this->nombre.";
        } else {
            echo "$objetivo->nombre tiene $objetivo->puntosVida puntos de vida restantes.\n";
        }
    }
    public function curarse($puntos)
    {
        $this->puntosVida += $puntos;
        echo "$this->nombre se cura y ahora tiene $this->puntosVida puntos de vida.\n";
    }
    public function subirNivel()
    {
        $this->nivel++;
        $this->puntosVida += 5;
        $this->puntosAtaque += 2;
        echo "$this->nombre ha subido al nivel $this->nivel!\n";
    }
}

$guerrero = new Personaje();
$guerrero->nombre = "Guerrero";
$guerrero->nivel = 1;
$guerrero->puntosVida = 30;
$guerrero->puntosAtaque = 5;

$mago = new Personaje();
$mago->nombre = "Mago";
$mago->nivel = 1;
$mago->puntosVida = 20;
$mago->puntosAtaque = 7;

// Simulación de una pequeña batalla
$guerrero->atacar($mago);
$mago->atacar($guerrero);
$guerrero->curarse(10);
$mago->atacar($guerrero);
$guerrero->subirNivel();
$guerrero->atacar($mago);
$mago->subirNivel();
$mago->curarse(5);
$mago->atacar($guerrero);
$guerrero->subirNivel();
$guerrero->atacar($mago);
$mago->atacar($guerrero);
$guerrero->atacar($mago);
