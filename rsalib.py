import dopfun
import json

class RSAKey:
    def __init__(self, power=None, mod=None):
        self.power=power
        self.mod=mod
    @property
    def power(self):
        return self.power
    @power.setter
    def power(self,new_power):
        self.power=new_power
    @property
    def mod(self):
        return self.mod
    @mod.setter
    def mod(self, new_mod)
        self.mod=new_mod
    def __repr__(self):
        s=str(RSAKey.__class__.__name__)
        s+='( Power = '
        s+=str(self.power)[:8]
        k=len(str(self.power))-8
        if k>0:
            s+='<..'+str(k)+'..>'
        s+=', Mod = '
                s+=str(self.mod)[:8]
        k=len(str(self.mod))-8
        if k>0:
            s+='<..'+str(k)+'..>'
        s+=')'
        return s
    def __str__(self):
        dic={'power':self.power, 'mod':self.mod}
        string=json.dumps(dic)
        return string
    def dump(self, filename=None):
        with open(filename,'w') as f:
            f.write(__str__)
    def load(self, filename=None):
        with open(filename,'r') as f:
            dic=f.read()
        dic=json.loads(dic)
        RSAKey.power(self,dic.get('power'))
        RSAKey.mod(self,dic.get('mod'))

class RSASecKey(RSAKey):
    def dump(self,filename='key.sec'):
        RSAKey.dump(self,filename)
    def load(self,filename='key.sec'):
        RSAKey.load(self,filename)
class RSAPubKey(RSAKey):
    def dump(self,filename='pub.sec'):
        RSAKey.dump(self,filename)
    def load(self,filename='pub.sec'):
        RSAKey.load(self,filename)
      
class RSACrypto:
    def __init__(self, pub_key, sec_key):
        if (pub_key[0]*sec_key[0])%((pub_key[0]-1)*(sec_key[0]-1))==1:
            self.pub=pub_key
            self.sec=sec_key
        else:
            raise IOError("Error Key")
    @property
    def block_len(self)
        self.block_len=pub_key[0].bit_length()
        return self.block_len
    def encrypt(self, block):
        return dopfun.powermod(block,self.pub[0],self.pub[1])
    def decrypt(self, block):
        return dopfun.powermod(block,self.sec[0],self.sec[1])
    def encrypts(self, message):
        mes=message.encode('utf-8')
        return encryptb(self,mes)
    def decrypts(self, cyphertext):
        mesb=decryptb(self,cyphertext)
        return mesb.decode('utf-8')
    def encryptb(self, message):
        leng=self.block_len//8 #максимальное кол-во байт, которые могут шифроваться
        j=0
        k=len(message)%leng
        result='0x'
        for i in range((len(message)+leng-1)//leng):
            byst=message[j:j+k]
            k=leng
            inst=int.from_bytes(byst,'big')
            res='00'*leng
            res+=hex(encrypt(self,inst))[2:]
            result+=res[len(res)-2*leng:]
        return result
    def decryptb(self, cyphertext):
        lengt=len(cyphertext)
        leng=self.block//8
        result=b''
        j=leng*2
        ost=cyphertext
        while ost!='0x':
            byst=ost[:leng*2+2]
            inst=int(byst,10)
            ost='0x'+ost[2+j:]
            result+=decrypt(self,inst).to_bytes(leng,'big')
        return result

def test_key(Eiler):
    prime=17
    while True:
        if dopfun.gcd(Eiler,prime)==1:
            return(prime)
        else:
            prime=dopfun.get_next_prime(prime)
def euklid(e,fi):
    if b == 0:
        return 1
    else:
        m,n=euklid(e, fi%e)
        if n<0:
            n=fi+n
        return n,m-n*(e//fi)

def gen_keys(number, half_len=256):
    leng=dopfun.powermod(2,half_len-1,1)
    first_prime=dopfun.get_next_prime(leng)
    second_prime=dopfun.get_next_prime(first_prime)
    modul=first_prime*second_prime
    Eiler=(first_prime-1)*(second_prime-1)
    pub.key=[test_key(Eiler),modul]
    sec.key=[euklid(pub.key[0],Eiler)[0],modul]
    return RSACrypto(pub.key,sec.key)