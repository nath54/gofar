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
imgven0=pygame.image.load("images/ven0.png")
imgven1=pygame.image.load("images/ven1.png")
imgven2=pygame.image.load("images/ven2.png")
imgven3=pygame.image.load("images/ven3.png")
imgboss1=pygame.image.load("images/boss1.png")
imgb1=pygame.image.load("images/bonus1.png")
imgb2=pygame.image.load("images/bonus2.png")
imgb3=pygame.image.load("images/bonus3.png")
imgb4=pygame.image.load("images/bonus4.png")

bonuses=[["nb mis",1,imgb1],["speed mis",2,imgb2],["energy+",3,imgb3],["armure+",4,imgb4]]

venstps=[]
venstps.append( [30,30,imgven0,3,1,0.01,0.75,1,(250,0,100),25,10,1,2,8,5] )
venstps.append( [40,40,imgven1,4,1.25,0.01,0.70,2,(250,0,100),35,11,2,2,8,5] )
venstps.append( [50,50,imgven2,5,1.5,0.01,0.65,3,(250,0,100),50,12,4,2,8,5] )
venstps.append( [60,60,imgven3,6,1.75,0.01,0.50,4,(250,0,100),60,13,6,2,8,5] )

bosstps=[]
bosstps.append( [200,200,imgboss1,5,0,0.01,2,50,(250,200,0),2000,8,2,7,14,9] )
bosstps.append( [200,200,imgboss1,6,0,0.01,2,50,(250,200,0),4000,10,3,7,14,9] )
bosstps.append( [200,200,imgboss1,7,0,0.01,1.5,50,(250,200,0),6000,12,4,7,14,9] )


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
                        if self.pos in [0,2]:
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
        self.maxttir=0.01
        self.amttir=0
        self.amttirmax=49
        self.nbmis=1
        self.maxnbmis=7
        self.amdg=0
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
                mil=int(self.nbmis/2.)
                divtx=self.nbmis+1
                for x in range(self.nbmis):
                    mis.append(Missil(  self.px+self.tx/divtx*(x+1) , self.py+self.ty/2  ,self.mtx,self.mty,x-mil,self.mvity,self.mdg,1,self.mtps,self.mcl))
                
        return mis

class Vsen:
    def __init__(self,tp):
        vtp=tp
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
                mis.append( Missil( self.px+self.tx/divtx*(x+1) , self.py+self.ty/2  , self.mtx , self.mty , x-mil , self.mvit , self.dg , 0 , self.mtps , self.cl ))
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
                mis.append( Missil( self.px+self.tx/divtx*(x+1) , self.py+self.ty/2  , self.mtx , self.mty , x-mil , self.mvit , self.dg , 2 , self.mtps , self.cl ))
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
                if vaisseau.nbmis<5: vaisseau.nbmis+=1
                else:
                    vaisseau.amdg+=1
                    vaisseau.mdg+=1
            elif self.effet==2:
                if vaisseau.ttir>0.01:
                    vaisseau.ttir-=0.01
                    vaisseau.amttir+=1
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
                if v.tp==2:
                    pygame.draw.rect(fenetre,(250,0,0),(150,15,int(v.armure/v.armure_tot*(tex-250)),20),0)
        vaisseau.rect=fenetre.blit( vaisseau.img , [vaisseau.px,vaisseau.py] )
        fenetre.blit(font.render("score = "+str(int(score)),20,(210,210,250)) , [5,10] )
        fenetre.blit(font.render("vies = "+str(vaisseau.vie),20,(210,210,250)) , [5,30] )
        fenetre.blit(font.render("vitesse = "+str(vaisseau.acc)[:3],20,(210,210,250)) , [5,50] )
        fenetre.blit(font.render("fps = "+str(fps),20,(210,210,250)) , [5,70] )
        fenetre.blit(font.render("vitesse tir = "+str(vaisseau.amttir)+"/"+str(vaisseau.amttirmax),20,(210,210,250)) , [5,90] )
        txtm="nb missiles = "+str(vaisseau.nbmis)+"/"+str(vaisseau.maxnbmis)+" ( +"+str(vaisseau.amdg)+"dg)"
        fenetre.blit(font.render(txtm,20,(210,210,250)) , [5,110] )
        fenetre.blit(font.render("nb ennemis = "+str(int(nben)),20,(210,210,250)) , [5,130] )
        fenetre.blit(font.render("niveau = "+str(int(nv)),20,(210,210,250)) , [5,150] )
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

def bbb(score,vaer,fn1y,fn2y,mis,vaisseau,meter,limm,vens,nben,taugen,daugen,pause,bonus,dbn,tbn,nv):
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
            if v.tp==0: score+=250*nben*vaisseau.acc
            elif v.tp==2: score+=2500*vaisseau.acc
        if v.py>=tey:
            if v in vens: del(vens[vens.index(v)])
    if time.time()-daugen>=taugen and len(vens)==0:
        daugen=time.time()
        if nben<5: nben+=1
        else:
            if nv<len(bosstps):
                vens.append( Boss(bosstps[nv]) )
            else:
                bb=bosstps[len(bosstps)-1]
                bb.vie+=(len(bosstps)-1-nv)*2000
                bb.nbmis+=(len(bosstps)-1-nv)
                vens.append( Boss(bb) ) 
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
    vaer+=0.001
    if vaer>=1.:
        if vaisseau.acc<25.: vaisseau.acc+=0.1
        vaer=0.
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

def main_jeu():
    #fond
    fn1y=0
    fn2y=-tey
    #vaisseau
    vaisseau=Vaisso(tex/2,tey/2)
    vaer=0
    #meteor
    limm=10
    meter=[]
    #ven
    nben=1
    taugen=35
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
    while encour:
        t1=time.time()
        aff(fps,vaisseau,mis,meter,fn1y,fn2y,score,vens,pause,bonus,nv,nben)
        score,vaer,fn1y,fn2y,mis,vaisseau,meter,vens,nben,taugen,daugen,bonus,dbn,nv=bbb(score,vaer,fn1y,fn2y,mis,vaisseau,meter,limm,vens,nben,taugen,daugen,pause,bonus,dbn,tbn,nv)
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
    fenetre.blit(font.render("APPUYEZ SUR 'ESPACE' POUR QUITTER",20,(210,210,100)) , [tex/3,tey/2+200] )
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
    fenetre.blit(font.render("play",20,(250,0,0)),[250,415])
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

main_menu()

