import hashlib

md5hash = hashlib.md5()
md5hash.update(b'Taddes')
print(md5hash.hexdigest())