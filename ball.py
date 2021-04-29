import pygame as pg
import sys
from random import randint
import random


NEGRO = (0,0,0)
ANCHO = 1200
ALTO = 750
RADIO = 10

def rebota(x, str):
    if str == ANCHO:
        if x <= 0 + RADIO or x >= str - RADIO:
            return -1
        return 1
    elif str == ALTO:
        if x <= 0 + RADIO or x >= str - RADIO:
            return -1
        return 1

def sig():
    st1 = randint(1,2)
    if st1 == 1:
        return -1
    return 1

pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))
reloj = pg.time.Clock()

class Bola():
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color

 
bolas = []

for _ in range(1):
    bola = Bola(randint(0, ANCHO),
            randint(0, ALTO),
            sig()*randint(5, 10),
            sig()*randint(5, 10),
            (randint(0, 255), randint(0,255), randint(0,255)))
    
    bolas.append(bola)

game_over = False
while not game_over:
    v = reloj.tick(60)
   
    #Gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    # Modificación de estado
    for bola in bolas:

        bola.x += bola.vx
        bola.y += bola.vy
                        
        bola.vy *= rebota(bola.y, ALTO)  # bola.vy = (-1 ó 1)*bola.vy
        bola.vx *= rebota(bola.x, ANCHO)

    # Gestión de la pantalla
    pantalla.fill(NEGRO)
    for bola in bolas:
        pg.draw.circle(pantalla, bola.color, (bola.x, bola.y), RADIO)


    pg.display.flip()

