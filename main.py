#coding:utf-8
import random,pygame,time,os
from pygame.locals import *
tex,tey=700,800
pygame.init()
fenetre=pygame.display.set_mode([tex,tey])
pygame.display.set_caption("GOFAR")
font=pygame.font.SysFont("Serif",20)
font1=pygame.font.SysFont("Serif",30)
fon2=pygame.font.SysFont("Sans",50)
#clock = pygame.time.Clock()

imgfond1=pygame.transform.scale(pygame.image.load("images/fond.png"),[tex,tey])
imgfond2=pygame.transform.scale(pygame.image.load("images/fond.png"),[tex,tey])
imgmeteor=pygame.image.load("images/meteor.png")
imgven0=pygame.image.load("images/ven0.png")
imgven1=pygame.image.load("images/ven1.png")
imgven2=pygame.image.load("images/ven2.png")
imgven3=pygame.image.load("images/ven3.png")
imgven4=pygame.image.load("images/ven4.png")
imgven5=pygame.image.load("images/ven5.png")
imgven6=pygame.image.load("images/ven6.png")
imgboss1=pygame.image.load("images/boss1.png")
imgboss2=pygame.image.load("images/boss2.png")
imgb1=pygame.image.load("images/bonus1.png")
imgb2=pygame.image.load("images/bonus2.png")
imgb3=pygame.image.load("images/bonus3.png")
imgb4=pygame.image.load("images/bonus4.png")


musiques=["through_space.ogg","ObservingTheStar.ogg","OutThere.ogg","space.mp3","Industria.mp3","Fly_1.mp3","Fly.mp3","Industria_1.mp3"]
musiques_menu=["menu_sci-fi.ogg","menu_sci-fi1.ogg"]
dmus="musiques/"
dimg="images/"
sons=["proj1.ogg"]

bonuses=[["nb mis",1,imgb1],["speed mis",2,imgb2],["energy+",3,imgb3],["armure+",4,imgb4]]

venstps=[]
venstps.append( [30 ,30 ,imgven0 ,3  ,1    ,0.01 ,0.75 ,1    ,(250,0,100) ,25  ,10    ,1    ,2    ,8    ,1] )
venstps.append( [30 ,30 ,imgven0 ,4  ,1.25 ,0.01 ,0.70 ,3    ,(250,0,100) ,35  ,11    ,1    ,2    ,8    ,1] )
venstps.append( [40 ,40 ,imgven1 ,5  ,1.35 ,0.01 ,0.70 ,2    ,(250,0,100) ,35  ,12    ,2    ,2    ,8    ,1] )
venstps.append( [40 ,40 ,imgven1 ,6  ,1.40 ,0.01 ,0.65 ,4    ,(250,0,100) ,50  ,13    ,2    ,2    ,8    ,1] )
venstps.append( [50 ,50 ,imgven2 ,7  ,1.5  ,0.01 ,0.65 ,3    ,(250,0,100) ,50  ,14    ,4    ,2    ,8    ,1] )
venstps.append( [50 ,50 ,imgven2 ,8  ,1.65 ,0.01 ,0.50 ,5    ,(250,0,100) ,60  ,15    ,4    ,2    ,8    ,1] )
venstps.append( [60 ,60 ,imgven3 ,9  ,1.75 ,0.01 ,0.50 ,4    ,(250,0,100) ,60  ,16    ,6    ,2    ,8    ,1] )
venstps.append( [60 ,60 ,imgven3 ,10 ,1.95 ,0.01 ,0.50 ,6    ,(250,0,100) ,70  ,17    ,6    ,2    ,8    ,1] )
venstps.append( [70 ,70 ,imgven4 ,11 ,2.05 ,0.50 ,0.60 ,10   ,(0,200,0)   ,80  ,22    ,2    ,1    ,6    ,0.5] )
venstps.append( [70 ,70 ,imgven5 ,12 ,2.10 ,0.50 ,0.60 ,11   ,(0,235,0)   ,90  ,23    ,4    ,1    ,6    ,0.5] )
venstps.append( [70 ,70 ,imgven6 ,10 ,2.00 ,0.50 ,0.60 ,16   ,(0,255,0)   ,100 ,20    ,2    ,5    ,8    ,0.5] )
#                tx ,ty ,image   ,vit,acc  ,tbg  ,ttir ,dgts ,clmis       ,vie ,vitmis,nbmis,txmis,tymis,tpsmis

bosstps=[]
bosstps.append( [200 ,200 ,imgboss1 ,5   ,0   ,0.01 ,2      ,50   ,(250,200,0)      ,1000  ,8      ,1     ,7     ,14     ,2] )
bosstps.append( [200 ,200 ,imgboss1 ,6   ,0   ,0.01 ,2      ,50   ,(250,200,0)      ,2000  ,10     ,2     ,7     ,14     ,2] )
bosstps.append( [200 ,200 ,imgboss1 ,7   ,0   ,0.01 ,1.5    ,50   ,(250,200,0)      ,3000  ,12     ,2     ,7     ,14     ,2] )
bosstps.append( [200 ,200 ,imgboss1 ,5   ,0   ,0.01 ,2      ,50   ,(250,200,0)      ,4000  ,8      ,3     ,7     ,14     ,2] )
bosstps.append( [200 ,200 ,imgboss1 ,6   ,0   ,0.01 ,2      ,50   ,(250,200,0)      ,5000  ,10     ,3     ,7     ,14     ,2] )
bosstps.append( [200 ,200 ,imgboss1 ,7   ,0   ,0.01 ,1.5    ,50   ,(250,200,0)      ,6000  ,12     ,4     ,7     ,14     ,2] )
bosstps.append( [200 ,200 ,imgboss2 ,7   ,0   ,0.01 ,0.5    ,10   ,(135, 12, 122)   ,8000  ,5      ,1     ,10    ,35     ,2] )
bosstps.append( [200 ,200 ,imgboss2 ,7   ,0   ,0.01 ,0.45   ,10   ,(135, 12, 122)   ,9000  ,5      ,1     ,10    ,35     ,2] )
bosstps.append( [200 ,200 ,imgboss2 ,7   ,0   ,0.01 ,0.4    ,10   ,(135, 12, 122)   ,10000 ,5      ,1     ,10    ,35     ,2] )

#                tx  ,ty  ,image    ,vit ,acc  ,tbg ,ttir   ,dgts ,clmis            ,vie   ,vitmis ,nbmis ,txmis ,tymis  ,tpsmis

vanzeta=["vaisseau6-1.png","vaisseau6-2.png","vaisseau6-3.png","vaisseau6-4.png","vaisseau6-5.png","vaisseau6-6.png","vaisseau6-7.png","vaisseau6-8.png","vaisseau6-9.png","vaisseau6-10.png","vaisseau6-11.png"]

