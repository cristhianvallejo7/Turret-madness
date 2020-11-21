import pygame as p
from pygame import mixer
import random as r
import sys
import math as m
import numpy as np
def game():
    Save=open("Save.txt","r")
    state1=Save.readline()
    st1=Save.readline()
    state2=Save.readline()
    st2=Save.readline()
    state3=Save.readline()
    st3=Save.readline()
    Save.close()
    countent=1
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
        def mostrar(self,img,a,l,colision1=False):
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
            if colision1:
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
        def colision1(self,kk,mm):
            if ((self.x-kk)**2+(self.y-mm)**2)<=30**2:
                return True
            else:
                return False
        def vida(self,daño=0):
            p.draw.rect(pantalla,(255,0,0),(self.x-40,self.y-50,80,10)) 
            if self.v>0:
                p.draw.rect(pantalla,(0,255,0),(self.x-40,self.y-50,int(80*self.v/self.salud_total),10))
            else:
                p.draw.rect(pantalla,(0,255,0),(self.x-40,self.y-50,0,10))
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
    p.display.set_caption("Tower-Madness")
    mixer.init()
    Aliensound=mixer.Sound("Sound\\Aliens.wav")
    soundselect=mixer.Sound("Sound\\select.wav")
    soundmano=mixer.Sound("Sound\\hand.wav")
    pausesound=mixer.Sound("Sound\\message.ogg")
    mixer.music.load("Sound\\alienblues.wav")
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)
    canalAliens=mixer.Channel(0)
    canalAliens.play(Aliensound,-1)
    canalselect=mixer.Channel(1)
    canalmano=mixer.Channel(2)
    canalpause=mixer.Channel(3)
    daño=[]
    clock=p.time.Clock()
    angulo=0
    salud=[]
    dinero=3000
    xhand,yhand=50,150
    est=(0,0,0)
    est1=(0,0,0)
    pantalla=p.display.set_mode((1280,720))
    p.display.set_caption("Turret Madness")
    fondo=p.image.load("images\\Fondo1.png").convert()
    cfondo=fondo.get_rect(center=(int(1280/2),int(720/2)))
    moverd,movera,moverr,moverl=False,False,False,False
    celdas=[]
    turrets=[]
    usable=[]
    balimg=[]
    vida=[1000,200,300,400,500,600,800]
    daño_enemigos=[1,2,3,4]
    vidturr=0
    vid=0
    a=[]
    sal=[]
    balas=[]
    nb=-1
    turr=-1
    superficies=[]
    #torretas
    for i in range(7):
        usable.append(False)
        turrets.append(p.image.load("images\\Torreta"+str(i)+".png"))
        if 0<=i<=2 or i==6:
            balimg.append(p.image.load("images\\Balas\\0.png"))
        else:
            balimg.append(p.image.load("images\\Balas\\"+str(i)+".png"))
    
    #Mano
    manoimg=p.image.load("images\\Mano.png")
    for i in range(75,976,150):
        for j in range(210,611,100):
            salud.append(0)
            salud.append(0)
            balas.append(bala(i+50,j+30,0))
            sal.append(0)
            sal.append(0)
            a.append(-1)
            a.append(-1)
            celdas.append((i,j))
            celdas.append(celda(i,j,True))
            superficies.append(p.Rect(i,j,80,80))

    #Menú
    menu=[]
    mx=[90,240,390,540,690,840,990]
    for i in range(14):
        menu.append(p.image.load("images\\MenuT"+str(i)+".png"))

    #Aliens
    Aliens=[]
    Alien1=[]
    Alien2=[]
    Alien3=[]
    Alien4=[]
    Alien1attack=[]
    Alien2attack=[]
    Alien3attack=[]
    Alien4attack=[]
    vel=[]
    enemigos=[]
    vidaenemigo=[]
    vidaenemigototal=[]
    al,al1=0,0
    X=[]
    Y=[]
    N=[]
    countenemigos=[]
    for i in range(4,11):
        Alien1attack.append(p.image.load("images\\Alien1"+str(i)+".png").convert_alpha())
        Alien2attack.append(p.image.load("images\\Alien2"+str(i)+".png").convert_alpha())
        Alien3attack.append(p.image.load("images\\Alien3"+str(i)+".png").convert_alpha())
        Alien4attack.append(p.image.load("images\\Alien4"+str(i)+".png").convert_alpha())
    for i in range(4):
        Alien1.append(p.image.load("images\\Alien1"+str(i)+".png").convert_alpha())
        Alien2.append(p.image.load("images\\Alien2"+str(i)+".png").convert_alpha())
        Alien3.append(p.image.load("images\\Alien3"+str(i)+".png").convert_alpha())
        Alien4.append(p.image.load("images\\Alien4"+str(i)+".png").convert_alpha())

    for i in range(7): #Esta variable controla el número de enemigos en el tablero
        vidaenemigo.append(200)
        vidaenemigototal.append(200)
        n=2
        N.append(n)
        Aliens.append(Alien2)
        vel.append(5)
        X.append(1280+i*1400+500)
        Y.append(240+r.randint(0,4)*100)
        countenemigos.append(0)
    for i in range(8):
        vidaenemigo.append(150)
        vidaenemigototal.append(150)
        n = 1
        N.append(n)
        Aliens.append(Alien1)
        vel.append(5)
        X.append(2200 + i * 1200+500)
        Y.append(240 + r.randint(0, 4) * 100)
        countenemigos.append(0)
    for i in range(4):
        vidaenemigo.append(200)
        vidaenemigototal.append(200)
        n=2
        N.append(n)
        Aliens.append(Alien2)
        vel.append(5)
        X.append(4280+i*1200+500)
        Y.append(240+r.randint(0,4)*100)
        countenemigos.append(0)
    for i in range(6):
        vidaenemigo.append(150)
        vidaenemigototal.append(150)
        n = 1
        N.append(n)
        Aliens.append(Alien1)
        vel.append(5)
        X.append(5000 + i * 1200+500)
        Y.append(240 + r.randint(0, 4) * 100)
        countenemigos.append(0)
    daño=np.zeros(len(N))
    
    #Nucleo
    pilar,cpilar=p.image.load("images\\Nucleo\\Pilar.png"),[]
    esfera=[]
    estadonucleo=[]
    nucleoimg=[]
    yn=[]
    xn=[]
    vn=[]
    countnucleo,countndest=0,[]
    destruir=[]
    cnucleo=[]
    for i in range(8):
        if i<5:
            destruir.append(p.image.load("images\\Nucleo\\D"+str(i)+".png"))
        nucleoimg.append(p.image.load("images\\Nucleo\\"+str(i)+".png"))
        esfera.append(p.image.load("images\\Nucleo\\E"+str(i)+".png"))
    for i in range(5):
        countndest.append(0)
        estadonucleo.append(0)
        xn.append(40)
        vn.append(10)
        yn.append(240+i*100)
        cpilar.append(nucleoimg[i].get_rect(center=(xn[i],yn[i])))
        cnucleo.append(nucleoimg[i].get_rect(center=(xn[i],yn[i])))

    #Guartado
    save=False

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
    fondoent=p.image.load("images\\fondo.png").convert()
    pause=False
    Run=True
    click=False
    while Run:
        casilla=False
        
        for event in p.event.get():
            if event.type== p.QUIT:
                Run=False
                p.quit()
                sys.exit()
            if event.type==p.KEYDOWN:
                if event.key == p.K_s or event.key == p.K_DOWN:
                    if not moverd:
                        moverd = True
                elif event.key == p.K_w or event.key == p.K_UP:
                    if not movera:
                        movera = True
                elif event.key == p.K_a or event.key == p.K_LEFT:
                    if not moverl:
                        moverl = True
                elif event.key == p.K_d or event.key == p.K_RIGHT:
                    if not moverr:
                        moverr = True
                elif event.key== p.K_RETURN:
                    est=mano.select()
                    canalselect.play(soundselect)
                elif event.key== p.K_BACKSPACE:
                    est1=mano.select()
                elif event.key== p.K_ESCAPE:
                    canalpause.play(pausesound)
                    pause=True
            elif event.type==p.MOUSEBUTTONDOWN:
                if event.button==1:
                    print("si")
                    click=True
                    est=mano.select()
                    canalselect.play(soundselect)
                if event.button==3:
                    est1=mano.select()
        Mx,My=p.mouse.get_pos()
        
        pantalla.blit(fondo,cfondo)
        p.draw.rect(pantalla,(0,0,0),(75,150,1000,30))
        p.draw.rect(pantalla,(50,50,50),(80,155,990,20))
        p.draw.rect(pantalla,(143,49,255),(80,155,int(990*dinero/7000),20))
        if dinero<3000:
            dinero+=50
        for l in range(1,7):
            p.draw.rect(pantalla,(0,0,0),(int(80+990*l/7),155,5,20))
        botones_menu=[]
        #Celdas y menú
        for i in range(70):
            if i%2!=0:
                for j in range(7):
                    if (dinero-1000)/1000<j:
                        botones_menu.append(pantalla.blit(menu[j+7],(mx[j],45)))
                        usable[j]=False
                    else:
                        usable[j]=True
                        botones_menu.append(pantalla.blit(menu[j],(mx[j],45)))            
                    if est[0]-65==mx[j] and est[1]==110:
                        if usable[j]:
                            turr=turrets[j]
                            nb=j
                            vidturr=vida[j]
                            vid=vida[j]   
                if a[i]!=-1:
                    balas[i//2].mostrar(balimg[a[i-1]],True,a[i-1])
                    for h in range(len(N)): 
                        if enemigos[h].colision1(balas[i//2].x,balas[i//2].y):
                            balas[i//2].mostrar(balimg[a[i-1]],False,a[i-1],True)
                            daño[h]+=10
                            if daño[h]>=vidaenemigototal[h]:
                                X[h]=5000
                                Y[h]=5000
                                daño[h]=0
                                countenemigos[h]=1
                celdas[i].mostrar(a[i],salud[i],sal[i])
            else:
                if (est[0]==celdas[i][0] and est[1]==celdas[i][1]):
                    if celdas[i+1].state:
                        a[i+1]=turr
                        a[i]=nb
                        sal[i+1]=vidturr
                        salud[i+1]=vid
                    if a[i+1]!=-1 and a[i]!=-1:
                        if not usable[nb]:
                            vid=0
                            nb=-1
                            turr=-1
                        if celdas[i+1].state:
                            dinero-=(nb+1)*1000
                            celdas[i+1]=celda(est[0],est[1],est[2])
                    est=(0,0,0)
                elif est1[0]==celdas[i][0] and est1[1]==celdas[i][1]:
                    a[i+1]=-1
                    a[i]=-1
                    salud[i+1]=0
                    celdas[i+1]=celda(est1[0],est1[1],True)
                    est1=(0,0,0)
                if celdas[i+1].state :
                    a[i+1]=-1
                    a[i]=-1
                    salud[i+1]=0
                    celdas[i+1]=celda(celdas[i][0],celdas[i][1],True)
                    
        #Nucleo
        if countnucleo<len(nucleoimg)-0.4:
            countnucleo+=0.4
        else:
            countnucleo=0
        for i in range(5):
            cnucleo[i]=nucleoimg[i].get_rect(center=(xn[i],yn[i]))
            if estadonucleo[i]==0:
                pantalla.blit(nucleoimg[int(countnucleo)],cnucleo[i])
                for k in range(len(Aliens)):
                    if abs(xn[i]-X[k])<40 and yn[i]==Y[k]:
                        estadonucleo[i]=1
            if estadonucleo[i]==1:
                for k in range(len(Aliens)):
                    if abs(xn[i]-X[k])<40 and yn[i]==Y[k]:
                        X[k]=1280+r.randint(0,len(Aliens))*100
                        Y[k]=240+r.randint(0,4)*100
                    if X[k]<20:
                        estadonucleo[i]=2
                pantalla.blit(pilar,cpilar[i])
                if xn[i]<1240:
                    xn[i]+=vn[i]
                    pantalla.blit(esfera[int(countnucleo)],cnucleo[i])
                else:
                    if countndest[i]<len(destruir)-0.2:
                        if xn[i]!=5000:
                            if countndest[i]<0.9:
                                countndest[i]+=0.1
                            else:
                                countndest[i]+=0.2
                            pantalla.blit(destruir[int(countndest[i])],cnucleo[i])
                    else:
                        xn[i],yn[i]=5000,5000
            if estadonucleo[i]==2:
                pantalla.blit(pilar,cpilar[i])
                print("Game over")
                estadonucleo[i]=3
        if movera or moverd or moverl or moverr:
            canalmano.play(soundmano)
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
        
        for i in range(7):
            if botones_menu[i].collidepoint((Mx,My)):
                xhand=mx[i]-40
                yhand=150
                casilla=True
            
        for i in range(35):
            if i%2==0:
                if superficies[i].collidepoint((Mx,My)):
                    xhand=celdas[i*2][0]-25
                    yhand=celdas[i*2][1]+40
          
            else:
                if superficies[i].collidepoint((Mx,My)):
                    xhand=celdas[i*2][0]-25
                    yhand=celdas[i*2][1]+40        
        if al<len(Alien1)-0.3:
            al+=0.3
        else:
            al=0
        if al1<len(Alien1attack)-0.15:
            al1+=0.15
        else:
            al1=0
        #este pedazo se encarga de mostrar los enemigos caminando
        enemigos=[]
        for i in range(len(Aliens)):
            enemigos.append(enemigo(X[i],Y[i],vidaenemigo[i]-daño[i],vidaenemigototal[i]))
            if vel[i]!=0:
                if -100<=X[i]<=1380:
                    X[i]-=vel[i]
                    enemigos[i].mostrar(eval("Aliens["+str(i)+"][int(al)]")).vida()
        if countenemigos.count(1)==len(N):
            countenemigos[0]=0
            save=True
        
        #Guardado
        if save:
            stars=estadonucleo.count(0)
            Save=open("Save.txt","w")
            Save.close()
            Save=open("Save.txt","a")
            Save.write("Completo\n")
            Save.write(str(stars)+"\n")
            Save.write("Disponible"+"\n")
            Save.write(st2)
            Save.write(state3)
            Save.write(st3)
            Save.close()
            save=False
            break

        #este pedazo se encarga de las colisiones
        for j in range(len(Aliens)):   
            for i in range(6,-1,-1):
                for k in range(1,10,2):
                    if m.sqrt((eval("X"+str([j]))-(185+i*150))**2+(eval("Y"+str([j]))-(celdas[int(str(i)+str(k))-1][1]))**2)<40:
                        if not celdas[int(str(i)+str(k))].state:
                            vel[j]=0
                            if N[j] == 1:
                                enemigos[j].mostrar(Alien1attack[int(al1)]).vida()
                                if salud[int(str(i)+str(k))]>=0:
                                    salud[int(str(i)+str(k))]-=daño_enemigos[N[j]-1]
                                else:
                                    salud[int(str(i)+str(k))]=0
                                    celdas[int(str(i)+str(k))].state=True
                            if N[j] == 2:
                                enemigos[j].mostrar(Alien2attack[int(al1)]).vida()
                                if salud[int(str(i)+str(k))]>=0:
                                    salud[int(str(i)+str(k))]-=daño_enemigos[N[j]-1]
                                else:
                                    salud[int(str(i)+str(k))]=0
                                    celdas[int(str(i)+str(k))].state=True
                            if N[j] == 3:
                                enemigos[j].mostrar(Alien3attack[int(al1)]).vida()
                                if salud[int(str(i)+str(k))]>=0:
                                    salud[int(str(i)+str(k))]-=daño_enemigos[N[j]-1]
                                else:
                                    salud[int(str(i)+str(k))]=0
                                    celdas[int(str(i)+str(k))].state=True
                            if N[j] == 4:
                                enemigos[j].mostrar(Alien4attack[int(al1)]).vida()
                                if salud[int(str(i)+str(k))]>=0: 
                                    salud[int(str(i)+str(k))]-=daño_enemigos[N[j]-1]
                                else:
                                    salud[int(str(i)+str(k))]=0
                                    celdas[int(str(i)+str(k))].state=True
                            PP=Torreta(celdas[int(str(i)+str(k))-1][0]+40,celdas[int(str(i)+str(k))-1][1]+40,salud[int(str(i)+str(k))],vida[a[int(str(i)+str(k))-1]])
                            PP.mostrar(turrets[a[int(str(i)+str(k))-1]]).vida()
                        else:
                            if X[j] <= 1500 and N[i] == 1:
                                vel[j] = 5
                            elif X[j] <= 1500 and N[i] == 2:
                                vel[j] = 3
                            if N[j]==1:
                                vel[j] = 5
                            elif N[j]==2:
                                vel[j] = 3
            X[j]-=vel[j]         
        
        if countent>0:
            countent-=0.05
            fondoent.set_alpha(int(countent*255))
            pantalla.blit(fondoent,(0,0))  
            
        #pausa
        while pause:
            mixer.music.pause()
            canalAliens.pause()
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
                            canalpause.play(pausesound)
                            mixer.music.unpause()
                            canalAliens.unpause()
                            pause=False
            clock.tick(60)
            p.display.update()
        clock.tick(60)
        p.display.update()
