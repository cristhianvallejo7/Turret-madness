import pygame as p
import sys
import numpy as np
import lvl_1
#import menu
p.init()
p.mixer.init()
def niveles():
    p.display.set_caption("Tower-Madness")
    font_1= p.font.Font('Fuentes\\spacerunnertwoital.TTF',100)
    clock=p.time.Clock()
    pantalla=p.display.set_mode((1280,720))
    bg_image=p.image.load("images\\fondo-proyecto.png")
    bg_image=bg_image.convert()
    back=p.image.load("images\\flecha-regresar.png")
    select=p.mixer.Sound('efectos\\sonido_boton.wav')
    tap=p.mixer.Sound('efectos\\boton_tap.wav')
    pop=p.mixer.Sound("Sound\\GUI.wav")
    wrong=p.mixer.Sound("Sound\\wrong.wav")
    #p.mixer.music.load("effectos\\fondo.ogg")
    #p.mixer.music.play(-1)
    #p.mixer.music.set_volume(0.2)
    canal1=p.mixer.Channel(0)
    canal2=p.mixer.Channel(1)
    Save=open("Save.txt","r")
    state1=Save.readline().replace("\n","")
    st1=Save.readline().replace("\n","")
    state2=Save.readline().replace("\n","")
    st2=Save.readline().replace("\n","")
    state3=Save.readline().replace("\n","")
    st3=Save.readline().replace("\n","")
    Save.close()
    k1,k2,k3,k4=0,0,0,0
    def draw_txt(texto, font, color, x, y,surface=pantalla):
        textobj=font.render(texto, True, color)
        textrect=textobj.get_rect(center=(int(x),int(y)))
        surface.blit(textobj,textrect)    
    def mostrar(x,y,im,a=0,j=1):
        imr=p.transform.rotozoom(im,a,j)
        centro=imr.get_rect(center=(int(x),int(y)))
        pantalla.blit(imr,centro)  
    states=[state1,state2,state3]
    escotilla=[]
    imgnvlsC=[]
    imgnvlsD=[]
    n=[]
    for i in range(10):
        escotilla.append(p.image.load("images\\Niveles\\Esctilla"+str(i)+".png").convert_alpha())
    countescotilla=[0,0,0]
    xesc,yesc=[],[]
    for i in range(3):
        if states[i]=="Completo":
            n.append(1)
        else:
            n.append(0)
        imgnvlsC.append(p.image.load("images\\Niveles\\Fondon"+str(i+1)+".png").convert_alpha())
        imgnvlsD.append(p.image.load("images\\Niveles\\Fondon"+str(i+1)+"1.png").convert_alpha())
        xesc.append((i+1)*(1180-200)/3)
        yesc.append(720/2)
    imgnvls=[imgnvlsD,imgnvlsC]
    S0=p.image.load("images\\Niveles\\S00.png").convert_alpha()
    S1=p.image.load("images\\Niveles\\S10.png").convert_alpha()
    xs,ys=[],[]
    counts=0
    S=[S1,S0]
    est=[]
    for i in range(5):
        if i <int(st1):
            est.append(1)
        else:
            est.append(0)
        xs.append((i)*(200)/5+xesc[0]-80)
        ys.append(720/2+80)
    for i in range(5):
        if i<int(st2):
            est.append(1)
        else:
            est.append(0)
        xs.append((i)*(200)/5+xesc[1]-80)
        ys.append(720/2+80)
    for i in range(5):
        if i <int(st3):
            est.append(1)
        else:
            est.append(0)
        xs.append((i)*(200)/5+xesc[2]-80)
        ys.append(720/2+80)
    running=True
    while running:
        click=False
        for event in p.event.get():
            if event.type==p.QUIT:
                running=False
                sys.exit()
            elif event.type==p.KEYDOWN:
                if event.key==p.K_ESCAPE:
                    running==False
            elif event.type==p.MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
        mx,my=p.mouse.get_pos()
        pantalla.blit(bg_image,(0,0))
        if xesc[0]-100<=mx<=xesc[0]+100 and yesc[0]-100<=my<yesc[0]+100:
            if click:
                lvl_1.game()
                click=False
            if k2==0:
                k2+=1
                if states[0]=="Disponible" or states[0]=="Completo":
                    canal2.play(pop)
                else:
                    canal2.play(wrong)
        else:
            k2=0
        if xesc[1]-100<=mx<=xesc[1]+100 and yesc[1]-100<=my<yesc[1]+100:
            if click:
                #Clases_juego.game() Niv2
                click=False
            if k3==0:
                k3+=1
                if states[1]=="Disponible" or states[1]=="Completo":
                    canal2.play(pop)
                else:
                    canal2.play(wrong)
        else:
            k3=0
        if xesc[2]-100<=mx<=xesc[2]+100 and yesc[2]-100<=my<yesc[2]+100:
            if click:
                #Clases_juego.game() Niv2
                click=False
            if k4==0:
                k4+=1
                if states[2]=="Disponible" or states[2]=="Completo":
                    canal2.play(pop)
                else:
                    canal2.play(wrong)
        else:
            k4=0
        for i in range(3):
            if states[i]=="Completo" or states[i]=="Disponible":
                if xesc[i]-100<=mx<=xesc[i]+100 and yesc[i]-100<=my<yesc[i]+100:
                    if countescotilla[i]<len(escotilla)-0.3:
                        countescotilla[i]+=0.3
                else:
                    if countescotilla[i]>0:
                        countescotilla[i]-=0.3
            mostrar(xesc[i],yesc[i],imgnvls[n[i]][i])
            mostrar(xesc[i],yesc[i],escotilla[int(countescotilla[i])])
        for i in range(15):
            if counts<360*np.pi:    
                counts+=1
            else:
                counts=0
            mostrar(xs[i],ys[i],S[est[i]],10*np.sin(counts/180))
        draw_txt("Niveles",font_1,(255,255,255),1280/2,100)
        boton_b=pantalla.blit(back,(50,630))
        if boton_b.collidepoint((mx,my)):
            pantalla.blit(bg_image,boton_b,boton_b)
            boton_b=pantalla.blit(back,(50,625))
            if k1==0:
                k1+=1
                canal1.play(tap)
            if click:
                #running=False
                print("volví al menú, creanme")
                #menu.main_menu()
                click=False
        else:
            k1=0
        p.display.update()
        clock.tick(60)
niveles()