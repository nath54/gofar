#coding:utf-8
import random,pygame,time
from pygame.locals import *
tex,tey=700,800
pygame.init()
fenetre=pygame.display.set_mode([tex,tey])
pygame.display.set_caption("GOFAR")
pygame.key.set_repeat(40,30)
font=pygame.font.SysFont("Serif",20)
fon2=pygame.font.SysFont("Sans",50)
#clock = pygame.time.Clock()

imgfond1=pygame.transform.scale(pygame.image.load("images/fond.png"),[tex,tey])
imgfond2=pygame.transform.scale(pygame.image.load("images/fond.png"),[tex,tey])
imgmeteor=pygame.image.load("images/meteor.png")
imgv=pygame.image.load("images/vaisseau.png")
imgven1=pygame.image.load("images/ven1.png")
imgb1=pygame.image.load("images/bonus1.png")
imgb2=pygame.image.load("images/bonus2.png")
imgb3=pygame.image.load("images/bonus3.png")
imgb4=pygame.image.load("images/bonus4.png")

bonuses=[["nb mis",1,imgb1],["speed mis",2,imgb2],["energy+",3,imgb3],["armure+",4,imgb4]]

##############Astéroide##############

class Meteor:
    def __init__(self,x,y,tx,ty,acc):
        self.px=x
        self.py=y
        self.tx=tx
        self.ty=ty
        self.acc=acc
        self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
        self.dbg=time.time()
        self.tbg=0.01
        self.destroy=False
        self.agl=random.randint(1,360)
        self.img=pygame.transform.rotate( pygame.transform.scale(imgmeteor,[self.tx,self.ty]) , self.agl )
    def vt(self,vr):
        if vr.colliderect(self.rect):
            return True
        else: return False

##############Missile##############

class Missil:
    def __init__(self,x,y,tx,ty,vitx,vity,dg,pos,tps,cl):
        self.px=x
        self.py=y
        self.tx=tx
        self.ty=ty
        self.vitx=vitx
        self.vity=vity
        self.dg=dg
        self.pos=pos
        self.tps=tps
        self.tim=time.time()
        self.destroy=False
        self.dbg=time.time()
        self.tbg=0.01
        self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
        self.cl=cl
    def update(self,asts,vaisseaux):
        if time.time()-self.dbg>=self.tbg:
            self.dbg=time.time()
            self.px+=self.vitx
            self.py+=self.vity
        for a in asts:
            if self.rect.colliderect(a.rect):
                self.destroy=True
                a.destroy=True
        for v in vaisseaux:
            if not self.destroy and v.tp!=self.pos:
                if self.rect.colliderect(v.rect):
                    v.armure-=self.dg
                    if self.pos==0:
                        v.ddg=time.time()
                    self.destroy=True
        if time.time()-self.tim>=self.tps:
            self.destroy=True

##############vaisseau##############