vaisseauxtps=[]
vaisseauxtps.append( ["alpha-0"         ,70   ,70  ,["vaisseau.png"] ,3     ,100         ,1000        ,5               ,1            ,5                ,0.5                ,0.1                    ,5         ,0            ,2      ,6     ,-20      ,1      ,1               ,0.01             ,False              ,"proj1.wav" ,1               ,[(0,250,200)]] )
vaisseauxtps.append( ["alpha-1"         ,70   ,70  ,["vaisseau7.png"],5     ,100         ,2000        ,10              ,1            ,7                ,0.5                ,0.05                   ,6         ,1000         ,2      ,6     ,-20      ,1      ,1               ,0.01             ,False              ,"proj1.wav" ,1               ,[(0,200,150)]] )
vaisseauxtps.append( ["alpha-10"        ,70   ,70  ,["vaisseau8.png"],5     ,110         ,2500        ,15              ,2            ,10               ,0.7                ,0.01                   ,6         ,5000         ,2      ,7     ,-20      ,1      ,1               ,0.01             ,False              ,"proj1.wav" ,1               ,[(0,0,250)]] )
vaisseauxtps.append( ["france-ship"     ,80   ,80  ,["vaisseau1.png"],5     ,150         ,5000        ,20              ,3            ,3                ,0.2                ,0.001                  ,10        ,200000       ,6      ,14    ,-15      ,1      ,1               ,0.05             ,True               ,"proj1.wav" ,1               ,[(255,0,0),(0,148,255),(255,255,255)]] )
vaisseauxtps.append( ["russian-ship"    ,80   ,80  ,["vaisseau2.png"],5     ,200         ,5000        ,30              ,1            ,1                ,0.7                ,0.1                    ,7         ,200000       ,100    ,20    ,-7       ,3      ,3               ,0.03             ,True               ,"proj1.wav" ,1               ,[(255,0,0),(255,255,255),(0,148,255)]] )
vaisseauxtps.append( ["beta-5"          ,100  ,100 ,["vaisseau5.png"],5     ,200         ,100000      ,10              ,1            ,1                ,0.                 ,0.                     ,7         ,1000000      ,20     ,40    ,-40      ,0.5    ,1               ,0.01             ,False              ,None        ,1               ,[(250,0,0)]] )
vaisseauxtps.append( ["zeta-100"        ,80   ,80  ,vanzeta          ,7     ,500         ,5000        ,50              ,3            ,15               ,0.2                ,0.01                   ,9         ,1000000000   ,2      ,6     ,-20      ,1      ,1               ,0.01             ,False              ,"proj1.wav" ,1               ,[(250,0,0)]] )
vaisseauxtps.append( ["el destructor"   ,100  ,100 ,["vaisseau3.png"],10    ,1000        ,10000000    ,100             ,10           ,20               ,0.1                ,0.01                   ,12        ,1000000000000,5      ,5     ,-20      ,1      ,1               ,0.01             ,False              ,"proj1.wav" ,1               ,[(250,0,0)]] )
vaisseauxtps.append( ["le vaisseau éco+",70   ,70  ,["vaisseau4.png"],1     ,60          ,100         ,1               ,1            ,3                ,0.6                ,0.1                    ,3         ,0            ,5      ,5     ,-10      ,1.5    ,2               ,0.05             ,False              ,"proj1.wav" ,2               ,[(200,250,0)]] )
#                    0=nom              1=tx 2=ty 3=img            4=vies 5=armure_tot 6=energy_tot 7=missile degats 8=nb missiles 9=nb missiles max 10=vitesse missiles 11=vitesse missiles max 12=vitesse ,13=prix       ,14=mtx ,15=mty,16=vitmis,17=mtps,18=nb mis/valve ,19=tps/mis/valve ,20=cl importantes  ,21=sound   ,22=frome mis      ,23=couleurs

cl=[250,0,0]
for x in range(250*3):
    if x/250<1:
        cl[0]-=1
        cl[1]+=1
    elif x/250<2:
        cl[1]-=1
        cl[2]+=1
    else:
        cl[2]-=1
        cl[0]+=1
    vaisseauxtps[5][23].append(tuple(cl))
    vaisseauxtps[6][23].append(tuple(cl))
    vaisseauxtps[7][23].append(tuple(cl))


from os.path import expanduser
home = expanduser("~")
dre="Gofar/"
if not dre[:-1] in os.listdir(home):
    os.mkdir(home+"/"+dre)

dire=home+"/"+dre

fs="stats.nath"
if not fs in os.listdir(dire):
    f=open(dire+fs,"w")
    f.close()

cac="#"
cacc="|"
ccac="-"

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
    def __init__(self,x,y,tx,ty,vitx,vity,dg,pos,tps,cl,forme):
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
        self.forme=forme
    def update(self,asts,vaisseaux):
        if not self.destroy:
            if time.time()-self.dbg>=self.tbg:
                self.dbg=time.time()
                self.px+=self.vitx
                self.py+=self.vity
            for a in asts:
                if self.rect.colliderect(a.rect):
                    self.destroy=True
                    a.destroy=True
            for v in vaisseaux:
                if v.tp!=self.pos:
                    if self.rect.colliderect(v.rect):
                        v.armure-=self.dg
                        if v.tp==1:
                            v.ddg=time.time()
                            if time.time()-v.ddg>v.tpsmaxsanssubirdg: v.tpsmaxsanssubirdg=time.time()-v.ddg
                        self.destroy=True
            if time.time()-self.tim>=self.tps:
                self.destroy=True

##############vaisseau##############

class Vaisso:
    def __init__(self,tp):
        vtp=vaisseauxtps[tp]
        self.tp=1
        self.vie_tot=vtp[4]
        self.vie=self.vie_tot
        self.armure_tot=vtp[5]
        self.armure=self.armure_tot
        self.vit=vtp[12]
        self.px=tex/2
        self.py=tey/2
        self.tx=vtp[1]
        self.ty=vtp[2]
        self.acc=1.0
        self.mdg=vtp[7]
        self.mtx=vtp[14]
        self.mty=vtp[15]
        self.mvitx=0
        self.mvity=vtp[16]
        self.isclimpmortant=vtp[20]
        self.mcls=vtp[23]
        self.formemis=vtp[22]
        self.dcl=0
        self.mtps=vtp[17]
        self.mce=5
        self.nbmpv=vtp[18]
        self.dtir=time.time()
        self.ttir=vtp[10]
        self.maxttir=vtp[11]
        self.amttir=0
        self.amttirmax=int((self.ttir-self.maxttir)/0.01)
        self.nbmis=vtp[8]
        self.maxnbmis=vtp[9]
        self.amdg=0
        self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
        self.dbg=time.time()
        self.tbg=0.01
        self.ddg=time.time()
        self.trarm=10
        self.dapespace=time.time()
        self.energy_tot=vtp[6]
        self.energy=self.energy_tot
        self.tremp=0.5
        self.ennemistues=0
        self.bosstues=0
        self.score=0
        self.distance_parcourue=0
        self.niveaux_finis=-1
        self.tpsmaxsanstirer=0
        self.tpsmaxsanssubirdg=0
        self.nbregenenergy=0
        self.nbregenarmure=0
        self.argent=0
        self.imgs=[]
        for i in vtp[3]:
            self.imgs.append( pygame.transform.scale(pygame.image.load(dimg+i),[self.tx,self.ty]) )
        self.an=0
        self.dan=time.time()
        self.tan=0.1
        self.image=self.imgs[self.an]
        self.dmv=time.time()
        self.tpspmispvalve=vtp[19]
        self.mpva=0
        self.soundeffect=vtp[21]
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
            self.dapespace=time.time()
            if time.time()-self.dtir>=self.ttir:
                self.mpva=0
                if self.isclimpmortant: self.dcl=0
            if (time.time()-self.dtir>=self.ttir or self.mpva<self.nbmpv) and self.energy>self.mce:
                if time.time()-self.dtir>self.tpsmaxsanstirer: self.tpsmaxsanstirer=time.time()-self.dtir
                self.dtir=time.time()
                if self.mpva<self.nbmpv and time.time()-self.dmv>=self.tpspmispvalve:
                    if self.soundeffect!=None:
                        try:
                            effect = pygame.mixer.Sound(dmus+self.soundeffect)
                            effect.play()
                        except: pass
                    self.mpva+=1
                    self.dmv=time.time()
                    self.energy-=self.mce
                    mil=int(self.nbmis/2.)
                    divtx=self.nbmis+1
                    for x in range(self.nbmis):
                        self.dcl+=1
                        if self.dcl>=len(self.mcls): self.dcl=0
                        mis.append(Missil(  self.px+self.tx/divtx*(x+1)-self.mtx/2 , self.py-self.mty  ,self.mtx,self.mty,x-mil,self.mvity,self.mdg,1,self.mtps,self.mcls[self.dcl],self.formemis))
        return mis

