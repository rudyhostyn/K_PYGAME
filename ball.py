import pygame as pg
import sys
from  random import randint

def rebotaX(x):
    if x <=0 or x>= ANCHO:
        return -1
    return 1

def rebotaY(x):
    if x <=0 or x>= ALTO:
        return -1
    return 1

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
ANCHO = 800
ALTO = 600

pg.init()

pantalla = pg.display.set_mode((800,600))

# Bola 1
game_over = False
x = ANCHO // 2
y = ALTO // 2
vx = -5
vy = -5

# Bola 1
x2 = randint(0, ANCHO)
y2 = randint(0, ALTO)
vx2 = randint(5,15)
vy2 = randint(5,15)



radio = 10
vradio = +0.3

reloj = pg.time.Clock()

while not game_over:
        reloj.tick(60)
        #gestion de eventos
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                game_over = True
        #pg.time.delay(10)
        x += vx
        y += vy
        x2 += vx2
        y2 += vy2

        vy *=rebotaY(y)
        vx *=rebotaX(x)

        vy2 *=rebotaY(y2)
        vx2 *=rebotaX(x2)

        radio += vradio

                                  
        pantalla.fill(NEGRO)
        pg.draw.circle(pantalla, ROJO, (x, y), radio)
        pg.draw.circle(pantalla, VERDE, (x2, y2), radio) 
       
        pg.display.flip()

pg.quit()
sys.exit()
