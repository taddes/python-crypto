import hashlib

md5hash = hashlib.md5()
md5hash.update(b'Taddes')
print(md5hash.hexdigest())

hexstring = hashlib.md5(b'bob').hexdigest()
binstring = bin(int(hexstring, 16))

print(f"{binstring[2:66]}\n{binstring[66:]}")

with open('./war-and-peace.txt', 'rb') as readfile:
    file = readfile.read()
    tolstoy_hash = hashlib.md5(file).hexdigest()
    print(tolstoy_hash)