class Vsen:
    def __init__(self,vtp):
        self.tp,self.tx,self.ty=0,vtp[0],vtp[1]
        self.px=random.randint(self.tx,tex-self.tx)
        self.py=random.randint(-tey,0)
        self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
        self.img=pygame.transform.scale(vtp[2],[self.tx,self.ty])
        self.vit,self.acc=vtp[3],vtp[4]
        self.dbg,self.tbg=time.time(),vtp[5]
        self.dtr,self.ttr=time.time(),vtp[6]
        self.dg=vtp[7]
        self.cl=vtp[8]
        self.armure_tot=vtp[9]
        self.armure=self.armure_tot
        self.mvit=vtp[10]
        self.nbmis=vtp[11]
        self.mtx=vtp[12]
        self.mty=vtp[13]
        self.mtps=vtp[14]
    def tirer(self,mis):
        if time.time()-self.dtr >= self.ttr:
            self.dtr=time.time()
            mil=int(self.nbmis/2.)
            divtx=self.nbmis+1
            for x in range(self.nbmis):
                mis.append( Missil( self.px+self.tx/divtx*(x+1) , self.py+self.ty/2  , self.mtx , self.mty , 0 , self.mvit , self.dg , 0 , self.mtps , self.cl ,1))
    def bouger(self,mis,vaisseau):
        if time.time()-self.dbg>=self.tbg:
            self.dbg=time.time()
            self.px+=random.randint(-self.vit,self.vit)
            self.py+=self.acc
            if self.px<0: self.px=0
            if self.px>tex-self.tx: self.px=tex-self.tx
            self.tirer(mis)

class Boss:
    def __init__(self,tp):
        vtp=tp
        self.tp,self.tx,self.ty=2,vtp[0],vtp[1]
        self.px=random.randint(self.tx,tex-self.tx)
        self.py=random.randint(0,tey/5)
        self.rect=pygame.Rect(self.px,self.py,self.tx,self.ty)
        self.img=pygame.transform.scale(vtp[2],[self.tx,self.ty])
        self.vit,self.acc=vtp[3],vtp[4]
        self.dbg,self.tbg=time.time(),vtp[5]
        self.dtr,self.ttr=time.time(),vtp[6]
        self.dg=vtp[7]
        self.cl=vtp[8]
        self.armure_tot=vtp[9]
        self.armure=self.armure_tot
        self.mvit=vtp[10]
        self.nbmis=vtp[11]
        self.mtx=vtp[12]
        self.mty=vtp[13]
        self.mtps=vtp[14]
    def tirer(self,mis):
        if time.time()-self.dtr >= self.ttr:
            self.dtr=time.time()
            mil=int(self.nbmis/2.)
            divtx=self.nbmis+1
            for x in range(self.nbmis):
                mis.append( Missil( self.px+self.tx/divtx*(x+1) , self.py+self.ty/2  , self.mtx , self.mty , x-mil , self.mvit , self.dg , 2 , self.mtps , self.cl ,1))
    def bouger(self,mis,vaisseau):
        if time.time()-self.dbg>=self.tbg:
            self.dbg=time.time()
            if vaisseau.px>self.px: depx=self.vit
            else: depx=-self.vit
            self.px+=depx
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
                if vaisseau.nbmis<vaisseau.maxnbmis: vaisseau.nbmis+=1
                else:
                    vaisseau.amdg+=1
                    vaisseau.mdg+=1
            elif self.effet==2:
                if vaisseau.ttir>vaisseau.maxttir:
                    vaisseau.ttir-=0.01
                    vaisseau.amttir+=1
                else:
                    vaisseau.amdg+=1
                    vaisseau.mdg+=1
            elif self.effet==3:
                vaisseau.energy+=200
                if vaisseau.energy>vaisseau.energy_tot: vaisseau.energy=vaisseau.energy_tot
            elif self.effet==4:
                vaisseau.armure+=50
                if vaisseau.armure>vaisseau.armure_tot: vaisseau.armure=vaisseau.armure_tot
            self.destroy=True
    
##############affichage##############

