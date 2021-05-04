import pygame as pg
import sys
from random import randint, choice
import random

WHITE = (255,255,255)
NEGRO = (0,0,0)
ANCHO = 800
ALTO = 600
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
            pg.time.delay(2000)
            self.x = ANCHO // 2
            self.y = ALTO // 10
            self.vx = randint(5, 10)*choice([-1,1])
            self.vy = randint(5, 10)*choice([-1,1])
                       
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
    
    def score(self, objeto):
        choqueX = self.x >= objeto.x and self.x <= objeto.x + objeto.anchura or \
            self.x+self.anchura >= objeto.x and self.x+self.anchura <= objeto.x + objeto.anchura

        choqueY = self.y >= objeto.y and self.y <= objeto.y + objeto.altura or \
            self.y+self.altura >= objeto.y and self.y+self.altura  <= objeto.y + objeto.altura
        if choqueX and choqueY:    
            return True
           
        
            
        
vidas = 3
marcadorcero = ""
score = 0


bola = Bola(randint(0, ANCHO),
            randint(0, ALTO),
            randint(5, 10)*choice([-1,1]),
            randint(5, 10)*choice([-1,1]),
            #(randint(0, 255), randint(0,255), randint(0,255)))
            (255, 255, 255))

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

class Marcador():
    def __init__(self, surface, text, size, x, y):
        self.surface = surface
        self.text = text
        self.size = size
        self.x = x
        self.y = y

    def dibuja_marcador(self, surface, text, size, x, y):
        font = pg.font.SysFont("arial", size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect = (x,y)
        surface.blit(text_surface, text_rect)
        

marcador1 = Marcador(pantalla, str(vidas), 35, ANCHO // 10,  ALTO // 10)
marcador2 = Marcador(pantalla, str(marcadorcero), 35, ANCHO // 2,  ALTO // 2)
marcador3 = Marcador(pantalla, str(score), 35, ANCHO - (ANCHO // 10),  ALTO // 10)

game_over = False
while not game_over and vidas > 0:
    v = reloj.tick(40)
    #Gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
 

    # Modificación de estado
    pierdebola = bola.actualizar()
    if pierdebola:
            vidas -= 1
    
    if vidas == 0:
        reloj.tick(1)
        marcadorcero = "Game Over"
    
    marcadorpuntos = bola.score(raqueta)
    if marcadorpuntos:
            score += 10

    
    # Gestión de la pantalla
    pantalla.fill(NEGRO)
    bola.dibujar(pantalla)
    raqueta.dibujar(pantalla)
    raqueta.actualizar()
    bola.comprueba_colision(raqueta)
    #marcador
    marcador1.dibuja_marcador(pantalla, str(vidas), 35, ANCHO // 10,  ALTO // 10)
    marcador2.dibuja_marcador(pantalla, str(marcadorcero), 35, ANCHO // 2,  ALTO // 2)
    marcador3.dibuja_marcador(pantalla, str(score), 35, ANCHO - (ANCHO // 10),  ALTO // 10)
    
    


    pg.display.flip()

