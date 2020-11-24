# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 18:09:18 2020

@author: Keven
"""
import pygame as p
import sys


p.init()
p.mixer.init()
p.display.set_caption("Tower-Madness")
font= p.font.Font('Fuentes\\spacerunnertwoital.TTF',35)
font_3= p.font.Font('Fuentes\\spacerunnertwoital.TTF',30)
font_1= p.font.Font('Fuentes\\spacerunnertwoital.TTF',100)
font_2= p.font.Font('Fuentes\\spacerunnertwoital.TTF',150)
clock=p.time.Clock()
size=width,height=1280,720
pantalla=p.display.set_mode(size)
bg_image=p.image.load("images\\fondo-proyecto.png")
bg_image=bg_image.convert()
boton=p.image.load("images\\boton.png")
back=p.image.load("images\\flecha-regresar.png")
select=p.mixer.Sound('efectos\\sonido_boton.wav')
tap=p.mixer.Sound('efectos\\boton_tap.wav')
#p.mixer.music.load("effectos\\fondo.wav")
#p.mixer.music.play(-1)
#p.mixer.music.set_volume(0.2)
canal1=p.mixer.Channel(0)
canal2=p.mixer.Channel(1)

def draw_txt(texto, font, color, surface, x, y):
    textobj=font.render(texto, True, color)
    textrect=textobj.get_rect()
    textrect.topleft=( x, y)
    surface.blit(textobj,textrect)

def controles_1():
    
    running = True 
    click=False
    while running:
        casilla=False
        pantalla.blit(bg_image,(0,0))
        draw_txt("CONTROLES",font_1, (0,0,0),pantalla,343,83)
        draw_txt("CONTROLES",font_1, (255,255,255),pantalla,330,80)
        mx,my=p.mouse.get_pos()
        boton_b=pantalla.blit(back,(50,630))
        if boton_b.collidepoint((mx,my)):
            casilla=True
            pantalla.blit(bg_image,boton_b,boton_b)
            boton_b=pantalla.blit(back,(50,625))
            canal1.play(tap)
            if click:
                running=False
                break
                #main_menu()
        for event in p.event.get():
            if event.type==p.QUIT:
                p.quit()
                sys.exit()
            elif event.type==p.KEYDOWN:
                if event.key==p.K_ESCAPE:
                    running==False
                    break
                    #main_menu()
            elif event.type==p.MOUSEBUTTONDOWN:
                if event.button==1 and casilla:
                    click=True
        p.display.update()
        clock.tick(60)