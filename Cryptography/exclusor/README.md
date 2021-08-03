### Problem Statement:
```txt
The Exclusive-Or (XOR) operation is a basic primitive of cryptography.
Because the XOR of two values can be XOR'ed again with one of the original
operands to get the other operand, it's been used to implement basic
encryption schemes.

We encrypted this flag using the XOR Cipher but we'll give you the key.
```

---

#### Given Flag:
    \x1f \xeca_\xac\xef\xae\xffX F\x90\xacV\xcf\x9c\xab\x86W\xb1\xb9c\x06\xf9\x1c\xa6G\xb2\x96\xf3

#### Given Key:
    yL\x8d\x06$\x9f\x97\xcd\x93-S/\xe6\xc5"\xb6\xc3\x9f\xf2\x08\xd8\xcdVY\x9fu\xc8t\xc1\xe2\x8e

---

As the question mentions, the flag has been encrypted using `XOR encryption`, with the given key.

To decrypt the flag, we may use a script like `exclusor.py`

---

#### Decrypted flag:
	flag{3xclusivity_4t_it5_fin3st}


Link to the challenge: [Exclusor](https://training.majorleaguecyber.org/challenges#Exclusor-12)
