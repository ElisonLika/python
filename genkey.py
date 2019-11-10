alp1=bytes([i for i in range(128)])
alp2=bytes([])
import random
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file','-o','--out', type=str, nargs='?', default='sec.key.bin')
args=parser.parse_args()
for i in range(128):
    k=random.randint(0,127-i)
    alp2+=bytes([alp1[k]])
    alp1=alp1[:k]+alp1[k+1:]
with open(args.file,'wb') as f:
    f.write(alp2)