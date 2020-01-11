import dopfun

class RSAKey:
    def __init__(self, power=None, mod=None):
        self.power=power
        self.mod=mod
    @property
    def power(self):
        return self.power
    @power.setter
    def power(self)
        self.power=
    @property
    def mod(self)
        return self.mod
    @mod.setter
    def mod(self)
        self.mod=
    def __repr__(self)
    def __str__(self)
    def dump(self, filename=None):

    def load(self, filename=None):

class RSASecKey(RSAKey):
class RSAPubKey(RSAKey):
      
class RSACrypto:
    def __init__(self, pub_key, sec_key):
        self.pub=pub_key
        self.sec=sec_key
    @property
    def block_len(self)
        #RSA.block_len
    def encrypt(self, block):
        
    def decrypt(self, block)
    def encrypts(self, message)
    def decrypts(self, cyphertext)
    def encryptb(self, message)
    def decryptb(self, cyphertext)

def gen_keys(number, half_len=256)
