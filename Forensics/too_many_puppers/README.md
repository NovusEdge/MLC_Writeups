### Problem Statement:
```txt
Here is a zip file full of just the finest little puppers.
Can you find the flag from here?
```

---
We've been given a large zip archive: `puppy.zip`

Unzipping the archive:
```zsh
$ unzip puppy.zip

A ton of files >.<
```


To obtain the flag, we can use [`strings`]():

```zsh
$ strings pu* | grep "flag"
PxNc/TvNkzcm/UdfV/BVoAp/yHkWSGaL/bBYy/lxANKI/hgugRa/fvgXjIbXg/OSvfOVZ/vSXzvo/FSsDewdd/NFFzMKA/flag{0h_y0u've_found_me}PK
PxNc/TvNkzcm/UdfV/BVoAp/yHkWSGaL/bBYy/lxANKI/hgugRa/fvgXjIbXg/OSvfOVZ/vSXzvo/FSsDewdd/NFFzMKA/flag{0h_y0u've_found_me}PK
```


---

### The Flag:
    flag{0h_y0u've_found_me}


Link to the challenge: [Too Many Puppers](https://training.majorleaguecyber.org/challenges#Too%20Many%20Puppers-19)