class Vaisso:
    def __init__(self,x,y):
        self.tp=1
        self.vie=5
        self.armure_tot=100
        self.armure=self.armure_tot
        self.vit=5
        self.px=x
        self.py=y
        self.tx=70
        self.ty=70
        self.acc=1.0
        self.mdg=10
        self.mtx=3
        self.mty=6
        self.mvitx=0
        self.mvity=-20
        self.mcl=(0,255,250)
        self.mtps=7
        self.mce=5
        self.dtir=time.time()
        self.ttir=0.5
        self.nbmis=1
        self.img=pygame.transform.scale(imgv,[self.tx,self.ty])
        self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
        self.dbg=time.time()
        self.tbg=0.01
        self.ddg=time.time()
        self.trarm=10
        self.energy_tot=2000
        self.energy=self.energy_tot
        self.tremp=2
    def bouger(self,aa,mis):
        if time.time()-self.dbg>=self.tbg:
            self.dbg=time.time()
            if aa == "Up":
                if self.py>0:
                    self.py-=self.vit
            elif aa == "Down":
                if self.py+self.ty<tey:
                    self.py+=self.vit
            elif aa == "Left":
                if self.px>0:
                    self.px-=self.vit
            elif aa == "Right":
                if self.px<tex-self.tx:
                    self.px+=self.vit
        if aa=="Tir":
            if time.time()-self.dtir>=self.ttir and self.energy>self.mce:
                self.dtir=time.time()
                self.energy-=self.mce
                if self.nbmis==1:
                    mis.append(Missil(self.px+self.tx/2,self.py+self.ty/2,self.mtx,self.mty,0,self.mvity,self.mdg,1,self.mtps,self.mcl))
                elif self.nbmis==2:
                    mis.append(Missil(self.px+self.tx/4,self.py+self.ty/2,self.mtx,self.mty,-1,self.mvity,self.mdg,1,self.mtps,self.mcl))
                    mis.append(Missil(self.px+self.tx/4*3,self.py+self.ty/2,self.mtx,self.mty,1,self.mvity,self.mdg,1,self.mtps,self.mcl))
                elif self.nbmis==3:
                    mis.append(Missil(self.px+self.tx/4,self.py+self.ty/2,self.mtx,self.mty,-1,self.mvity,self.mdg,1,self.mtps,self.mcl))
                    mis.append(Missil(self.px+self.tx/2,self.py+self.ty/2,self.mtx,self.mty,0,self.mvity,self.mdg,1,self.mtps,self.mcl))
                    mis.append(Missil(self.px+self.tx/4*3,self.py+self.ty/2,self.mtx,self.mty,1,self.mvity,self.mdg,1,self.mtps,self.mcl))
                elif self.nbmis==4:
                    mis.append(Missil(self.px+self.tx/4*0,self.py+self.ty/2,self.mtx,self.mty,-2,self.mvity,self.mdg,1,self.mtps,self.mcl))
                    mis.append(Missil(self.px+self.tx/4*1,self.py+self.ty/2,self.mtx,self.mty,-1,self.mvity,self.mdg,1,self.mtps,self.mcl))
                    mis.append(Missil(self.px+self.tx/4*3,self.py+self.ty/2,self.mtx,self.mty,1,self.mvity,self.mdg,1,self.mtps,self.mcl))
                    mis.append(Missil(self.px+self.tx/4*4,self.py+self.ty/2,self.mtx,self.mty,2,self.mvity,self.mdg,1,self.mtps,self.mcl))
                else:
                    mis.append(Missil(self.px+self.tx/4*0,self.py+self.ty/2,self.mtx,self.mty,-2,self.mvity,self.mdg,1,self.mtps,self.mcl))
                    mis.append(Missil(self.px+self.tx/4*1,self.py+self.ty/2,self.mtx,self.mty,-1,self.mvity,self.mdg,1,self.mtps,self.mcl))
                    mis.append(Missil(self.px+self.tx/4*2,self.py+self.ty/2,self.mtx,self.mty,0,self.mvity,self.mdg,1,self.mtps,self.mcl))
                    mis.append(Missil(self.px+self.tx/4*3,self.py+self.ty/2,self.mtx,self.mty,1,self.mvity,self.mdg,1,self.mtps,self.mcl))
                    mis.append(Missil(self.px+self.tx/4*4,self.py+self.ty/2,self.mtx,self.mty,2,self.mvity,self.mdg,1,self.mtps,self.mcl))
        return mis


class Vsen1:
    def __init__(self):
        self.tp=0
        self.tx=50
        self.ty=50
        self.px=random.randint(self.tx,tex-self.tx)
        self.py=random.randint(-tey,0)
        self.img=pygame.transform.scale(imgven1,[self.tx,self.ty])
        self.vit=5
        self.acc=2
        self.dbg=time.time()
        self.tbg=0.01
        self.dtr=time.time()
        self.ttr=0.5
        self.dg=1
        self.cl=(250,0,100)
        self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
        self.armure_tot=25
        self.armure=self.armure_tot
    def tirer(self,mis):
        if time.time()-self.dtr >= self.ttr:
            self.dtr=time.time()
            mis.append( Missil(self.px+23/2,self.py+60/2,3/2,8,0,10,self.dg,0,6,self.cl) )
            #mis.append( Missil(self.px+33/2,self.py+60/2,3/2,5,0,10,self.dg,0,5,self.cl) )
            #mis.append( Missil(self.px+67/2,self.py+60/2,3/2,5,0,10,self.dg,0,5,self.cl) )
            mis.append( Missil(self.px+77/2,self.py+60/2,3/2,8,0,10,self.dg,0,6,self.cl) )
    def bouger(self,mis):
        if time.time()-self.dbg>=self.tbg:
            self.dbg=time.time()
            self.px+=random.randint(-self.vit,self.vit)
            self.py+=self.acc
            if self.px<0: self.px=0
            if self.px>tex-self.tx: self.px=tex-self.tx
            self.tirer(mis)

