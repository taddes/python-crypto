import os
import hashlib
import string
import random
def generate(alphabet, max_len):
    if max_len <= 0: return
    for c in alphabet:
        yield c
    for c in alphabet:
        for next in generate(alphabet, max_len-1):
            yield c + next

def check_hash():
    preimage_seed = random.choice(string.ascii_lowercase)
    preimage_seed_hash = hashlib.md5(preimage_seed.encode('utf-8'))
    preimage_seed_hash = preimage_seed_hash.hexdigest()
    print(preimage_seed)
    print(preimage_seed.encode('utf-8'))

    for char in string.ascii_lowercase:
        print(char)
        hash_char = hashlib.md5(char.encode('utf-8')).hexdigest()
        print(hash_char)
    if hash_char == preimage_seed_hash:
        return f'Match: {hash_char} equals preimage seed {preimage_seed_hash} for character {char}'


print(check_hash())

