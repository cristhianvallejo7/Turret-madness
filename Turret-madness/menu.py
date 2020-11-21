import pygame as p
import sys
import Niveles
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
p.mixer.music.load("effectos\\fondo.wav")
p.mixer.music.play(-1)
p.mixer.music.set_volume(0.2)
canal1=p.mixer.Channel(0)
canal2=p.mixer.Channel(1)

def draw_txt(texto, font, color, surface, x, y):
    textobj=font.render(texto, True, color)
    textrect=textobj.get_rect()
    textrect.topleft=( x, y)
    surface.blit(textobj,textrect)    
    
def main_menu():
    running=True
    click=False
    boton_1=None
    boton_2=None
    boton_3=None
    pos=540,300
    k,k1,k2=0,0,0
    while running:
        casilla=False
        pantalla.blit(bg_image,(0,0))
        draw_txt("TURRET",font_2, (0,0,0),pantalla,335,65)
        draw_txt("TURRET",font_2, (255,255,255),pantalla,332,50)
        draw_txt("MADNESS",font_1, (0,0,0),pantalla,381,185)
        draw_txt("MADNESS",font_1, (255,255,255),pantalla,368,170)
        if not(boton_1==None or boton_2==None or boton_3==None): 
            pantalla.blit(bg_image,boton_1,boton_1)
            pantalla.blit(bg_image,boton_2,boton_2)       
            pantalla.blit(bg_image,boton_3,boton_3)
             
        mx,my=p.mouse.get_pos()
        boton_1=pantalla.blit(boton,pos)
        boton_2=pantalla.blit(boton,(pos[0],pos[1]+100))
        boton_3=pantalla.blit(boton,(pos[0],pos[1]+200))
        draw_txt("JUGAR",font, (0,0,0),pantalla,580,308)
        draw_txt("JUGAR",font, (255,255,255),pantalla,578,305)
        draw_txt("OPCIONES",font, (0,0,0),pantalla,554,408)
        draw_txt("OPCIONES",font, (255,255,255),pantalla,552,405)
        draw_txt("CONTROLES",font_3, (0,0,0),pantalla,554,511)
        draw_txt("CONTROLES",font_3, (255,255,255),pantalla,552,508)
        
        if boton_1.collidepoint((mx,my)):
            casilla=True
            pantalla.blit(bg_image,boton_1,boton_1)
            boton_1=pantalla.blit(boton,(pos[0],pos[1]-5))
            draw_txt("JUGAR",font, (0,0,0),pantalla,580,303)
            draw_txt("JUGAR",font, (255,255,255),pantalla,578,300)
            if k==0:
                canal1.play(tap)
                k+=1
            if click:
                canal2.play(select)
                click=False
                Niveles.niveles()
        else:
            k=0
            
        if boton_2.collidepoint((mx,my)):
            casilla=True
            pantalla.blit(bg_image,boton_2,boton_2)
            boton_2=pantalla.blit(boton,(pos[0],pos[1]+95))
            draw_txt("OPCIONES",font, (0,0,0),pantalla,554,403)
            draw_txt("OPCIONES",font, (255,255,255),pantalla,552,400)
            if k1==0:
                canal1.play(tap)
                k1+=1
            if click:
                canal1.play(select)
                opciones()
        else:
            k1=0
            
        if boton_3.collidepoint((mx,my)):
            casilla=True
            pantalla.blit(bg_image,boton_3,boton_3)
            boton_3=pantalla.blit(boton,(pos[0],pos[1]+195))
            draw_txt("CONTROLES",font_3, (0,0,0),pantalla,554,506)
            draw_txt("CONTROLES",font_3, (255,255,255),pantalla,552,503)
            if k2==0:
                canal1.play(tap)
                k2+=1
            if click:
                canal1.play(select)
                opciones()
        else:
            
            k2=0
        for event in p.event.get():
            if event.type==p.QUIT:
                running=False
                sys.exit()
            elif event.type==p.KEYDOWN:
                if event.key==p.K_ESCAPE:
                    running==False
            elif event.type==p.MOUSEBUTTONDOWN:
                
                if event.button==1 and casilla:
                    click=True
        p.display.update()
        clock.tick(60)
def opciones():
    running = True 
    click=False
    while running:
        casilla=False
        pantalla.blit(bg_image,(0,0))
        draw_txt("opciones",font_1, (0,0,0),pantalla,343,83)
        draw_txt("opciones",font_1, (255,255,255),pantalla,330,80)
        mx,my=p.mouse.get_pos()
        boton_b=pantalla.blit(back,(50,630))
        if boton_b.collidepoint((mx,my)):
            casilla=True
            pantalla.blit(bg_image,boton_b,boton_b)
            boton_b=pantalla.blit(back,(50,625))
            canal1.play(tap)
            if click:
                running=False
                main_menu()
        for event in p.event.get():
            if event.type==p.QUIT:
                p.quit()
                sys.exit()
            elif event.type==p.KEYDOWN:
                if event.key==p.K_ESCAPE:
                    running==False
                    main_menu()
            elif event.type==p.MOUSEBUTTONDOWN:
                if event.button==1 and casilla:
                    click=True
        p.display.update()
        clock.tick(60)

def controles():
    
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
                main_menu()
        for event in p.event.get():
            if event.type==p.QUIT:
                p.quit()
                sys.exit()
            elif event.type==p.KEYDOWN:
                if event.key==p.K_ESCAPE:
                    running==False
                    main_menu()
            elif event.type==p.MOUSEBUTTONDOWN:
                if event.button==1 and casilla:
                    click=True
        p.display.update()
        clock.tick(60)
main_menu()

