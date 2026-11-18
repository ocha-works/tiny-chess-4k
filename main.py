import json,os
import urllib.request as U
E=os.getenv("MAKEFUN_ENV_URL")
V=[0,100,320,330,500,900]
KN=[33,31,18,14,-14,-18,-31,-33]
KG=[1,-1,16,-16,15,17,-15,-17]
BD=[15,17,-15,-17]
RD=[1,-1,16,-16]
DR=[0,0,KN,BD,RD,KG,KG]
D=lambda s:[ord(c)-61 for c in s]
PT=[[],D("====BGG)B83====QBBGVGGQ[oooo===="),D(")=BBGL=LQBLQ=GL)==")]+[[0]*32]*4
M=lambda s:(s>>4)*4+((s&7)if(s&7)<4 else 7-(s&7))
def pv(p,s):
 t=abs(p)
 return V[t]+PT[t][M(s)]if p>0 else -V[t]-PT[t][M(s^112)]
ZK=lambda i:i*2654435761%2**64
CK={0:13,7:14,4:12,112:7,119:11,116:3}
B=[0]*128;KQ=[0,0];UN=[]
NL=8e4;BM=0;I=10**9
def atk(s,by):
 for d in((-15,-17)if by>0 else(15,17)):
  if not (s+d)&136 and B[s+d]==by:return 1
 for ds,p,sl in((KN,2,0),(KG,6,0),(BD,3,1),(RD,4,1)):
  for d in ds:
   x=s+d
   while not x&136:
    q=B[x]
    if q:
     if q==p*by or(sl and q==5*by):return 1
     break
    if not sl:break
    x+=d
 return 0
def gen(co):
 mv=[];ap=mv.append
 for s in range(128):
  if s&136:continue
  p=B[s]
  if p*SD<=0:continue
  t=abs(p)
  if t==1:
   u=16*SD;la=7*(SD>0)
   for d in(u-1,u,u+1):
    to=s+d
    if to&136:continue
    q=B[to]
    if d==u:
     if q:continue
    elif not(q*SD<0 or to==EP):continue
    if d==u and not co and s>>4==1+5*(SD<0)and not B[s+2*u]:ap(s|(s+2*u)<<7)
    for pr in((5,4,3,2)if to>>4==la else(0,)):
     if pr or d!=u or not co:ap(s|to<<7|pr<<14)
  else:
   for d in DR[t]:
    to=s+d
    while not to&136:
     q=B[to]
     if q:
      if q*SD<0:ap(s|to<<7)
      break
     if not co:ap(s|to<<7)
     if t in(2,6):break
     to+=d
 if co:return mv
 ksq=60-56*SD
 if B[ksq]==6*SD:
  bb=(5-3*SD)//2
  for bt,ds,em in((bb,2,(1,2)),(bb<<1,-2,(-1,-2,-3))):
   if CA&bt and not any(B[ksq+x]for x in em)and not(atk(ksq,-SD)or atk(ksq+em[0],-SD)):ap(ksq|(ksq+ds)<<7)
 return mv
def mk(m):
 global SD,CA,EP,SC,KY
 UN.append((B[:],SD,CA,EP,SC,KQ[:],KY))
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 p=B[f];cap=B[t];cs=t;ip=abs(p)==1
 if ip and t==EP:
  cs=t-16*SD;cap=B[cs];B[cs]=0
 KY^=ZK(2000+CA)
 if cap:
  KY^=ZK((cap+7)*128+cs)
  SC-=pv(cap,cs)
 KY^=ZK((p+7)*128+f);B[f]=0
 np=pr*p if pr else p
 if pr or abs(p)!=6:SC+=pv(np,t)-pv(p,f)
 KY^=ZK((np+7)*128+t);B[t]=np
 if abs(p)==6:
  KQ[p<0]=t
  if abs(t-f)==2:
   rf,rt=(t+1,t-1)if t>f else(t-2,t+1)
   r=B[rf];B[rf]=0;B[rt]=r
   KY^=ZK((r+7)*128+rf)^ZK((r+7)*128+rt);SC+=pv(r,rt)-pv(r,rf)
 CA&=CK.get(f,15)&CK.get(t,15);KY^=ZK(2000+CA);EP=-1
 if ip and abs(t-f)==32:EP=f+16*SD
 SD=-SD;KY^=ZK(3000)
def un():
 global B,SD,CA,EP,SC,KQ,KY
 B,SD,CA,EP,SC,KQ,KY=UN.pop()
def nm(d,a,b,ply):
 global ND,ST,BM
 ND+=1;ki=SD<0;ck=atk(KQ[ki],-SD);tm=0;best=-I
 if ck:d+=1
 if ND>=NL:ST=1;return 0
 if d<=0:
  if ply>=96:return SC*SD
  if not ck:
   best=SC*SD
   if best>=b:return best
 else:
  e=TT.get(KY)
  if e:
   tm=e[3]
   if e[0]>=d:
    s=e[2]
    if e[1]==0 or(e[1]==1 and s>=b):return s
 mv=gen(not ck if d<=0 else 0);mv.sort(key=lambda m:-(1<<28)if m==tm else-(2**24+V[abs(B[(m>>7)&127])]*16-abs(B[m&127]))if B[(m>>7)&127]else 0)
 a0=a;bm=0
 for m in mv:
  mk(m)
  if atk(KQ[ki],SD):un();continue
  sc=-nm(d-1,-b,-a,ply+1)
  un()
  if ST:return 0
  if sc>best:best=sc;bm=m
  if sc>a:a=sc
  if a>=b:break
 if not bm:return -100000+ply if ck else best if d<=0 else 0
 if d<=0:return best
 TT[KY]=(d,(best>=b)+2*(best<=a0),best,bm)
 if ply==0:BM=bm
 return best
def ch():
 global TT,ND,ST,BM
 TT={};BM=0
 for d in range(1,64):
  ND=0;ST=0
  nm(d,-I,I,0)
  if ST:break
 return BM
def au(u):
 f,t=[ord(u[i])-97+16*(ord(u[i+1])-49)for i in(0,2)]
 pr="nbrq".index(u[4])+2 if len(u)==5 else 0
 mk(f|t<<7|pr<<14)
def po(p,b):
 return json.load(U.urlopen(U.Request(E+p,data=json.dumps(b).encode())))
while 1:
 g=po("/game",{});w=g["status"]
 if w=="done":break
 while w=="your_move":
  B=[0]*128;SD=1;CA=15;EP=-1;SC=0;KQ=[4,116];KY=3382560316719;UN=[]
  for i,t in enumerate((4,2,3,5,6,3,2,4)):
   for s,p in((i,t),(i+16,1),(i+96,-1),(i+112,-t)):B[s]=p
  for u in g["moves"]:au(u)
  m=ch()
  g=po("/move",{"game":g["game"],"move":"%c%d%c%d"%(97+(m&7),(m>>4&7)+1,97+(m>>7&7),(m>>11&7)+1)+("nbrq"[(m>>14)-2]if m>>14 else"")});w=g["status"]
