import time
import string

def generate_substitution_table():
    ''' Generates the substitution table for deciphering the flag '''
    characters          = string.ascii_lowercase
    shifted_characters  = characters[11:] + characters[:11]

    return dict(zip(characters, shifted_characters))

def decrypt_flag():
    with open('ciphertext.txt', "r") as f:
        flag = f.read().strip() # Get the flag from the file

    sub_table = generate_substitution_table()
    sub_table.update({ "'": "'", "_": "_", "{": "{", "}": "}" }) # updating the table to avoid KeyError

    return ''.join(list(map( lambda x: sub_table[x], list(flag) )))

if __name__ == "__main__":
    start = time.time()
    print(f"\nDecrypted flag: { decrypt_flag() }")
    print(f"Time taken: { time.time() - start }ms\n")


