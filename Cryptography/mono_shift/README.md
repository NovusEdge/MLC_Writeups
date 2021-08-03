### Problem Statement:
```txt
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher,
Caesar's code or Caesar shift, is one of the simplest and most widely known
encryption techniques.

It is a type of substitution cipher in which each letter in the plaintext is
replaced by a letter some fixed number of positions down the alphabet.
```

---

### Contents of `ciphertext.txt`:
    uapv{ndj'kt_qtvjc_ndjg_rgneid_psktcijgth}

---

As stated by the challenge statement, the encryption is a Caesar cipher of some sort.
Now, to solve this, we may try the following approach:

First, we make a substitution table for the Caesar cipher.

Since we know, that the flag may be in the format: "flag{...}"
We can map out that:
- u → f
- a → l
- p → a
- v → g

Clearly, there's a shift of `+15`

The substitution table thus formed will be:


Unshifted|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z
--|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
Shifted|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|a|b|c|d|e|f|g|h|i|j|k


We can implement a script like `mono_shift_solution.py` to obtain the decrypted flag.

---

### Decrypted flag:
	flag{you've_begun_your_crypto_adventures}


Link to the challenge: [Mono_Shift](https://training.majorleaguecyber.org/challenges#Mono%20Shift-7)