def aff(fps,vaisseau,mis,meter,fn1y,fn2y,score,vens,pause,bonus,nv,nben):
    if not pause:
        fenetre.blit( imgfond1 , [0,fn1y] )
        fenetre.blit( imgfond2 , [0,fn2y] )
        for m in mis:
            if m.forme==1: m.rect=pygame.draw.rect(fenetre,m.cl,(m.px,m.py,m.tx,m.ty),0)
            elif m.forme==2:
                m.rect=pygame.draw.ellipse(fenetre,m.cl,(m.px,m.py,m.tx,m.ty),0)
        for b in bonus:
            if b.px>=0-b.tx and b.px <= tex+b.tx and b.py>=0-b.ty and b.py <= tey+b.ty:
                b.rect=fenetre.blit( b.img , [b.px,b.py] )
        for m in meter:
            if m.px>=0-m.tx and m.px <= tex+m.tx and m.py>=0-m.ty and m.py <= tey+m.ty:
                m.rect=fenetre.blit( m.img , [m.px,m.py] )
        for v in vens:
            if v.px>=0-v.tx and v.px <= tex+v.tx and v.py>=0-v.ty and v.py <= tey+v.ty:
                v.rect=fenetre.blit( v.img, [v.px,v.py] )
                if v.tp==2:
                    if v.armure>0: pygame.draw.rect(fenetre,(250,0,0),(150,15,int(v.armure/v.armure_tot*(tex-250)),20),0)
                elif v.tp==0:
                    if v.armure>0: pygame.draw.rect(fenetre,(250,0,0),(v.px,v.py-5,int(v.armure/v.armure_tot*v.tx),3),0)
            #else: v.rect=pygame.Rect(v.px,v.py,v.tx,v.ty)
        vaisseau.rect=fenetre.blit( vaisseau.image , [vaisseau.px,vaisseau.py] )
        fenetre.blit(font.render("distance parcourue = "+str(int(vaisseau.distance_parcourue))+"m",20,(210,210,250)) , [5,10] )
        fenetre.blit(font.render("score = "+str(int(score)),20,(210,210,250)) , [5,30] )
        fenetre.blit(font.render("vies = "+str(vaisseau.vie),20,(210,210,250)) , [5,50] )
        fenetre.blit(font.render("vitesse = "+str(vaisseau.acc)[:3],20,(210,210,250)) , [5,70] )
        fenetre.blit(font.render("fps = "+str(fps)+" Hz",20,(210,210,250)) , [5,90] )
        fenetre.blit(font.render("vitesse tir = "+str(vaisseau.amttir)+"/"+str(vaisseau.amttirmax),20,(210,210,250)) , [5,110] )
        txtm="nb missiles = "+str(vaisseau.nbmis)+"/"+str(vaisseau.maxnbmis)+" ( +"+str(vaisseau.amdg)+"dg)"
        fenetre.blit(font.render(txtm,20,(210,210,250)) , [5,130] )
        fenetre.blit(font.render("nb ennemis = "+str(int(nben)),20,(210,210,250)) , [5,150] )
        fenetre.blit(font.render("niveau = "+str(int(nv)),20,(210,210,250)) , [5,180] )
    else:
        fenetre.blit(fon2.render("PAUSE, appuyez 'p' pour jouer",20,(250,210,200)) , [20,tey/2] )
    
    vener=float(vaisseau.energy)/float(vaisseau.energy_tot)
    ety=tey-50
    pygame.draw.rect(fenetre,(0,255,250),(tex-25,10+ety-int(vener*ety),10,int(vener*ety)),0)
    pygame.draw.rect(fenetre,(0,55,50),(tex-25,10,10,tey-50),2)
    if vaisseau.armure>0: 
        varm=float(vaisseau.armure)/float(vaisseau.armure_tot)
        vvie=float(vaisseau.vie)/float(vaisseau.vie_tot)
        pygame.draw.rect(fenetre,(30+int(vvie*40),0,0+int(vvie*250.)),(10,tey-20,int(varm*(tex-20.)),15),0)
        pygame.draw.rect(fenetre,(0,0,0),(10,tey-20,(tex-20),15),2)
    pygame.display.update()
    pygame.display.flip()

##############gestion du jeu##############

def bbb(score,vaer,fn1y,fn2y,mis,vaisseau,meter,limm,vens,nben,taugen,daugen,pause,bonus,dbn,tbn,nv):
    score+=vaisseau.acc
    vaisseau.score=score
    vaisseau.distance_parcourue+=vaisseau.acc
    vaisseaux=[vaisseau]+vens
    #meter
    for m in meter:
        if time.time()-m.dbg>=m.tbg:
            m.py+=m.acc
            if m.py >= tey and m in meter: del(meter[meter.index(m)])
            for v in vaisseaux:
                if m.vt(v.rect):
                    v.armure-=1./float(m.tx+m.ty)*150
                    if v.tp==1: v.ddg=time.time()
                    if v.tp==1 and time.time()-v.ddg>v.tpsmaxsanssubirdg: v.tpsmaxsanssubirdg=time.time()-v.ddg
                    if m in meter: del(meter[meter.index(m)])
            if m.destroy: #x,y,tx,ty,acc
                if m.tx>=20 and m.ty>=20:
                    meter.append( Meteor(m.px-random.randint(0,m.tx),m.py+random.randint(-m.ty,m.ty),random.randint(int(m.tx/4),int(m.tx/1.5)),random.randint(int(m.ty/4),int(m.ty/1.5)),random.randint(1,m.acc+1)) )
                    meter.append( Meteor(m.px+random.randint(0,m.tx),m.py+random.randint(-m.ty,m.ty),random.randint(int(m.tx/4),int(m.tx/1.5)),random.randint(int(m.ty/4),int(m.ty/1.5)),random.randint(1,m.acc+1)) )
                if m in meter: del(meter[meter.index(m)])
    while len(meter)<=limm:
        meter.append( Meteor(random.randint(0,tex),random.randint(-tey,0),random.randint(15,50),random.randint(15,40),random.randint(int(vaisseau.acc)-1,int(vaisseau.acc)+2)) )
    #vens
    while len(vens)<nben and time.time()-daugen<taugen:
        if nv<len(venstps):
            vens.append( Vsen(venstps[nv]) )
        else:
            vv=Vsen(venstps[len(venstps)-1])
            vv.vie+=(len(venstps)-1-nv)*5
            vv.dg+=(len(venstps)-1-nv)
            vens.append( vv )
    for v in vens:
        v.bouger(mis,vaisseau)
        if v.armure<=0:
            del(vens[vens.index(v)])
            if v.tp==0:
                score+=250*nben*vaisseau.acc
                vaisseau.ennemistues+=1
            elif v.tp==2:
                score+=2500*vaisseau.acc
                vaisseau.bosstues+=1
        if v.py>=tey:
            if v in vens: del(vens[vens.index(v)])
    if time.time()-daugen>=taugen and len(vens)==0:
        daugen=time.time()
        if nben<5: nben+=1
        else:
            if nv<len(bosstps):
                vens.append( Boss(bosstps[nv]) )
            else:
                bb=Boss( bosstps[len(bosstps)-1] )
                bb.armure+=(len(bosstps)-1-nv)*2000
                bb.armure_tot+=(len(bosstps)-1-nv)*2000
                bb.nbmis+=(len(bosstps)-1-nv)
                vens.append( bb ) 
            nv+=1
            nben=0
    #bonus
    if time.time()-dbn>=tbn:
        dbn=time.time()
        bonus.append( Bonus(vaisseau.acc) )
    for b in bonus:
        if not b.destroy and b.py<tey:
            b.update(vaisseau)
        else:
            if b in bonus: del(bonus[bonus.index(b)])
    #mis
    for m in mis:
        if not m.destroy:
            m.update(meter,vaisseaux)
        else: del(mis[mis.index(m)])
    #vaisseau
    if vaisseau.armure<vaisseau.armure_tot and time.time()-vaisseau.ddg>=vaisseau.trarm: vaisseau.armure+=1
    if vaisseau.armure<=0:
        vaisseau.vie-=1
        vaisseau.armure=vaisseau.armure_tot
    if time.time()-vaisseau.dapespace >= vaisseau.tremp and vaisseau.energy<vaisseau.energy_tot: vaisseau.energy+=1
    vaer+=0.001
    if vaer>=1.:
        if vaisseau.acc<25.: vaisseau.acc+=0.1
        vaer=0.
    if len(vaisseau.imgs)>1 and time.time()-vaisseau.dan>=vaisseau.tan:
        vaisseau.dan=time.time()
        vaisseau.an+=1
        if vaisseau.an>=len(vaisseau.imgs): vaisseau.an=0
        vaisseau.image=vaisseau.imgs[vaisseau.an]
    #fond
    fn1y+=float(float(vaisseau.acc)/2.0)
    fn2y+=float(float(vaisseau.acc)/2.0)
    if fn1y >= tey: fn1y=-tey
    if fn2y >= tey: fn2y=-tey
    return score,vaer,fn1y,fn2y,mis,vaisseau,meter,vens,nben,taugen,daugen,bonus,dbn,nv

