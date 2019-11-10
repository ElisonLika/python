import sys
n=ord(sys.argv[1])-48 #Пусть файлов будет меньше 10 :)
a=[0 for i in range(128)]
b=0
for i in range(n):
    f=open(sys.argv[(3+i)],'r')
    st=f.read()
    stb=bytearray(st,'utf-8')
    for i in range(128):
        a[i]+=stb.count(i)+stb.count(i)
        b+=a[i]
    f.close
for i in range(128):
    a[i]/=b
a=str(a)

fo=open(sys.argv[2],'w')
fo.write(a)
fo.close