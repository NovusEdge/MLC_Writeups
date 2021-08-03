from time import time
from itertools import cycle


def ascii_to_int(char):
    return ord(char)


def xor_function(data, key): 
    return ''.join(chr(ord(c)^ord(k)) for c,k in zip(data, cycle(key)))


def decrypt_flag():
    flag = "\x1f \xeca_\xac\xef\xae\xffX F\x90\xacV\xcf\x9c\xab\x86W\xb1\xb9c\x06\xf9\x1c\xa6G\xb2\x96\xf3"
    key = '''yL\x8d\x06$\x9f\x97\xcd\x93-S/\xe6\xc5"\xb6\xc3\x9f\xf2\x08\xd8\xcdVY\x9fu\xc8t\xc1\xe2\x8e"
'''

    return xor_function(flag, key)

if __name__ == "__main__":
    start = time()
    print(f"\nDecrypted flag: { decrypt_flag() }")
    print(f"Time taken: { time() - start }\n")