class Bonus:
    def __init__(self,acc):
        bn=bonuses[random.choice([0,1,1,1,2,2,2,2,3,3,3,3])]
        self.nom=bn[0]
        self.effet=bn[1]
        self.tx=30
        self.ty=30
        self.px=random.randint(self.tx,tex-self.tx)
        self.py=random.randint(-tey,0)
        self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
        self.img=pygame.transform.scale(bn[2],[self.tx,self.ty])
        self.acc=acc
        self.destroy=False
        self.dbg=time.time()
        self.tbg=0.01
    def update(self,vaisseau):
        if time.time()-self.dbg>=self.tbg:
            self.py+=self.acc
        if not self.destroy and self.rect.colliderect(vaisseau.rect):
            if self.effet==1:
                if vaisseau.nbmis<5: vaisseau.nbmis+=1
            elif self.effet==2:
                if vaisseau.ttir>0.01: vaisseau.ttir-=0.01
            elif self.effet==3:
                vaisseau.energy+=200
                if vaisseau.energy>vaisseau.enregy_tot: vaisseau.energy=vaisseau.energy_tot
            elif self.effet==4:
                vaisseau.armure+=50
                if vaisseau.armure>vaisseau.armure_tot: vaisseau.armure=vaisseau.armure_tot
            self.destroy=True
    
##############affichage##############

def aff(fps,vaisseau,mis,meter,fn1y,fn2y,score,vens,pause,bonus):
    if not pause:
        fenetre.blit( imgfond1 , [0,fn1y] )
        fenetre.blit( imgfond2 , [0,fn2y] )
        for m in mis:
            m.rect=pygame.draw.rect(fenetre,m.cl,(m.px,m.py,m.tx,m.ty),0)
        for b in bonus:
            if b.px>=0-b.tx and b.px <= tex+b.tx and b.py>=0-b.ty and b.py <= tey+b.ty:
                b.rect=fenetre.blit( b.img , [b.px,b.py] )
        for m in meter:
            if m.px>=0-m.tx and m.px <= tex+m.tx and m.py>=0-m.ty and m.py <= tey+m.ty:
                m.rect=fenetre.blit( m.img , [m.px,m.py] )
        for v in vens:
            if v.px>=0-v.tx and v.px <= tex+v.tx and v.py>=0-v.ty and v.py <= tey+v.ty:
                v.rect=fenetre.blit( v.img, [v.px,v.py] )
        vaisseau.rect=fenetre.blit( vaisseau.img , [vaisseau.px,vaisseau.py] )
        fenetre.blit(font.render("score = "+str(int(score)),20,(210,210,250)) , [5,10] )
        fenetre.blit(font.render("vies = "+str(vaisseau.vie),20,(210,210,250)) , [5,30] )
        fenetre.blit(font.render("vitesse = "+str(vaisseau.acc)[:3],20,(210,210,250)) , [5,50] )
        fenetre.blit(font.render("fps = "+str(fps),20,(210,210,250)) , [5,70] )
    else:
        fenetre.blit(fon2.render("PAUSE, press 'p' to play",20,(250,210,200)) , [20,tey/2] )
    varm=float(vaisseau.armure)/float(vaisseau.armure_tot)
    vener=float(vaisseau.energy)/float(vaisseau.energy_tot)
    ety=tey-50
    pygame.draw.rect(fenetre,(0,255,250),(tex-25,10+ety-int(vener*ety),20,int(vener*ety)),0)
    pygame.draw.rect(fenetre,(0,55,50),(tex-25,10,20,tey-50),2)
    pygame.draw.rect(fenetre,(30+int(varm*40),0,0+int(varm*250.)),(10,tey-20,int(varm*(tex-20.)),15),0)
    pygame.draw.rect(fenetre,(0,0,0),(10,tey-20,(tex-20),15),2)
    pygame.display.update()
    pygame.display.flip()

##############gestion du jeu##############

