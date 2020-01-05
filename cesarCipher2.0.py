import random
import argparse
import math

def freq(st,a,b): 
    for j in st:
        stb=bytearray(j,'utf-16BE')
        a[0]+=stb.count(b'\x00\x00')
        b+=a[0]
        for k in range(255):
            a[k+1]+=stb.count(k+1)
            b+=a[k+1]
    return a,b
def perest(sours):
    res=[]
    elem=len(sours)
    arrang=math.factorial(elem)
    for i in range(arrang):
        res.append([])
        source=list(sours)
        for j in range(elem):
            p=i//math.factorial(elem-1-j)%len(source)
            res[len(res)-1].append(source[p])
            source.pop(p)
    return res
def lst(elem,ls,ls2,c):
    res=[]
    for i in range(c):
        j=ls.index(elem)
        k=ls2.index(elem)
        res.append(j)
        ls[j]=1
        ls2[k]=1
    return res
def new(ls,num,elem):
    for i in range(len(num)):
        ls[num[i]]=elem[i]

def createGen(args):
    with open(args.finp,'r') as fi:
        yield fi.read()
def createG(args,i):
    with open(args.fil[i],'r') as fi:
        yield fi.read()

def genkey(args):
    alp1=bytes([i for i in range(256)])
    alp2=bytes([])
    for i in range(256):
        k=random.randint(0,255-i)
        alp2+=bytes([alp1[k]])
        alp1=alp1[:k]+alp1[k+1:]
    with open(args.file,'wb') as f:
        f.write(alp2)
    return

def dec(args):
    fk = open(args.fkey,'rb')
    fo = open(args.fout,'w',encoding='utf-16BE')
    st= createGen(args)
    b = fk.read()
    dicb = {b[i]:i for i in range(256)}
    so=''
    for i in st:
        stb=bytearray(i,'utf-16BE')
        for j in range(len(stb)//2):
            sb=bytes([0x00,dicb[stb[2*j+1]]])
            so+=(sb.decode('utf-16BE'))
        fo.write(so)   
    fo.close()
    fk.close()
    return

def enc(args):
    fk = open(args.fkey,'rb')
    fo = open(args.fout,'w',encoding='utf-16BE')
    st= createGen(args)
    b = fk.read()
    dicb = {i:b[i] for i in range(256)}
    so=''
    for i in st:
        stb=bytearray(i,'utf-16BE')
        for j in range(len(stb)//2):
            sb=bytes([0x00,dicb[stb[2*j+1]]])
            so+=(sb.decode('utf-16BE'))
        fo.write(so)   
    fo.close()
    fk.close()
    return

def makemodel(args):
    ln=len(args.fil)
    a=[0 for i in range(256)]
    b=0
    for i in range(ln):
        st=createG(args,i)
        a,b=freq(st,a,b)
    for i in range(256):
        a[i]/=b
    a.sort(reverse=True)
    fo=open(args.model,'w')
    for i in a:
        fo.write(str(i)+"\n")
    #fo.write(str(a))
    fo.close

def broke(args):
    fmodel = open(args.fmodel,'r')
    st= createGen(args)
    stm=[]
    for i in range(256):
        sk=fmodel.readline()
        stm.append(float(sk))
    stmc=list(stm)
    stm.sort(reverse=True)
    fi = open(args.finp,'r')
    st=createGen(args)
    a=[0 for i in range(256)]
    b=0
    a,b=freq(st,a,b)
    for i in range(256):
        a[i]/=b
    ac=list(a)
    a.sort(reverse=True)
    s=1#кол-во ключей
    i=0
    while a[i]>0:
        n=a[i]
        s*=math.factorial(a.count(a[i]))
        i+=a.count(a[i])
    key=[[0 for j in range(256)]for i in range(s)]
    h=1
    i=0
    odin=[]
    ind=[]
    while a[i]>0:
        n=a.count(a[i])
        num1=lst(a[i],ac,a,n)
        num2=[]
        for j in range(n):
            k=stmc.index(stm[i])
            num2.append(k)
            stmc[k]=1
            i+=1
        per=perest(num1)
        coun=math.factorial(n)
        for l in range(h):
            u=l*(s//h)
            for j in range(coun):
                m=j*((s//coun)//h)
                for k in range((s//coun)//h):
                    new(key[u+m+k],num2,per[j])
        h*=coun
    while i<256: #a[i]==0
        j=ac.index(0.0)
        odin.append(j)
        ac[j]=1
        k=stmc.index(stm[i])
        ind.append(k)
        stmc[k]=1
        i+=1
    for j in range(256):
        new(key[j],ind,odin)

    print(key)
    fmodel.close
    return

parser=argparse.ArgumentParser()
subparsers=parser.add_subparsers()
parser_genkey=subparsers.add_parser('genkey')
parser_genkey.add_argument('func',action='store_const',const=genkey)
parser_genkey.add_argument('--file','-o','--out', type=str, nargs='?', default='sec.key.bin')
parser_enc=subparsers.add_parser('enc')
parser_enc.add_argument('func',action='store_const',const=enc)
parser_enc.add_argument('--fkey','--key', type=str, nargs='?', default='sec.key.bin')
parser_enc.add_argument('--finp','-f' ,type=str, nargs='?', default='input.file.enc')
parser_enc.add_argument('--fout','-o', type=str, nargs='?', default='out.file.enc')
parser_dec=subparsers.add_parser('dec')
parser_dec.add_argument('func',action='store_const',const=dec)
parser_dec.add_argument('--fkey','--key', type=str, nargs='?', default='sec.key.bin')
parser_dec.add_argument('--finp','-f', type=str, nargs='?', default='out.file.enc')
parser_dec.add_argument('--fout','-o', type=str, nargs='?', default='out1.file.enc')
parser_makemodel=subparsers.add_parser('makemodel')
parser_makemodel.add_argument('func',action='store_const',const=makemodel)
parser_makemodel.add_argument('-model','-o', type=str, nargs='?', default='model.txt')
parser_makemodel.add_argument('fil',nargs='*')
parser_broke=subparsers.add_parser('broke')
parser_broke.add_argument('func',action='store_const',const=broke)
parser_broke.add_argument('--fmodel','-f', type=str, nargs='?', default='model.txt')
parser_broke.add_argument('--finp','-o', type=str, nargs='?', default='out.file.enc')
args=parser.parse_args()

args.func(args)