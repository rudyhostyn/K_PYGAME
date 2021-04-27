import pygame as pg
import sys

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
ANCHO = 800
ALTO = 600

pg.init()

pantalla = pg.display.set_mode((800,600))

game_over = False
x = ANCHO // 2
y = ALTO // 2

vx = -5
vy = -5

radio = 10

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
        radio += 0.3

        if y <= 0 or y >= ALTO:
            vy = -vy
            radio = 0.3
            
        if x <= 0 or x >= ANCHO:
            vx = -vx
                          
        pantalla.fill(NEGRO)
        pg.draw.circle(pantalla, ROJO, (x, y), radio) 
       
        pg.display.flip()

pg.quit()
sys.exit()
