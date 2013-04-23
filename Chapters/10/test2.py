import itertools
import md5

hash1 = '0b18a3d7b9c43ff1750d2baa4606b8d0'
hash2 = '62cc0b4ebb0b57b40778179234246c38'
hash3 = '17c0f75d610ec414e5c9be1a6059b65a'
letters = []

for num in xrange(97, 123):
	letters.append(chr(num))

"""
When hash is found, terminate thread and
start new thread with new hash.

Update value for number of hashes cracked and
check frequently to avoid running beyond when the
three hashes are cracked.
"""

def passCompare(word):
	hashedWord = md5.new(word)
	if hashedWord.hexdigest() == hash1:
		print word
		exit()
	elif hashedWord.hexdigest() == hash2:
		print word
		exit()
	elif hashedWord.hexdigest() == hash3:
		print word
		exit()

# THIS WORKS! Adjust repeat value for 
for pw in itertools.product(''.join(letters), repeat=5):
	newPw = ''.join(pw)
	print newPw
	passCompare(newPw)



# def all_perms(test):
# 	if len(test) <= 1:
# 		yield test 
# 	else:
# 		for perm in all_perms(test[1:]):
# 			for i in range(len(perm) + 1):
# 				#yield perm[:i]
# 				#yield test[0:1]
# 				#yield perm[i:]
# 				yield perm[:i] + test[0:1] + perm[i:]
# 				# yield var[:8]

# letters = []
# for num in xrange(97, 123):
# 	letters.append(chr(num))
# lets = ''.join(letters)

# for perm in all_perms('abcd'):
# 	print perm
	# if 'i' in perm:
	# 	print perm
	# 	exit()
	# else:
	# 	print perm


