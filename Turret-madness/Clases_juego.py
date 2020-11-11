import pygame as p
import random as r
import sys
p.init()
p.mixer.init()
font= p.font.Font('spacerunnertwoital.TTF',35)
font_3= p.font.Font('spacerunnertwoital.TTF',30)
font_1= p.font.Font('spacerunnertwoital.TTF',100)
font_2= p.font.Font('spacerunnertwoital.TTF',150)
clock=p.time.Clock()
size=width,height=1280,720
pantalla=p.display.set_mode(size)
bg_image=p.image.load("fondo-proyecto.png")
bg_image=bg_image.convert()
boton=p.image.load("boton.png")
back=p.image.load("flecha-regresar.png")
select=p.mixer.Sound('sonido_boton.mp3')
tap=p.mixer.Sound('boton_tap.mp3')
p.mixer.music.load("fondo.mp3")
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
    while running:
        if boton_1==None and boton_2==None and boton_3==None: 
            pantalla.blit(bg_image,(0,0))
            draw_txt("TURRET",font_2, (0,0,0),pantalla,385,65)
            draw_txt("TURRET",font_2, (255,255,255),pantalla,372,50)
            draw_txt("MADNESS",font_1, (0,0,0),pantalla,381,185)
            draw_txt("MADNESS",font_1, (255,255,255),pantalla,368,170)
        else:
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
            pantalla.blit(bg_image,boton_1,boton_1)
            boton_1=pantalla.blit(boton,(pos[0],pos[1]-5))
            draw_txt("JUGAR",font, (0,0,0),pantalla,580,303)
            draw_txt("JUGAR",font, (255,255,255),pantalla,578,300)
            canal1.play(tap)
            if click:
                canal2.play(select)
                game()
        if boton_2.collidepoint((mx,my)):
            pantalla.blit(bg_image,boton_2,boton_2)
            boton_2=pantalla.blit(boton,(pos[0],pos[1]+95))
            draw_txt("OPCIONES",font, (0,0,0),pantalla,554,403)
            draw_txt("OPCIONES",font, (255,255,255),pantalla,552,400)
            canal1.play(tap)
            if click:
                canal1.play(select)
                opciones()
        if boton_3.collidepoint((mx,my)):
            pantalla.blit(bg_image,boton_3,boton_3)
            boton_3=pantalla.blit(boton,(pos[0],pos[1]+195))
            draw_txt("CONTROLES",font_3, (0,0,0),pantalla,554,506)
            draw_txt("CONTROLES",font_3, (255,255,255),pantalla,552,503)
            canal1.play(tap)            
            if click: 
                canal1.play(select)
                controles()
        for event in p.event.get():
            if event.type==p.QUIT:
                running=False
                sys.exit()
            elif event.type==p.KEYDOWN:
                if event.key==p.K_ESCAPE:
                    running==False
            elif event.type==p.MOUSEBUTTONDOWN:
                if (event.button==1 and boton_1.collidepoint((mx,my))) or (event.button==1 and boton_2.collidepoint((mx,my))) or (event.button==1 and boton_3.collidepoint((mx,my))):
                    click=True
        p.display.update()
        clock.tick(60)
def opciones():
    running = True 
    click=False
    while running:
        pantalla.blit(bg_image,(0,0))
        draw_txt("opciones",font_1, (0,0,0),pantalla,343,83)
        draw_txt("opciones",font_1, (255,255,255),pantalla,330,80)
        mx,my=p.mouse.get_pos()
        boton_b=pantalla.blit(back,(50,630))
        if boton_b.collidepoint((mx,my)):
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
                if event.button==1 and boton_b.collidepoint((mx,my)):
                    click=True
        p.display.update()
        clock.tick(60)

