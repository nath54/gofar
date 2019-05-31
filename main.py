#coding:utf-8
import random,pygame,time
from pygame.locals import *
tex,tey=700,800
pause=False
meter=[]
score=0
fn1y=0
fn2y=-tey
pygame.init()
fenetre=pygame.display.set_mode([tex,tey])
pygame.display.set_caption("GOFAR")
pygame.key.set_repeat(40,30)
#clock = pygame.time.Clock()
class Vaisso:
    def __init__(self,x,y):
        self.vie=5
        self.vit=10
        self.px=x
        self.py=y
        self.fx=x
        self.fy=y
        self.tx=70
        self.ty=70
        self.acc=1.0
    def bouger(self,aa):
        if aa == "Up":
            if self.py>0:
                self.py-=self.vit
                self.fy-=self.vit
        elif aa == "Down":
            if self.py<tey:
                self.py+=self.vit
                self.fy+=self.vit
        elif aa == "Left":
            if self.px>0:
                self.px-=self.vit
                self.fx-=self.vit
        elif aa == "Right":
            if self.px<tex-self.tx:
                self.px+=self.vit
                self.fx+=self.vit
vaisseau=Vaisso(tex/2,tey/2)
class Meteor:
    def __init__(self,x,y,tx,ty,acc):
        self.px=x
        self.py=y
        self.fx=x
        self.fy=y
        self.tx=tx
        self.ty=ty
        self.acc=acc
    def vt(self,vr):
        if vr.colliderect(pygame.Rect(self.fx,self.fy,self.tx,self.ty)):
            return True
        else: return False
font=pygame.font.SysFont("Serif",20)
fon2=pygame.font.SysFont("Sans",50)
imgfond1=pygame.transform.scale(pygame.image.load("images/fond.png"),[tex,tey])
imgfond2=pygame.transform.scale(pygame.image.load("images/fond.png"),[tex,tey])
imgmeteor=pygame.image.load("images/meteor.png")
imgvaisseau=pygame.transform.scale(pygame.image.load("images/vaisseau.png"),[vaisseau.tx,vaisseau.ty])
def aff(fps):
    if not pause:
#        fenetre.fill((0,0,0))
        fenetre.blit( imgfond1 , [0,fn1y] )
        fenetre.blit( imgfond2 , [0,fn2y] )
        for m in meter:
            if m.fx>=0-m.tx and m.fx <= tex+m.tx and m.fy>=0-m.ty and m.fy <= tey+m.ty:
                fenetre.blit( pygame.transform.scale(imgmeteor,[m.tx,m.ty]) , [m.fx,m.fy] )
        fenetre.blit( imgvaisseau , [vaisseau.fx,vaisseau.fy] )
        fenetre.blit(font.render("score = "+str(int(score)),20,(210,210,250)) , [5,10] )
        fenetre.blit(font.render("vies = "+str(vaisseau.vie),20,(210,210,250)) , [5,30] )
        fenetre.blit(font.render("vitesse = "+str(vaisseau.acc)[:3],20,(210,210,250)) , [5,50] )
        fenetre.blit(font.render("fps = "+str(fps),20,(210,210,250)) , [5,70] )
    else:
        fenetre.blit(fon2.render("PAUSE, press 'p' to play",20,(250,210,200)) , [tex/3,tey/2] )
    pygame.display.update()
    pygame.display.flip()
limm=15
vaer=0
def bbb(score):
    global vaer,fn1y,fn2y
    score+=vaisseau.acc
    vrr=pygame.Rect(vaisseau.fx,vaisseau.fy,vaisseau.tx,vaisseau.ty)
    for m in meter:
        m.py+=m.acc
        m.fy+=m.acc
        if m.fy >= tey: del(meter[meter.index(m)])
        if m.vt(vrr):
            vaisseau.vie-=1
            del(meter[meter.index(m)])
    while len(meter)<=limm:
        meter.append( Meteor(random.randint(0,tex),random.randint(-tey,0),random.randint(15,50),random.randint(15,40),random.randint(int(vaisseau.acc)-1,int(vaisseau.acc)+2)) )
    vaer+=0.01
    if vaer>=1:
        vaisseau.acc+=0.1
        vaer=0
    fn1y+=float(float(vaisseau.acc)/2.0)
    fn2y+=float(float(vaisseau.acc)/2.0)
    if fn1y >= tey: fn1y=-tey
    if fn2y >= tey: fn2y=-tey
    return score
##########################################################################
encour=True
fps=0
while encour:
    t1=time.time()
    for event in pygame.event.get():
        if event.type==QUIT: encour=False
        elif event.type==KEYDOWN:
            if event.key==K_a: encour=False
            if event.key==K_q: encour=False
            elif event.key==K_p: pause=not pause
            elif event.key==K_UP:   vaisseau.bouger("Up")
            elif event.key==K_DOWN: vaisseau.bouger("Down")
            elif event.key==K_LEFT: vaisseau.bouger("Left")
            elif event.key==K_RIGHT:vaisseau.bouger("Right")
    t2=time.time()
    tt=float(t2)-float(t1)
    if tt!=0:
        fps=int(1.0/float(tt))
    aff(fps)
    score=bbb(score)
    if vaisseau.vie<=0: encour=False
encour2=False
if vaisseau.vie<=0:
    encour2=True
fenetre.blit(font.render("VOUS ETES MORT",20,(210,100,250)) , [tex/3,tey/2] )
fenetre.blit(font.render("score = "+str(int(score)),20,(100,210,250)) , [tex/3,tey/2+100] )
fenetre.blit(font.render("APPUYEZ SUR 'q' pour quitter",20,(210,210,100)) , [tex/3,tey/2+200] )
pygame.display.update()
while encour2:
    for event in pygame.event.get():
        if event.type==QUIT: encour2=False
        elif event.type==KEYDOWN:
            if event.key==K_a: encour2=False
            if event.key==K_q: encour2=False
