import random
import string
from .models import Url


def generate_short_code(size=7,chars=string.ascii_lowercase+string.digits):
    # new_code = ''
    # for _ in range(size):
    #     new_code+=random.choice(chars)
    # return new_code
    
    return ''.join(random.choice(chars) for _ in range(size))


def generate_hash():
    size,chars= 7,string.ascii_lowercase+string.digits

    hash_value = ''.join(random.choice(chars) for _ in range(size))
    url = Url(None, hash_value)
    if url.is_hash_present():
        return generate_hash()
    
    return hash_value





