def is_prime(number, test_func=None, func_args=None):
    if test_func==None:
        n=rabin_miller_test(number,func_args)
    else:
        n=test_func(number, func_args)
    return n

def rabin_miller_test(number, log_precision=128):
    

def get_next_prime(edge, test_func=None, func_args=None):
    if (edge%2)==0:
        edge+=1
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