def controles():
    running = True 
    click=False
    while running:
        pantalla.blit(bg_image,(0,0))
        draw_txt("CONTROLES",font_1, (0,0,0),pantalla,343,83)
        draw_txt("CONTROLES",font_1, (255,255,255),pantalla,330,80)
        mx,my=p.mouse.get_pos()
        boton_b=pantalla.blit(back,(50,630))
        if boton_b.collidepoint((mx,my)):
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
                if event.button==1 and boton_b.collidepoint((mx,my)):
                    click=True
        p.display.update()
        clock.tick(60)
        
def game():
    class Torreta:
        def __init__(self,x,y,salud,salud_total=1):
            self.x=int(x)
            self.y=int(y)
            self.salud=salud
            self.salud_total=salud_total
        def mostrar(self,img,i=0,di=0):
            if isinstance(img,int):
                return self
            else:
                if isinstance(img,list):
                    centro=img[i//di].get_rect(center=(self.x,self.y))
                    pantalla.blit(img[i//di],centro)
                else:
                    centro=img.get_rect(center=(self.x,self.y))
                    pantalla.blit(img,centro)
                return self
        def vida(self):
            p.draw.rect(pantalla,(255,0,0),(self.x-40,self.y-50,80,10))
            p.draw.rect(pantalla,(0,255,0),(self.x-40,self.y-50,int(80*self.salud/self.salud_total),10))
            return self
    class bala:
        def __init__(self,x,y,n):
            self.x=x
            self.x2=x
            self.y=y
            self.y2=y
            self.tipo=n
        def mostrar(self,img,a,l,colision=False):
            if l==0 or l==6:
                velbal=0
            elif l==1:
                velbal=4
            elif l==2:
                velbal=6
            elif l==3:
                velbal=8
            elif  l==4:
                velbal=10
            elif l==5:
                velbal=12
            else:
                velbal=0
            if self.x<=1280:
                self.x+=4*velbal
                centro=img.get_rect(center=(int(self.x),int(self.y)))
                pantalla.blit(img,centro)
            else:
                self.x=self.x2
            return self
    class Hand:
        def __init__(self, x , y):
            self.x=int(x)
            self.y=int(y)
        def mostrar(self,img,i=0,di=0,a=0):
            if isinstance(img,list):
                manita=p.transform.rotozoom(img[i//di],a,1)
                centro=manita.get_rect(center=(self.x,self.y))
                pantalla.blit(manita,centro)
            else:
                manita=p.transform.rotozoom(img,a,1)
                centro=manita.get_rect(center=(self.x,self.y))
                pantalla.blit(manita,centro)
            return self   
        def cuadrado(self):
            if self.y!=150:
                p.draw.rect(pantalla,(255,0,0),(self.x+25,self.y-40,80,80),4)
            else:
                p.draw.rect(pantalla,(255,0,0),(self.x-40,self.y-105,80,80),4)
            return self
        def select(self):
            return self.x+25,self.y-40,False
    class celda:
        def __init__(self,x,y,vacia=True):
            self.x=int(x)
            self.y=int(y)
            self.state=vacia
        def mostrar(self,img,salud=100,salud_total=1):
            if self.state:
                p.draw.rect(pantalla,(50,50,50),(self.x,self.y,80,80),4)
            else:
                PP=Torreta(self.x+40,self.y+40,salud,salud_total)
                PP.mostrar(img).vida()
            return self
    class enemigo:
        def __init__(self,x,y,vida,salud_total):
            self.x=x
            self.y=y
            self.v=vida
            self.salud_total=salud_total
        def mostrar(self,img,i=0,di=0):
            if isinstance(img,int):
                return self
            else:
                if isinstance(img,list):
                    centro=img[i//di].get_rect(center=(self.x,self.y))
                    pantalla.blit(img[i//di],centro)
                else:
                    centro=img.get_rect(center=(self.x,self.y))
                    pantalla.blit(img,centro)
                return self
        def vida(self):
            p.draw.rect(pantalla,(255,0,0),(self.x-40,self.y-50,80,10))
            p.draw.rect(pantalla,(0,255,0),(self.x-40,self.y-50,int(80*self.v/self.salud_total),10))
            return self
        def colision(self,o1,o2):
            if (o1.x-self.x)**2+(self.y-o1.y)**2<=50:
                return True
            else: 
                return False
            if o2.x-50<=self.x<=o2.x+50:
                return True
            else: 
                return False
    #Inicio de declaración de variables
    p.init()
    angulo=0
    salud=[]
    dinero=0
    xhand,yhand=50,150
    est=(0,0,0)
    est1=(0,0,0)
    pantalla=p.display.set_mode((1280,720))
    p.display.set_caption("Turret Madness")
    fondo=p.image.load("images\\Fondo.png").convert()
    cfondo=fondo.get_rect(center=(int(1280/2),int(720/2)))
    moverd,movera,moverr,moverl=False,False,False,False
    celdas=[]
    turrets=[]
    usable=[]
    balimg=[]
    vida=[100,200,300,400,500,600,800]
    vidturr=0
    vid=0
    #torretas
    for i in range(7):
        usable.append(False)
        turrets.append(p.image.load("images\\Torreta"+str(i)+".png"))
        if 0<=i<=2 or i==6:
            balimg.append(p.image.load("images\\Balas\\0.png"))
        else:
            balimg.append(p.image.load("images\\Balas\\"+str(i)+".png"))
    a=[]
    sal=[]
    balas=[]
    nb=-1
    turr=-1
    #Mano
    manoimg=p.image.load("images\\Mano.png")
    for i in range(75,976,150):
        for j in range(210,611,100):
            balas.append(bala(i+50,j+30,0))
            sal.append(0)
            sal.append(0)
            a.append(-1)
            a.append(0)
            celdas.append((i,j))
            celdas.append(celda(i,j,True))
    #Menú
    menu=[]
    mx=[90,240,390,540,690,840,990]
    for i in range(14):
        menu.append(p.image.load("images\\MenuT"+str(i)+".png"))
    #Aliens
    Alien1=[]
    Alien2=[]
    Alien3=[]
    Alien4=[]
    al=0
    x1,x2,x3,x4,y1,y2,y3,y4=1280,1280+100,1280+200,1280+300,240+r.randint(0,4)*100,240+r.randint(0,4)*100,240+r.randint(0,4)*100,240+r.randint(0,4)*100
    velx=2
    for i in range(4):
        Alien1.append(p.image.load("images\\Alien1"+str(i)+".png").convert_alpha())
        Alien2.append(p.image.load("images\\Alien2"+str(i)+".png").convert_alpha())
        Alien3.append(p.image.load("images\\Alien3"+str(i)+".png").convert_alpha())
        Alien4.append(p.image.load("images\\Alien4"+str(i)+".png").convert_alpha())
    #Pausa
    font=p.font.Font("Fuentes\\raidercrusadersemistraight.ttf",32)
    cp=0
    pause=False
    Pausado="PAUSA"
    color=1
    def Pause(a,color):
        hola=font.render(a,True,(color*255,color*255,color*255))
        cent=hola.get_rect(center=(int(1280/2),int(720/2)))
        pantalla.blit(hola,cent)
    pause=False
    Run=True
    while Run:
        for event in p.event.get():
            if event.type== p.QUIT:
                Run=False
                p.quit()
                sys.exit()
            if event.type==p.KEYDOWN:
                if event.key == p.K_s:
                    if not moverd:
                        moverd = True
                elif event.key == p.K_w:
                    if not movera:
                        movera = True
                elif event.key == p.K_a:
                    if not moverl:
                        moverl = True
                elif event.key == p.K_d:
                    if not moverr:
                        moverr = True
                elif event.key== p.K_RETURN:
                    est=mano.select()
                elif event.key== p.K_BACKSPACE:
                    est1=mano.select()
                elif event.key== p.K_ESCAPE:
                    pause=True
        pantalla.blit(fondo,cfondo)
        p.draw.rect(pantalla,(0,0,0),(75,150,1000,30))
        p.draw.rect(pantalla,(50,50,50),(80,155,990,20))
        p.draw.rect(pantalla,(143,49,255),(80,155,int(990*dinero/7000),20))
        if dinero<7000:
            dinero+=10
        for l in range(1,7):
            p.draw.rect(pantalla,(0,0,0),(int(80+990*l/7),155,5,20))
        for i in range(70):
            if i%2!=0:
                for j in range(7):
                    if (dinero-1000)/1000<j:
                        pantalla.blit(menu[j+7],(mx[j],45))
                        usable[j]=False
                    else:
                        usable[j]=True
                        pantalla.blit(menu[j],(mx[j],45))                
                    if est[0]-65==mx[j] and est[1]==110:
                        if usable[j]:
                            turr=turrets[j]
                            nb=j
                            vidturr=vida[j]
                            vid=vida[j]
                if a[i]!=-1:
                    balas[i//2].mostrar(balimg[a[i-1]],True,a[i-1])
                celdas[i].mostrar(a[i],salud[i],sal[i])         
            else:
                if est[0]==celdas[i][0] and est[1]==celdas[i][1]:
                    a[i+1]=turr
                    a[i]=nb
                    sal[i+1]=vidturr
                    salud[i+1]=vid
                    if a[i+1]!=-1 and a[i]!=-1:
                        dinero-=(nb+1)*1000
                        celdas[i+1]=celda(est[0],est[1],est[2])
                    vid=0
                    nb=-1
                    turr=-1
                    est=(0,0,0)
                elif est1[0]==celdas[i][0] and est1[1]==celdas[i][1]:
                    a[i+1]=-1
                    a[i]=-1
                    salud[i+1]=0
                    celdas[i+1]=celda(est1[0],est1[1],True)
                    est1=(0,0,0)
        #Mover la mano
        if moverd:
            yhand+=100
            moverd=False
        elif movera:
            yhand-=100
            movera=False
        elif moverl:
            xhand-=150
            moverl=False
        elif moverr:
            xhand+=150
            moverr=False
        if yhand<=150:
            angulo=90
            yhand=150
            mano=Hand(xhand+80,yhand)
        elif yhand>650:
            yhand=650
        else:
            mano=Hand(xhand,yhand)
            angulo=0
        if xhand<50:
            xhand=50
        elif xhand>950:
            xhand=950
        mano.mostrar(manoimg,0,0,angulo).cuadrado()
        if al<len(Alien1)-0.3:
            al+=0.3
        else:
            al=0
        en1,en2,en3,en4=enemigo(x1,y1,200,300),enemigo(x2,y2,200,300),enemigo(x3,y3,200,300),enemigo(x4,y4,200,300)
        en2.mostrar(Alien1[int(al)]).vida()
        en1.mostrar(Alien2[int(al)]).vida()
        en3.mostrar(Alien3[int(al)]).vida()
        en4.mostrar(Alien4[int(al)]).vida()
        x1-=velx
        x2-=velx
        x3-=velx
        x4-=velx
        if x2<=0:
            x2=1280
            y2=240+r.randint(0,4)*100
        if x1<=0:
            x1=1280
            y1=240+r.randint(0,4)*100
        if x3<=0:
            x3=1280
            y3=240+r.randint(0,4)*100
        if x4<=0:
            x4=1280
            y4=240+r.randint(0,4)*100
        while pause:
            if cp<=500:
                cp+=1
            else:
                cp=0
            if cp<=250:
                color=1
            else:
                color=0
            Pause(Pausado,color)
            for event in p.event.get():
                if event.type== p.QUIT:
                    pause=False
                    Run=False
                if event.type == p.KEYDOWN:
                    if event.key == p.K_ESCAPE:
                        if pause==True:
                            pause=False
            p.display.update()
        p.display.update()
main_menu()
