import hashlib

hashCall = hashlib.md5()
pw = 'aaaaaaab'
hashCall.update(pw)
print hashCall.hexdigest()