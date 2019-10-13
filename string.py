str=input()
for i in range(26):
    print(i,' ',str.count(chr(i+ord('a')))+str.count(chr(i+ord('A'))))