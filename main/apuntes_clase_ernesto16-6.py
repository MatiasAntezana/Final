"""
0   A4  .5
.5  Bb4 .5
1   B4  .5
1.5 C4  .5
2   Cs4 .5
2.5 D4  .5

DISEÑO:
Sintetizador -> Puedo pensarlo como partitura de una sola nota
El instrumento de 1 solo armonico, con la envolvente de ataque nulo, sustain constante y decay nulo
El sintetizador recibe como parámetro el instrumento y la partitura
El método sintetizar() comprondra un audio a partir de la lección
FASE B:
Interactuar con el metalofón-bot
En vez de crear un audio a partir de audios aditivos, hay que interactuar con un server que está
Va a haber una función que se encargará de eliminar aquellas nota que entran en conflicto
"""