import os
import hashlib

pw = hashlib.sha256(b'mygreatpassword')
salt = os.urandom(16)

print(pw.hexdigest())
print(salt)

salted_pw = (salt.hex()) + (pw.hexdigest())
print(salted_pw)

hashed_salted_pw = hashlib.sha256(b'{salted_pw}').hexdigest()
print(hashed_salted_pw)