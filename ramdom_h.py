from random import random
from hashlib import md5

def ramdom_hash():
    for _ in range(1000):
        r = str(random()).encode()
        hash_thing = md5(r).hexdigest()

        if hash_thing[0] == hash_thing[1] == '0':
            return True
        
    return False

print(ramdom_hash())