def verif_key(vaisseau,mis):
    keys=pygame.key.get_pressed()
    if keys[K_UP]: vaisseau.bouger("Up",mis)
    if keys[K_DOWN]: vaisseau.bouger("Down",mis)
    if keys[K_LEFT]: vaisseau.bouger("Left",mis)
    if keys[K_RIGHT]: vaisseau.bouger("Right",mis)
    if keys[K_SPACE]: vaisseau.bouger("Tir",mis)

##########################################################################


##############mainjeu##############

def main_jeu(tpv):
    #fond
    fn1y=0
    fn2y=-tey
    #vaisseau
    vaisseau=Vaisso(tpv)
    vaer=0
    #meteor
    limm=10
    meter=[]
    #ven
    nben=1
    taugen=20
    daugen=time.time()
    nv=0
    vens=[]
    #bonus
    tbn=10
    dbn=time.time()
    bonus=[]
    #mis
    mis=[]
    #main
    score=0
    fps=0
    pause=False
    encour=True
    pygame.mixer.music.load(dmus+random.choice(musiques))
    pygame.mixer.music.play(-1)
    while encour:
        t1=time.time()
        aff(fps,vaisseau,mis,meter,fn1y,fn2y,score,vens,pause,bonus,nv,nben)
        if not pause: score,vaer,fn1y,fn2y,mis,vaisseau,meter,vens,nben,taugen,daugen,bonus,dbn,nv=bbb(score,vaer,fn1y,fn2y,mis,vaisseau,meter,limm,vens,nben,taugen,daugen,pause,bonus,dbn,tbn,nv)
        verif_key(vaisseau,mis)
        for event in pygame.event.get():
            if event.type==QUIT: encour=False
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE: encour=False
                elif event.key==K_p:
                    vaisseau.ddg=time.time()
                    pause=not pause
        t2=time.time()
        tt=float(t2)-float(t1)
        if tt!=0:
            fps=int(1.0/float(tt))
        
        if vaisseau.vie<=0: encour=False
    vaisseau.niveaux_finis=nv-1
    encour2=True
    vaisseau.argent=10*vaisseau.ennemistues+50*vaisseau.bosstues+int(vaisseau.score/10000)
    fenetre.blit(font.render("VOUS ETES MORT",20,(210,100,250)) , [tex/3,tey/2] )
    fenetre.blit(font.render("score = "+str(int(score)),20,(100,210,250)) , [tex/3,tey/2+100] )
    fenetre.blit(font1.render("Vous avez gagné = "+str(int(vaisseau.argent))+"argent",20,(255,255,255)) , [tex/3,tey/2+200] )
    fenetre.blit(font.render("APPUYEZ SUR 'ESPACE' POUR QUITTER",20,(210,210,100)) , [tex/3,tey/2+300] )
    pygame.display.update()
    while encour2:
        for event in pygame.event.get():
            if event.type==QUIT: encour2=False
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE: encour2=False
                if event.key==K_SPACE: encour2=False
    return vaisseau

##########################################################

missions=[]
missions.append([10000,"parcourir "," m au total",10,0])
missions.append([100,"tuer "," ennemis au total",10,0])
missions.append([20,"tuer "," boss au total",10,0])
missions.append([100000,"dépasser "," points en une partie",10,0])
missions.append([30,"ne pas tirer pendant "," sec en une partie",10,0])
missions.append([30,"ne pas subir de dégats pendant "," sec en une partie",10,0])
missions.append([0,"finir le niveau "," en une partie",10,0])
missions.append([1,"avoir "," améliorations sur le nombre de missiles en une partie",10,0])
missions.append([1,"avoir "," améliorations sur la vitesse des missiles en une partie",10,0])
missions.append([1,"avoir "," regénération d'energie en une partie",10,0])
missions.append([1,"avoir "," regénération d'armure en une partie",10,0])
#0=valeur 1=texte1 2=texte2 3=recompense 4=nb etapes faites

#afftexte(texte1+str(valeur)+texte2)

class Joueur:
    def __init__(self):
        self.distanceparcourue=0
        self.distancemaxparcourue=0
        self.distanceparcourue_tot=0
        self.score=0
        self.scoremax=0
        self.score_tot=0
        self.ennemis_tues=0
        self.ennemis_tues_max=0
        self.ennemis_tues_tot=0
        self.boss_tues=0
        self.boss_tues_max=0
        self.boss_tues_tot=0
        self.argent=0
        self.tpsmaxsanstirer=0
        self.tpsmaxsanssubirdg=0
        self.niveaumaxfini=-1
        self.niveaufini=-1
        self.nbmaxamnbmis=0
        self.nbmaxvitmis=0
        self.nbmaxregenenergy=0
        self.nbmaxregenarmure=0
        self.vaisseauchoisi=0
        self.vaisseauxacquis=[0]
        self.nbfaitmission1=0
        self.nbfaitmission2=0
        self.nbfaitmission3=0
        self.nbfaitmission4=0
        self.nbfaitmission5=0
        self.nbfaitmission6=0
        self.nbfaitmission7=0
        self.nbfaitmission8=0
        self.nbfaitmission9=0
        self.nbfaitmission10=0
        self.nbfaitmission11=0
        self.vaisseaux_possedes=[0]

