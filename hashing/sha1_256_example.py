import hashlib

with open('./war-and-peace.txt', 'rb') as readfile:
    file = readfile.read()
    tolstoy_hash = hashlib.sha1(file).hexdigest()
    print(tolstoy_hash)

with open('./war-and-peace.txt', 'rb') as readfile:
    file = readfile.read()
    tolstoy_hash = hashlib.sha256(file).hexdigest()
    print(tolstoy_hash)