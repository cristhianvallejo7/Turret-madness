import pygame as p
import random as r
#Código de Jh0mpis, derechos de autor piroos :v
#La idea es que pillen las ideas principales del código, no les recomiendo que copien y peguen el código porque no se entiende igual
class Torreta:
    def __init__(self,x,y,salud,salud_total=1):
        self.x=int(x)
        self.y=int(y)
        self.salud=salud
        self.salud_total=salud_total
    def mostrar(self,img,i=0,di=0):
        if isinstance(img,list):#Si es un Sprite lo carga
            centro=img[i//di].get_rect(center=(self.x,self.y))
            pantalla.blit(img[i//di],centro)
        else:#Sino carga una sola imagen
            centro=img.get_rect(center=(self.x,self.y))
            pantalla.blit(img,centro)
        return self
    def vida(self):#Muestra la vida que queda de la torreta
        p.draw.rect(pantalla,(255,0,0),(self.x-40,self.y-50,80,10))
        p.draw.rect(pantalla,(0,255,0),(self.x-40,self.y-50,int(80*self.salud/self.salud_total),10))
        return self
class bala:
    def __init__(self,x,y,n):
        self.x=x#Coordenada que voy a variar porque no supe como hacerla volver a un estado inicial :v
        self.x2=x#Coordenada inicial
        self.y=y#Coordenada que voy a variar porque no supe como hacerla volver a un estado inicial :v
        self.y2=y#Coordenada inicial
        self.tipo=n#Creo que con esto haré algo relacionado al poder que cada bala tendrá :v, aún está en construcción.
    def mostrar(self,img,a,l,colision=False):
        if l==0 or l==6:#l indica el tipo de torreta que hay en cada casilla.
            velbal=0#Si es una barrera no se mueve
        elif l==1:
            velbal=4#si es la primera torreta se mueve lento
        elif l==2:
            velbal=6#Si es la segunda se mueve más rápido
        elif l==3:
            velbal=8#Si es la tercera se mueve aún más rápido
        elif  l==4:
            velbal=10#Lo mismo de arriba :v
        elif l==5:
            velbal=12#x2
        else:
            velbal=0
        if self.x<=1280:#No le paren muchas bolas a esto, aún es experimental.
            self.x+=4*velbal#Mover la bala
            centro=img.get_rect(center=(int(self.x),int(self.y)))
            pantalla.blit(img,centro)
        else:
            self.x=self.x2 #Si la bala se sale de la pantalla o colisiona, la vuelve al inicio
        return self
class Hand:
    def __init__(self, x , y):
        self.x=int(x)
        self.y=int(y)
    def mostrar(self,img,i=0,di=0,a=0):
        if isinstance(img,list):#Muestra la mano
            manita=p.transform.rotozoom(img[i//di],a,1)#el rotozoom me deja rotar o agrandar la imagen
            centro=manita.get_rect(center=(self.x,self.y))
            pantalla.blit(manita,centro)
        else:
            manita=p.transform.rotozoom(img,a,1)
            centro=manita.get_rect(center=(self.x,self.y))
            pantalla.blit(manita,centro)
        return self   
    def cuadrado(self):
        if self.y!=150:#Muestra el cuadrado rojo :v
            p.draw.rect(pantalla,(255,0,0),(self.x+25,self.y-40,80,80),4)
        else:
            p.draw.rect(pantalla,(255,0,0),(self.x-40,self.y-105,80,80),4)
        return self
    def select(self):
        return self.x+25,self.y-40,False #Seleccionar casilla
class celda:
    def __init__(self,x,y,vacia=True):
        self.x=int(x)
        self.y=int(y)
        self.state=vacia
    def mostrar(self,img,salud=100,salud_total=1):
        if self.state:#Si está vacía muestre un cuadrado gris
            p.draw.rect(pantalla,(50,50,50),(self.x,self.y,80,80),4)
        else: #Sino muestre la torreta segun la img que tiene
            PP=Torreta(self.x+40,self.y+40,salud,salud_total)
            PP.mostrar(img).vida()
        return self
#Inicio de declaración de variables
p.init()#Inicializar el juego
p.mixer.init()
angulo=0
salud=100
dinero=7000
xhand,yhand=50,150#coordenadas iniciales de la mano
est=(0,0,0)#Estado para poner torreta
est1=(0,0,0)#Estado para quitar torreta
#pantalla=p.display.set_mode((1280,720))#Tamaño de la pantalla
size=width,height=1280,720
pantalla=p.display.set_mode(size)#de esta manera si usamos las variables de size se puede cambiar el tamaño de la pantalla sin modificar los números de abajo 
p.display.set_caption("Turret Madness")#Caption :v
fondo=p.image.load("images\\Fondo.png").convert()#cargar el fondo
cfondo=fondo.get_rect(center=(int(1280/2),int(720/2)))
moverd,movera,moverr,moverl=False,False,False,False#Detectar como se mueve la mano
celdas=[]
turrets=[]
usable=[]
balimg=[]
vida=[100,200,300,400,500,600,800]
vidturr=0
font= p.font.Font('spacerunnertwoital.TTF',35)#no supe si se puede cambiar el tamaño de la fuente así que llamé varias veces la misma para diferentes tamaños
font_3= p.font.Font('spacerunnertwoital.TTF',30)
font_1= p.font.Font('spacerunnertwoital.TTF',100)
font_2= p.font.Font('spacerunnertwoital.TTF',150)
clock=p.time.Clock()
#bg_image=p.image.load("fondo-proyecto.png")
boton=p.image.load("boton.png")
back=p.image.load("flecha-regresar.png")
select=p.mixer.Sound('sonido_boton.mp3')
tap=p.mixer.Sound('boton_tap.mp3')
p.mixer.music.load("fondo.mp3")
#p.mixer.music.play(-1)
canal1=p.mixer.Channel(0)
canal2=p.mixer.Channel(1)
#función que escribe cualquier texto
def draw_txt(texto, font, color, surface, x, y):
    textobj=font.render(texto, True, color)
    textrect=textobj.get_rect()
    textrect.topleft=( x, y)
    surface.blit(textobj,textrect)
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
turr=0
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
al=0
for i in range(4):
    Alien1.append(p.image.load("images\\Alien1"+str(i)+".png").convert_alpha())
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

def game():
    Run=True
    while Run:
        for event in p.event.get():
            if event.type== p.QUIT:
                Run=False
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
        for l in range(1,7):#Cargar la recta morada, la de las luKs
            p.draw.rect(pantalla,(0,0,0),(int(80+990*l/7),155,5,20))
        for i in range(70):#cargar las celdas
            if i%2!=0:
                for j in range(7):#Cargar el menú
                    if (dinero-1000)/1000<j:
                        pantalla.blit(menu[j+7],(mx[j],45))
                        usable[j]=False#Decir qué torretas no son usables
                    else:
                        usable[j]=True#Que torretas si lo son
                        pantalla.blit(menu[j],(mx[j],45))                
                    if est[0]-65==mx[j] and est[1]==110:
                        if usable[j]:
                            turr=turrets[j]#Guardar las torretas usables en una variable
                            nb=j#el tipo de bala
                            vidturr=vida[j]#La vida todal de la torreta J
                if a[i]!=0:
                    balas[i//2].mostrar(balimg[a[i-1]],True,a[i-1]) #Mostrar la bala si la torreta está puesta
                celdas[i].mostrar(a[i],salud,sal[i])         
            else:
                if est[0]==celdas[i][0] and est[1]==celdas[i][1]:#Mostrar dónde seleccionó la mano
                    a[i+1]=turr#Definir la torreta de la casilla
                    a[i]=nb#El tipo de bala en la casilla
                    sal[i+1]=vidturr#La vida de la torreta de la casilla
                    if a[i]!=-1:
                        dinero-=500#Si pone una torreta, la paga
                        celdas[i+1]=celda(est[0],est[1],est[2])#Poner la torreta
                    est=(0,0,0)#Reiniciar la selección 
                elif est1[0]==celdas[i][0] and est1[1]==celdas[i][1]:#Si quiere quitar la torreta, pues la quita :v
                    a[i+1]=0
                    a[i]=-1
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
        #Mostrar un alien en la mitad de la pantalla :v
        if al<len(Alien1)-0.1:
            al+=0.02
            pantalla.blit(Alien1[int(al)],(1280/2,720/2))
        else:
            al=0
        while pause:#La pausa :v
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
