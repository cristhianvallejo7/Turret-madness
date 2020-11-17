import pygame as p
import random as r
import sys
import math as m
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
    daño=[]
    angulo=0
    salud=[]
    dinero=7000
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
    vida=[100,200,300,400,500,600,800]
    vidturr=0
    vid=0
    a=[]
    sal=[]
    balas=[]
    nb=-1
    turr=-1
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
        daño.append(0)
        Aliens.append(Alien2)
        vel.append(5)
        X.append(1280+i*1400)
        Y.append(240+r.randint(0,4)*100)
    for i in range(8):
        vidaenemigo.append(150)
        vidaenemigototal.append(150)
        daño.append(0)
        n = 1
        N.append(n)
        Aliens.append(Alien1)
        vel.append(5)
        X.append(2200 + i * 1200)
        Y.append(240 + r.randint(0, 4) * 100)
    for i in range(4):
        vidaenemigo.append(200)
        vidaenemigototal.append(200)
        daño.append(0)
        n=2
        N.append(n)
        Aliens.append(Alien2)
        vel.append(5)
        X.append(4280+i*1200)
        Y.append(240+r.randint(0,4)*100)
    for i in range(6):
        daño.append(0)
        vidaenemigo.append(150)
        vidaenemigototal.append(150)
        n = 1
        N.append(n)
        Aliens.append(Alien1)
        vel.append(5)
        X.append(5000 + i * 1200)
        Y.append(240 + r.randint(0, 4) * 100)
        
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
        vn.append(5)
        yn.append(240+i*100)
        cpilar.append(nucleoimg[i].get_rect(center=(xn[i],yn[i])))
        cnucleo.append(nucleoimg[i].get_rect(center=(xn[i],yn[i])))

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
                elif event.key== p.K_BACKSPACE:
                    est1=mano.select()
                elif event.key== p.K_ESCAPE:
                    pause=True
        pantalla.blit(fondo,cfondo)
        p.draw.rect(pantalla,(0,0,0),(75,150,1000,30))
        p.draw.rect(pantalla,(50,50,50),(80,155,990,20))
        p.draw.rect(pantalla,(143,49,255),(80,155,int(990*dinero/7000),20))
        if dinero<7000:
            dinero+=20
        for l in range(1,7):
            p.draw.rect(pantalla,(0,0,0),(int(80+990*l/7),155,5,20))
        
        #Celdas y menú
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
                    for h in range(len(N)): 
                        if enemigos[h].colision1(balas[i//2].x,balas[i//2].y):
                            balas[i//2].mostrar(balimg[a[i-1]],False,a[i-1],True)
                            daño[h]+=10
                            if daño[h]>=vidaenemigototal[h]:
                                X[h]=1280
                                Y[h]=2400+r.randint(0,4)*100
                                daño[h]=0
                                enemigos[h]=enemigo(X[h],Y[h],200,300) 
                celdas[i].mostrar(a[i],salud[i],sal[i])
            else:
                if est[0]==celdas[i][0] and est[1]==celdas[i][1]:
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
        if al1<len(Alien1attack)-0.15:
            al1+=0.15
        else:
            al1=0
            
        #este pedazo se encarga de mostrar los enemigos caminando
        enemigos=[]
        for i in range(len(Aliens)):
            if vidaenemigo[i]==0:
                X[i]=1280
                Y[i]=240+r.randint(0,4)*100
                vidaenemigo[i]=200
            enemigos.append(enemigo(X[i],Y[i],vidaenemigo[i]-daño[i],vidaenemigototal[i]))
            if X[i]<=0:
                X[i]=1280+r.randint(0,len(Aliens))*100
                Y[i]=240+r.randint(0,4)*100
            if vel[i]!=0:
                X[i]-=vel[i]
                enemigos[i].mostrar(eval("Aliens["+str(i)+"][int(al)]")).vida() 
            
        #este pedazo se encarga de las colisiones
        for j in range(len(Aliens)):   
            for i in range(6,-1,-1):
                for k in range(1,10,2):
                    if m.sqrt((eval("X"+str([j]))-(185+i*150))**2+(eval("Y"+str([j]))-(celdas[int(str(i)+str(k))-1][1]))**2)<40:
                        if not celdas[int(str(i)+str(k))].state:
                            vel[j]=0
                            if N[j] == 1:
                                enemigos[j].mostrar(Alien1attack[int(al1)]).vida(vidaenemigo[N[j]])
                            if N[j] == 2:
                                enemigos[j].mostrar(Alien2attack[int(al1)]).vida(vidaenemigo[N[j]])
                            if N[j] == 3:
                                enemigos[j].mostrar(Alien3attack[int(al1)]).vida(vidaenemigo[N[j]])
                            if N[j] == 4:
                                enemigos[j].mostrar(Alien4attack[int(al1)]).vida(vidaenemigo[N[j]])
                        else:
                            if X[i] <= 1500 and N[i] == 1:
                                vel[j] = 5
                            if X[i] <= 1500 and N[i] == 2:
                                vel[j] = 3
                            if N[j]==1:
                                vel[j]=1
                            elif N[j]==2:
                                vel[j]=3
        #pausa
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
