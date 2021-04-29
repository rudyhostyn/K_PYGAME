import pygame as pg
import sys
from random import randint
import random


NEGRO = (0,0,0)
ANCHO = 1200
ALTO = 750
RADIO = 10
'''
def rebota(str):
    if str == ANCHO:
        if bola.x <= 0 + RADIO or bola.x >= str - RADIO:
            return -1
        return 1
    elif str == ALTO:
        if bola.x <= 0 + RADIO or bola.x >= str - RADIO:
            return -1
        return 1
'''
def sig():
    st1 = randint(1,2)
    if st1 == 1:
        return -1
    return 1

pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))
reloj = pg.time.Clock()

class Bola():
    def __init__(self, x, y, vx=5, vy=5, color=(255, 255, 255), radio=10):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.radio = radio

    def actualizar(self):

        bola.x += bola.vx
        bola.y += bola.vy
        
        if self.y <=0 or self.y >= ALTO:
            self.vy = -self.vy

        if self.x <=0 or self.x >= ANCHO:
            self.vx = -self.vx
    
    def dibujar(self, lienzo):
        pg.draw.circle(lienzo, self.color, (self.x, self.y), self.radio)
            
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
        bola.actualizar()

    # Gestión de la pantalla
    pantalla.fill(NEGRO)
    for bola in bolas:
        bola.dibujar(pantalla)


    pg.display.flip()

