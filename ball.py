import pygame as pg
import sys
from random import randint, choice
import random


NEGRO = (0,0,0)
ANCHO = 1200
ALTO = 750
RADIO = 10

pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))
reloj = pg.time.Clock()

class Bola():

    def __init__(self, x, y, vx=5, vy=5, color=(255, 255, 255), radio=7):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.radio = radio
        self.anchura = radio*2
        self.altura = radio*2

    def actualizar(self):

        bola.x += bola.vx
        bola.y += bola.vy
        
        if self.y <=0:
            self.vy = -self.vy

        if self.x <=0 or self.x >= ANCHO:
            self.vx = -self.vx

        if self.y >= ALTO:
            self.x = ANCHO // 2
            self.y = ALTO // 2
            self.vx = randint(5, 10)*choice([-1,1])
            self.vy = randint(5, 10)*choice([-1,1])
            pg.time.delay(500)
           
            return True
        return False
    
    def dibujar(self, lienzo):
        pg.draw.circle(lienzo, self.color, (self.x, self.y), self.radio)

    def comprueba_colision(self, objeto):
        choqueX = self.x >= objeto.x and self.x <= objeto.x + objeto.anchura or \
            self.x+self.anchura >= objeto.x and self.x+self.anchura <= objeto.x + objeto.anchura

        choqueY = self.y >= objeto.y and self.y <= objeto.y + objeto.altura or \
            self.y+self.altura >= objeto.y and self.y+self.altura  <= objeto.y + objeto.altura
        if choqueX and choqueY:
            self.vy *= -1
        

           
vidas = 3

bola = Bola(randint(0, ANCHO),
            randint(0, ALTO),
            randint(5, 10)*choice([-1,1]),
            randint(5, 10)*choice([-1,1]),
            (randint(0, 255), randint(0,255), randint(0,255)))

class Raqueta():
    def __init__(self, X=0, Y=0):
        self.altura = 25
        self.anchura = 100
        self.color = (255,255,255)
        self.x = (ANCHO - self.anchura) // 2
        self.y = ALTO - self.altura - 15
        self.vy = 0
        self.vx = 20

    def dibujar(self, lienzo):
        rect = pg.Rect(self.x , self.y, self.anchura, self.altura)
        pg.draw.rect(lienzo, self.color, rect)

    def actualizar(self):
        teclas_pulsadas = pg.key.get_pressed() # se mueve mientras esté apretado
        if teclas_pulsadas[pg.K_LEFT] and self.x > 0:
            self.x -= self.vx
        if teclas_pulsadas[pg.K_RIGHT] and self.x < ANCHO - self.anchura:
            self.x += self.vx



raqueta = Raqueta()

game_over = False
while not game_over and vidas > 0:
    v = reloj.tick(60)
    #Gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
 

    # Modificación de estado
    pierdebola = bola.actualizar()
    if pierdebola:
            vidas -= 1
    # Gestión de la pantalla
    pantalla.fill(NEGRO)
    bola.dibujar(pantalla)
    raqueta.dibujar(pantalla)
    raqueta.actualizar()
    bola.comprueba_colision(raqueta)


    pg.display.flip()

