import random

def is_prime(number, test_func=None, func_args=None):
    if test_func==None:
        n=rabin_miller_test(number,func_args)
    else:
        n=test_func(number, func_args)
    return n
 
def rabin_miller_test(number, log_precision=128):
    n=number-1
    m=n
    s=0    
    while m%2==0:
        s+=1
        m//=2 
    t=n//(2**s)
    k=random.sample([i for i in range(2,number)],log_precision)
    for i in range(log_precision):
        a=k[i]
        prime=False
        x=powermod(a,t,n+1)
        if x==1 or x==n:
            prime=True
        if prime==False:
            for j in range(s-1):
                x=(x*x)%(n+1)
                if x==1:
                    return prime
                if x==n:
                    break
                    prime=True
            if prime==False:
                return prime
    return prime


def get_next_prime(edge, test_func=None, func_args=None):
    if (edge%2)==0:
        edge+=1
    if test_func==None:
        while is_prime(edge,rabin_miller_test, func_args)==False:
            edge+=2
    else:
        while is_prime(edge,test_func, func_args)==False:
            edge+=2
    return edge

def gcd(a,b):
    while a!=0 and b!=0:
        if a>b:
            a %= b
        else:
            b %= a
    return a+b

def powermod(a,b,mod):
    k=a%mod
    while b!=0:
        ost=b%2
        b//=2
        if ost==1:
           a=(a*k)%mod
        k=(k*k)%mod
    return a 