def loadj(missions):
    joueur=Joueur()
    if fs in os.listdir(dire) and len(open(dire+fs,"r").read())>1:
        f=open(dire+fs,"r").read().split(cac)
        print(f)
        if len(f)>0:
            if True: joueur.distancemaxparcourue=float(f[0])
            else: pass
        if len(f)>1:
            if True: joueur.distanceparcourue_tot=float(f[1])
            else: pass
        if len(f)>2:
            if True: joueur.scoremax=float(f[2])
            else: pass
        if len(f)>3:
            if True: joueur.score_tot=float(f[3])
            else: pass
        if len(f)>4:
            if True: joueur.ennemis_tues_max=float(f[4])
            else: pass
        if len(f)>5:
            if True: joueur.ennemis_tues_tot=float(f[5])
            else: pass
        if len(f)>6:
            if True: joueur.boss_tues_max=float(f[6])
            else: pass
        if len(f)>7:
             if True: joueur.boss_tues_tot=float(f[7])
             else: pass
        if len(f)>8:
            if True: joueur.argent=float(f[8])
            else: pass
        if len(f)>9:
            if True: joueur.tpsmaxsanstirer=float(f[9])
            else: pass
        if len(f)>10:
            if True: joueur.tpsmaxsanssubirdg=float(f[10])
            else: pass
        if len(f)>11:
            if True: joueur.niveaumaxfini=float(f[11])
            else: pass
        if len(f)>12:
            if True: joueur.nbmaxamnbmis=float(f[12])
            else: pass
        if len(f)>13:
            if True: joueur.nbmaxvitmis=float(f[13])
            else: pass
        if len(f)>14:
            if True: joueur.nbmaxregenenergy=float(f[14])
            else: pass
        if len(f)>15:
            if True: joueur.nbmaxregenarmure=float(f[15])
            else: pass
        if len(f)>16:
            if True: joueur.vaisseauchoisi=int(f[16])
            else: pass
        if len(f)>17:
            if True: joueur.nbfaitmission1=int(f[17])
            else: pass
        if len(f)>18:
            if True: joueur.nbfaitmission2=int(f[18])
            else: pass
        if len(f)>19:
            if True: joueur.nbfaitmission3=int(f[19])
            else: pass
        if len(f)>20:
            if True: joueur.nbfaitmission4=int(f[20])
            else: pass
        if len(f)>21:
            if True: joueur.nbfaitmission5=int(f[21])
            else: pass
        if len(f)>22:
            if True: joueur.nbfaitmission6=int(f[22])
            else: pass
        if len(f)>23:
            if True: joueur.nbfaitmission7=int(f[23])
            else: pass
        if len(f)>24:
            if True: joueur.nbfaitmission8=int(f[24])
            else: pass
        if len(f)>25:
            if True: joueur.nbfaitmission9=int(f[25])
            else: pass
        if len(f)>26:
            if True: joueur.nbfaitmission10=int(f[26])
            else: pass
        if len(f)>27:
            if True: joueur.nbfaitmission11=int(f[27])
            else: pass
        if len(f)>28:
            if True:
                ff=f[28].split(ccac)
                joueur.vaisseaux_possedes=[]
                for g in ff:
                    if g not in [""," "]:
                        joueur.vaisseaux_possedes.append(int(g))
                joueur.vaisseaux_possedes=list(set(joueur.vaisseaux_possedes))
            else: pass
        for m in missions:
            for x in range(joueur.nbfaitmission1):
                if missions.index(m)<=5:
                    m[0]=int(m[0]*1.2)
                else:
                    m[0]+=1
                m[3]=int(m[3]*1.2)
                m[4]+=1
    return joueur,missions

def savej(joueur):
    txt=""
    txt+=str(joueur.distancemaxparcourue)+cac
    txt+=str(joueur.distanceparcourue_tot)+cac
    txt+=str(joueur.scoremax)+cac
    txt+=str(joueur.score_tot)+cac
    txt+=str(joueur.ennemis_tues_max)+cac
    txt+=str(joueur.ennemis_tues_tot)+cac
    txt+=str(joueur.boss_tues_max)+cac
    txt+=str(joueur.boss_tues_tot)+cac
    txt+=str(joueur.argent)+cac
    txt+=str(joueur.tpsmaxsanstirer)+cac
    txt+=str(joueur.tpsmaxsanssubirdg)+cac
    txt+=str(joueur.niveaumaxfini)+cac
    txt+=str(joueur.nbmaxamnbmis)+cac
    txt+=str(joueur.nbmaxvitmis)+cac
    txt+=str(joueur.nbmaxregenenergy)+cac
    txt+=str(joueur.nbmaxregenarmure)+cac
    txt+=str(joueur.vaisseauchoisi)+cac
    txt+=str(joueur.nbfaitmission1)+cac
    txt+=str(joueur.nbfaitmission2)+cac
    txt+=str(joueur.nbfaitmission3)+cac
    txt+=str(joueur.nbfaitmission4)+cac
    txt+=str(joueur.nbfaitmission5)+cac
    txt+=str(joueur.nbfaitmission6)+cac
    txt+=str(joueur.nbfaitmission7)+cac
    txt+=str(joueur.nbfaitmission8)+cac
    txt+=str(joueur.nbfaitmission9)+cac
    txt+=str(joueur.nbfaitmission10)+cac
    txt+=str(joueur.nbfaitmission11)+cac
    for vp in joueur.vaisseaux_possedes:
        txt+=str(vp)+ccac
    txt=txt[:-1]
    f=open(dire+fs,"w")
    f.write(txt)
    f.close()

def alert(txt1,txt2,txt3):
    taillex,tailley=550,350
    posx,posy=50,200
    pygame.draw.rect(fenetre,(25,25,25),(posx,posy,taillex,tailley),0)
    fenetre.blit(font.render(txt1,20,(255,255,255)),[posx+15,posy+20])
    fenetre.blit(font.render(txt2,20,(255,255,255)),[posx+10,posy+60])
    fenetre.blit(font.render(txt3,20,(255,255,255)),[posx+10,posy+100])
    button=pygame.draw.rect(fenetre,(200,200,0),(posx+taillex/4,posy+tailley-50,taillex/2,40),0)
    fenetre.blit(font.render("ok",20,(0,0,0)),[posx+taillex/4+3,posy+tailley-40])
    pygame.display.update()
    encouralert=True
    while encouralert:
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN and event.key in [K_ESCAPE,K_SPACE]: encouralert=False
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if button.collidepoint(pos):
                    encouralert=False

