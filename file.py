a=[0 for i in range(33)]
f=open('file2.txt',encoding='utf-8')
str=f.read()
for i in range(33):
    a[i]+=str.count(chr(i+ord('а')))+str.count(chr(i+ord('А')))
    print(chr(i+ord('а')),' ',a[i])