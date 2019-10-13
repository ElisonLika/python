k=int(input())
s=input()
output=''
alpha=[chr(ord('a')+i)for i in range(26)]
output=''.join([alpha[(alpha.index(a)+k)%26] for a in s])
print(output)
