import pygame as pg
import sys
from random import randint

def rebotaX(x):
    if x <=0 or x >=ANCHO:
        return -1

    return 1

def rebotaY(y):
    if y <=0 or y >=ALTO:
        return -1

    return 1


ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0,0,0)
ANCHO = 800
ALTO = 600

pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))

game_over = False
x = ANCHO // 2
y = ALTO // 2
vx = -13
vy = -13
reloj = pg.time.Clock()

bolas = []
for _ in range(20):
    bola = {'x': randint(0, ANCHO),
            'y': randint(0, ALTO),
            'vx': randint(5, 10),
            'vy': randint(5, 10),
            'color': (randint(0, 255), randint(0,255), randint(0,255))
    }
    bolas.append(bola)

game_over = False
while not game_over:
    v = reloj.tick(60)
    print(v)
    #Gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    # Modificación de estado
    x += vx
    y += vy
    for bola in bolas:
        bola['x'] += bola['vx']
        bola['y'] += bola['vy']

        bola['vy'] *= rebotaY(bola['y'])
        bola['vx'] *= rebotaX(bola['x'])

    if y <= 0 or y>= ALTO:
        vy = -vy
    
    if x <= 0 or x >= ANCHO:
        vx = -vx

    # Gestión de la pantalla
    pantalla.fill(NEGRO)
    pg.draw.circle(pantalla, ROJO, (x, y), 10)
    for bola in bolas:
        pg.draw.circle(pantalla, bola['color'], (bola['x'], bola['y']), 10)


    pg.display.flip()