def bbb(score,vaer,fn1y,fn2y,mis,vaisseau,meter,limm,vens,nben,taugen,daugen,pause,bonus):
    score+=vaisseau.acc
    #meter
    for m in meter:
        if time.time()-m.dbg>=m.tbg:
            m.py+=m.acc
            if m.py >= tey and m in meter: del(meter[meter.index(m)])
            if m.vt(vaisseau.rect):
                vaisseau.armure-=1./float(m.tx+m.ty)*100
                vaisseau.ddg=time.time()
                if m in meter: del(meter[meter.index(m)])
            if m.destroy: #x,y,tx,ty,acc
                if m.tx>=20 and m.ty>=20:
                    meter.append( Meteor(m.px-random.randint(0,m.tx),m.py+random.randint(-m.ty,m.ty),random.randint(int(m.tx/4),int(m.tx/1.5)),random.randint(int(m.ty/4),int(m.ty/1.5)),random.randint(1,m.acc+1)) )
                    meter.append( Meteor(m.px+random.randint(0,m.tx),m.py+random.randint(-m.ty,m.ty),random.randint(int(m.tx/4),int(m.tx/1.5)),random.randint(int(m.ty/4),int(m.ty/1.5)),random.randint(1,m.acc+1)) )
                if m in meter: del(meter[meter.index(m)])
    while len(meter)<=limm:
        meter.append( Meteor(random.randint(0,tex),random.randint(-tey,0),random.randint(15,50),random.randint(15,40),random.randint(int(vaisseau.acc)-1,int(vaisseau.acc)+2)) )
    #vens
    while len(vens)<nben:
        vens.append( Vsen1() )
    for v in vens:
        v.bouger(mis)
        if v.armure<=0:
            del(vens[vens.index(v)])
            score+=100*nben*vaisseau.acc
        if v.py>=tey:
            if v in vens: del(vens[vens.index(v)])
    if time.time()-daugen>=taugen:
        daugen=time.time()
        if nben<5: nben+=1
    #bonus
    if time.time()-dbn>=tbn: bonus.append( Bonus(vaisseau.acc) )
    for b in bonus:
        if not b.destroy and b.py<tey:
            b.update(vaisseau)
        else:
            if b in bonus: del(bonus[bonus.index(b)])
    #mis
    vaisseaux=[vaisseau]+vens
    for m in mis:
        if not m.destroy:
            m.update(meter,vaisseaux)
        else: del(mis[mis.index(m)])
    #vaisseau
    if vaisseau.armure<vaisseau.armure_tot and time.time()-vaisseau.ddg>=vaisseau.trarm: vaisseau.armure+=1
    if vaisseau.armure<=0:
        vaisseau.vie-=1
        vaisseau.armure=vaisseau.armure_tot
    if time.time()-vaisseau.dtir >= vaisseau.tremp and vaisseau.energy<vaisseau.energy_tot: vaisseau.energy+=0.5
    vaer+=0.005
    if vaer>=1:
        vaisseau.acc+=0.1
        vaer=0
    #fond
    fn1y+=float(float(vaisseau.acc)/2.0)
    fn2y+=float(float(vaisseau.acc)/2.0)
    if fn1y >= tey: fn1y=-tey
    if fn2y >= tey: fn2y=-tey
    return score,vaer,fn1y,fn2y,mis,vaisseau,meter,vens,nben,taugen,daugen,bonus
    

def verif_key(vaisseau,mis):
    keys=pygame.key.get_pressed()
    if keys[K_UP]: vaisseau.bouger("Up",mis)
    if keys[K_DOWN]: vaisseau.bouger("Down",mis)
    if keys[K_LEFT]: vaisseau.bouger("Left",mis)
    if keys[K_RIGHT]: vaisseau.bouger("Right",mis)
    if keys[K_SPACE]: vaisseau.bouger("Tir",mis)

##########################################################################

##############mainjeu##############

def main_jeu():
    vaisseau=Vaisso(tex/2,tey/2)
    fn1y=0
    fn2y=-tey
    encour=True
    fps=0
    limm=10
    nben=1
    taugen=25
    daugen=time.time()
    vaer=0
    tbn=5
    dbn=time.time()
    meter=[]
    mis=[]
    vens=[]
    bonus=[]
    score=0
    pause=False
    while encour:
        t1=time.time()
        aff(fps,vaisseau,mis,meter,fn1y,fn2y,score,vens,pause,bonus)
        score,vaer,fn1y,fn2y,mis,vaisseau,meter,vens,nben,taugen,daugen,bonus=bbb(score,vaer,fn1y,fn2y,mis,vaisseau,meter,limm,vens,nben,taugen,daugen,pause,bonus)
        verif_key(vaisseau,mis)
        for event in pygame.event.get():
            if event.type==QUIT: encour=False
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE: encour=False
                elif event.key==K_p:
                    pause=not pause
                    time.sleep(0.5)
        t2=time.time()
        tt=float(t2)-float(t1)
        if tt!=0:
            fps=int(1.0/float(tt))
        
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


#######menu

def main_menu():
    encourme=True
    bts=[None]
    fenetre.blit(imgfond1,[0,0])
    bts[0]=pygame.draw.rect(fenetre,(200,200,20),(200,400,200,100),0)
    fenetre.blit(font.render("play",20,(250,0,0)),[])
    pygame.display.update()
    while encourme:
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE: encourme=False
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                for b in bts:
                    if b!=None and b.collidepoint(pos):
                        di=bts.index(b)
                        if di==0:
                            main_jeu()










main_jeu()