def verif_missions(joueur,missions):
    while joueur.distanceparcourue_tot>=missions[0][0]:
        missions[0][0]=int(missions[0][0]*1.2)
        joueur.argent+=missions[0][3]
        missions[0][3]=int(missions[0][3]*1.2)
        joueur.nbfaitmission1+=1
        missions[0][4]+=1
        alert("Vous avez fini la mission : ",missions[0][1]+str(missions[0][0])+missions[0][2],"vous avez gagné "+str(int(missions[0][3]/1.5))+" argent")
    while joueur.ennemis_tues_tot>=missions[1][0]:
        missions[1][0]=int(missions[1][0]*1.2)
        joueur.argent+=missions[1][3]
        missions[1][3]=int(missions[1][3]*1.2)
        joueur.nbfaitmission2+=1
        missions[1][4]+=1
        alert("Vous avez fini la mission : ",missions[1][1]+str(missions[1][0])+missions[1][2],"vous avez gagné "+str(int(missions[1][3]/1.5))+" argent")
    while joueur.boss_tues_tot>=missions[2][0]:
        missions[2][0]=int(missions[2][0]*1.2)
        joueur.argent+=missions[2][3]
        missions[2][3]=int(missions[2][3]*1.2)
        joueur.nbfaitmission3+=1
        missions[2][4]+=1
        alert("Vous avez fini la mission : ",missions[2][1]+str(missions[2][0])+missions[2][2],"vous avez gagné "+str(int(missions[2][3]/1.5))+" argent")
    while joueur.score_tot>=missions[3][0]:
        missions[3][0]=int(missions[3][0]*1.2)
        joueur.argent+=missions[3][3]
        missions[3][3]=int(missions[3][3]*1.2)
        joueur.nbfaitmission4+=1
        missions[3][4]+=1
        alert("Vous avez fini la mission : ",missions[3][1]+str(missions[3][0])+missions[3][2],"vous avez gagné "+str(int(missions[3][3]/1.5))+" argent")
    while joueur.tpsmaxsanstirer>=missions[4][0]:
        missions[4][0]=int(missions[4][0]*1.2)
        joueur.argent+=missions[4][3]
        missions[4][3]=int(missions[4][3]*1.2)
        joueur.nbfaitmission5+=1
        missions[4][4]+=1
        alert("Vous avez fini la mission : ",missions[4][1]+str(missions[4][0])+missions[4][2],"vous avez gagné "+str(int(missions[4][3]/1.5))+" argent")
    while joueur.tpsmaxsanssubirdg>=missions[5][0]:
        missions[5][0]=int(missions[5][0]*1.2)
        joueur.argent+=missions[5][3]
        missions[5][3]=int(missions[5][3]*1.2)
        joueur.nbfaitmission6+=1
        missions[5][4]+=1
        alert("Vous avez fini la mission : ",missions[5][1]+str(missions[5][0])+missions[5][2],"vous avez gagné "+str(int(missions[5][3]/1.5))+" argent")
    while joueur.niveaufini>=missions[6][0]:
        missions[6][0]=int(missions[6][0]+1)
        joueur.argent+=missions[6][3]
        missions[6][3]=int(missions[6][3]*1.2)
        joueur.nbfaitmission7+=1
        missions[6][4]+=1
        alert("Vous avez fini la mission : ",missions[6][1]+str(missions[6][0])+missions[6][2],"vous avez gagné "+str(int(missions[6][3]/1.5))+" argent")
    while joueur.nbmaxamnbmis>=missions[7][0]:
        missions[7][0]=int(missions[7][0]+1)
        joueur.argent+=missions[7][3]
        missions[7][3]=int(missions[7][3]*1.2)
        joueur.nbfaitmission8+=1
        missions[7][4]+=1
        alert("Vous avez fini la mission : ",missions[7][1]+str(missions[7][0])+missions[7][2],"vous avez gagné "+str(int(missions[7][3]/1.5))+" argent")
    while joueur.nbmaxvitmis>=missions[8][0]:
        missions[8][0]=int(missions[8][0]+1)
        joueur.argent+=missions[8][3]
        missions[8][3]=int(missions[8][3]*1.2)
        joueur.nbfaitmission9+=1
        missions[8][4]+=1
        alert("Vous avez fini la mission : ",missions[8][1]+str(missions[8][0])+missions[8][2],"vous avez gagné "+str(int(missions[8][3]/1.5))+" argent")
    while joueur.nbmaxregenenergy>=missions[9][0]:
        missions[9][0]=int(missions[9][0]+1)
        joueur.argent+=missions[9][3]
        missions[9][3]=int(missions[9][3]*1.2)
        joueur.nbfaitmission10+=1
        missions[9][4]+=1
        alert("Vous avez fini la mission : ",missions[9][1]+str(missions[9][0])+missions[9][2],"vous avez gagné "+str(int(missions[9][3]/1.5))+" argent")
    while joueur.nbmaxregenarmure>=missions[10][0]:
        missions[10][0]=int(missions[10][0]+1)
        joueur.argent+=missions[10][3]
        missions[10][3]=int(missions[10][3]*1.2)
        joueur.nbfaitmission11+=1
        missions[10][4]+=1
        alert("Vous avez fini la mission : ",missions[10][1]+str(missions[10][0])+missions[10][2],"vous avez gagné "+str(int(missions[10][3]/1.5))+" argent")
    return joueur

def act_j(joueur,vaisseau):
    joueur.score=vaisseau.score
    joueur.score_tot+=vaisseau.score
    if vaisseau.score>joueur.scoremax: joueur.scoremax=vaisseau.score
    joueur.distanceparcourue=vaisseau.distance_parcourue
    joueur.distanceparcourue_tot+=vaisseau.distance_parcourue
    if vaisseau.distance_parcourue>joueur.distancemaxparcourue: joueur.distancemaxparcourue=vaisseau.distance_parcourue
    joueur.ennemis_tues=vaisseau.ennemistues
    joueur.ennemis_tues_tot+=vaisseau.ennemistues
    if vaisseau.ennemistues>joueur.ennemis_tues_max: joueur.ennemis_tues_max=vaisseau.ennemistues
    joueur.boss_tues=vaisseau.bosstues
    joueur.boss_tues_tot+=vaisseau.bosstues
    if vaisseau.bosstues>joueur.boss_tues_max: joueur.boss_tues_max=vaisseau.bosstues
    if vaisseau.tpsmaxsanstirer>joueur.tpsmaxsanstirer: joueur.tpsmaxsanstirer=vaisseau.tpsmaxsanstirer
    if vaisseau.tpsmaxsanssubirdg>joueur.tpsmaxsanssubirdg: joueur.tpsmaxsanssubirdg=vaisseau.tpsmaxsanssubirdg
    if vaisseau.nbregenenergy>joueur.nbmaxregenenergy: joueur.nbmaxrengenenergy=vaisseau.nbregenenergy
    if vaisseau.nbregenarmure>joueur.nbmaxregenarmure: joueur.nbmaxrengenarmure=vaisseau.nbregenarmure
    nb=vaisseau.nbmis-1+vaisseau.amdg
    if nb>joueur.nbmaxamnbmis: joueur.nbmaxamnbmis=nb
    if vaisseau.amttir>joueur.nbmaxvitmis: joueur.nbmaxvitmis=vaisseau.amttir
    joueur.niveaufini=vaisseau.niveaux_finis
    if vaisseau.niveaux_finis>joueur.niveaumaxfini: joueur.niveaumaxfini=vaisseau.niveaux_finis
    joueur.argent+=vaisseau.argent
    return joueur
        

#######menu

