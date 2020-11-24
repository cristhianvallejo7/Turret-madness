import pygame as p
import sys
#import Clases_juego

p.init()
p.mixer.init()
font = p.font.Font('Fuentes\\spacerunnertwoital.TTF', 35)
font_3 = p.font.Font('Fuentes\\spacerunnertwoital.TTF', 30)
font_1 = p.font.Font('Fuentes\\spacerunnertwoital.TTF', 80)
font_2 = p.font.Font('Fuentes\\spacerunnertwoital.TTF', 80)
clock = p.time.Clock()
size = width, height = 720, 400
pantalla = p.display.set_mode(size)
bg_image = p.image.load("images\\fondo1.png")
bg_image = bg_image.convert()
gameover =p.image.load("images\\gamewin.png")
boton = p.image.load("images\\boton.png")
select = p.mixer.Sound('efectos\\sonido_boton.mp3')
tap = p.mixer.Sound('efectos\\boton_tap.mp3')
p.mixer.music.load("efectos\\fondo.mp3")
p.mixer.music.play(-1)
p.mixer.music.set_volume(0.2)
canal1 = p.mixer.Channel(0)
canal2 = p.mixer.Channel(1)


def draw_txt(texto, font, color, surface, x, y):
    textobj = font.render(texto, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    running = True
    click = False
    boton_1 = None
    boton_2 = None
    pos = 30, 200
    while running:
        if boton_1 == None and boton_2 == None:
            pantalla.blit(bg_image, (0, 0))
            pantalla.blit(gameover,(200,0))
            draw_txt("LEVEL", font_2, (0, 0, 0), pantalla, 25, 18)
            draw_txt("LEVEL", font_2, (255, 255, 255), pantalla, 20, 10)
            draw_txt("WIN", font_1, (0, 0, 0), pantalla, 35, 86)
            draw_txt("WIN", font_1, (255, 255, 255), pantalla, 30, 78)
        else:
            pantalla.blit(bg_image, boton_1, boton_1)
            pantalla.blit(bg_image, boton_2, boton_2)


        mx, my = p.mouse.get_pos()
        boton_1 = pantalla.blit(boton, pos)
        boton_2 = pantalla.blit(boton, (pos[0], pos[1] + 100))
        draw_txt("Siguiente", font, (0, 0, 0), pantalla, 37, 208)
        draw_txt("Siguiente", font, (255, 255, 255), pantalla, 35, 205)
        draw_txt("Salir", font, (0, 0, 0), pantalla, 77, 308)
        draw_txt("Salir", font, (255, 255, 255), pantalla, 75, 305)


        if boton_1.collidepoint((mx, my)):
            pantalla.blit(bg_image, boton_1, boton_1)
            boton_1 = pantalla.blit(boton, (pos[0], pos[1] - 5))
            draw_txt("Siguiente", font, (0, 0, 0), pantalla, 37, 200)
            draw_txt("Siguiente", font, (255, 255, 255), pantalla, 35, 197)
            canal1.play(tap)
            if click:
                canal2.play(select)
                reiniciar()
        if boton_2.collidepoint((mx, my)):
            pantalla.blit(bg_image, boton_2, boton_2)
            boton_2 = pantalla.blit(boton, (pos[0], pos[1] + 95))
            draw_txt("Salir", font, (0, 0, 0), pantalla, 77, 300)
            draw_txt("Salir", font, (255, 255, 255), pantalla, 75, 297)
            canal1.play(tap)
            if click:
                canal1.play(select)
                salir()
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
                sys.exit()
            elif event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    running == False
            elif event.type == p.MOUSEBUTTONDOWN:
                if (event.button == 1 and boton_1.collidepoint((mx, my))) or (
                        event.button == 1 and boton_2.collidepoint((mx, my))) or (
                        event.button == 1 and boton_3.collidepoint((mx, my))):
                    click = True
        p.display.update()
        clock.tick(60)


def reiniciar():
    running = False
    import lvl_1
    sys.exit()
    clock.tick(60)


def salir():
    running = False
    sys.exit()
    clock.tick(60)


main_menu()