def aff_menu(menu,j,vr):
    bts=[None,None,None,None,None,None,None,None]
    fenetre.blit(imgfond1,[0,0])
    clmns=[(250,250,0),(250,250,0),(250,250,0),(250,250,0)]
    clmns[menu]=(0,0,250)
    bts[1]=pygame.draw.rect(fenetre,(0,0,0),(tex/4*0,0,tex/4,35),0)
    pygame.draw.rect(fenetre,clmns[0],(tex/4*0,0,tex/4,35),2)
    fenetre.blit(font.render("jouer",20,clmns[0]),[tex/4*0+25,10])
    bts[2]=pygame.draw.rect(fenetre,(0,0,0),(tex/4*1,0,tex/4,35),0)
    pygame.draw.rect(fenetre,clmns[1],(tex/4*1,0,tex/4,35),2)
    fenetre.blit(font.render("missions",20,clmns[1]),[tex/4*1+25,10])
    bts[3]=pygame.draw.rect(fenetre,(0,0,0),(tex/4*2,0,tex/4,35),0)
    pygame.draw.rect(fenetre,clmns[2],(tex/4*2,0,tex/4,35),2)
    fenetre.blit(font.render("stats",20,clmns[2]),[tex/4*2+25,10])
    bts[4]=pygame.draw.rect(fenetre,(0,0,0),(tex/4*3,0,tex/4,35),0)
    pygame.draw.rect(fenetre,clmns[3],(tex/4*3,0,tex/4,35),2)
    fenetre.blit(font.render("vaisseaux",20,clmns[3]),[tex/4*3+25,10])
    if menu==0: #jouer
        bts[0]=pygame.draw.rect(fenetre,(200,200,20),(200,400,200,100),0)
        fenetre.blit(fon2.render("Jouer",20,(250,0,0)),[235,415])
    elif menu==1: #missions
        fenetre.blit(font1.render("Missions : ",20,(250,250,250)),[250,75])
        yy=150
        for m in missions:
            fenetre.blit(font.render("-"+m[1]+str(m[0])+m[2],20,(250,250,200)),[50,yy])
            yy+=30
    elif menu==2: #stats
         fenetre.blit( font1.render("Stats : ",20,(255,255,255)) , [250,50] )
         fenetre.blit( font.render("distance parcourue totale : "+str(int(j.distanceparcourue_tot))+"m"                  ,20,(250,250,250)) , [50,100] )
         fenetre.blit( font.render("distance parcoure maximale : "+str(int(j.distancemaxparcourue))+"m"                  ,20,(250,250,250)) , [50,120] )
         fenetre.blit( font.render("score total : "+str(int(j.score_tot))                                                ,20,(250,250,250)) , [50,140] )
         fenetre.blit( font.render("score maximal : "+str(int(j.scoremax))                                               ,20,(250,250,250)) , [50,160] )
         fenetre.blit( font.render("ennemis tués maximaux : "+str(int(j.ennemis_tues_max))                               ,20,(250,250,250)) , [50,180] )
         fenetre.blit( font.render("ennemis tués totaux : "+str(int(j.ennemis_tues_tot))                                 ,20,(250,250,250)) , [50,200] )
         fenetre.blit( font.render("boss tués maximaux : "+str(int(j.boss_tues_max))                                     ,20,(250,250,250)) , [50,220] )
         fenetre.blit( font.render("boss tués totaux : "+str(int(j.boss_tues_tot))                                       ,20,(250,250,250)) , [50,240] )
         fenetre.blit( font.render("temps maximal sans tirer : "+str(j.tpsmaxsanstirer)[:5]+"sec"                        ,20,(250,250,250)) , [50,260] )
         fenetre.blit( font.render("temps maximal sans subir de dégats : "+str(j.tpsmaxsanssubirdg)[:5]+"sec"            ,20,(250,250,250)) , [50,280] )
         fenetre.blit( font.render("nombre maximal d'améliorations de la vitesse des missiles : "+str(int(j.nbmaxvitmis)),20,(250,250,250)) , [50,300] )
         fenetre.blit( font.render("nombre maximal d'améliorations sur le nombre de missiles : "+str(int(j.nbmaxamnbmis)),20,(250,250,250)) , [50,320] )
         fenetre.blit( font.render("nombre maximal de regénération d'énergie : "+str(int(j.nbmaxregenenergy))            ,20,(250,250,250)) , [50,340] )
         fenetre.blit( font.render("nombre maximal de regénération d'armure : "+str(int(j.nbmaxregenarmure))             ,20,(250,250,250)) , [50,360] )
         fenetre.blit( font.render("niveau maximal fini : "+str(int(j.niveaumaxfini))                                    ,20,(250,250,250)) , [50,380] )
         fenetre.blit( font.render("argent : "+str(int(j.argent))                                                        ,20,(250,250,250)) , [50,400] )
    elif menu==3: #vaisseaux
        bts[5]=pygame.draw.rect(fenetre,(150,100,0),(50,tey-50,150,30),0)
        fenetre.blit(font.render("précédent",20,(0,0,0)),[85,tey-45])
        bts[6]=pygame.draw.rect(fenetre,(150,100,0),(tex-200,tey-50,150,30),0)
        fenetre.blit(font.render("suivant",20,(0,0,0)),[tex-175,tey-45])
        if vr in j.vaisseaux_possedes and j.vaisseauchoisi==vr: txt,cl="choisi",(0,200,0)
        elif vr in j.vaisseaux_possedes: txt,cl="choisir",(200,200,0)
        elif j.argent >= vaisseauxtps[vr][13]: txt,cl="acheter "+str(vaisseauxtps[vr][13]),(200,150,0)
        else: txt,cl="acheter "+str(vaisseauxtps[vr][13]),(200,0,0)
        bts[7]=pygame.draw.rect(fenetre,cl,(tex/2-100,tey-50,200,30),0)
        fenetre.blit(font.render(txt,20,(0,0,0)),[tex/2-65,tey-45])
        fenetre.blit( pygame.transform.scale(pygame.image.load(dimg+vaisseauxtps[vr][3][0]),[150,150]), [tex/2-75,100] )
        fenetre.blit( font1.render(vaisseauxtps[vr][0],20,(250,250,250)), [tex/2-50,50] )
        fenetre.blit( font.render("vies : "+str(vaisseauxtps[vr][4]),20,(250,250,250)), [tex/2-250,300] )
        fenetre.blit( font.render("armure : "+str(vaisseauxtps[vr][5]),20,(250,250,250)), [tex/2-250,320] )
        fenetre.blit( font.render("vitesse : "+str(vaisseauxtps[vr][12]),20,(250,250,250)), [tex/2-250,340] )
        fenetre.blit( font.render("energie : "+str(vaisseauxtps[vr][6]),20,(250,250,250)), [tex/2-250,360] )
        fenetre.blit( font.render("degats missiles : "+str(vaisseauxtps[vr][7]),20,(250,250,250)), [tex/2-250,380] )
        fenetre.blit( font.render("nombre missiles : "+str(vaisseauxtps[vr][8])+"-"+str(vaisseauxtps[vr][9]),20,(250,250,250)), [tex/2-250,400] )
        fenetre.blit( font.render("vitesse missiles : "+str(vaisseauxtps[vr][10])+"-"+str(vaisseauxtps[vr][11]),20,(250,250,250)), [tex/2-250,420] )
        #0=nom      1=tx 2=ty 3=img 4=vies 5=armure_tot 6=energy_tot 7=missile degats
        #8=nb missiles 9=nb missiles max 10=vitesse missiles 11=vitesse missiles max 12=vitesse ,13=prix
    pygame.display.update()
    return bts

def main_menu(missions):
    joueur,missions=loadj(missions)
    joueur=verif_missions(joueur,missions)
    savej(joueur)
    encourme=True
    menu=0
    vr=joueur.vaisseauchoisi
    pygame.mixer.music.load(dmus+random.choice(musiques_menu))
    pygame.mixer.music.play(-1)
    needtoaff=True
    while encourme:
        if needtoaff:
            bts=aff_menu(menu,joueur,vr)
            needtoaff=False
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
                            pygame.mixer.music.stop()
                            vaisseau=main_jeu(joueur.vaisseauchoisi)
                            joueur=act_j(joueur,vaisseau)
                            savej(joueur)
                            joueur=verif_missions(joueur,missions)
                            savej(joueur)
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load(dmus+random.choice(musiques_menu))
                            pygame.mixer.music.play(-1)
                        elif di==1: menu=0
                        elif di==2: menu=1
                        elif di==3: menu=2
                        elif di==4: menu=3
                        elif di==5:
                            if vr>0: vr-=1
                        elif di==6:
                            if vr<len(vaisseauxtps)-1: vr+=1
                        elif di==7:
                            if vr in joueur.vaisseaux_possedes:
                                joueur.vaisseauchoisi=vr
                            else:
                                if joueur.argent>=vaisseauxtps[vr][13]:
                                    joueur.argent-=vaisseauxtps[vr][13]
                                    joueur.vaisseaux_possedes.append(vr)
                        needtoaff=True
                savej(joueur)
    savej(joueur)

main_menu(missions)

