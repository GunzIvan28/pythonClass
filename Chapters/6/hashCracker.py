# Lower case ASCII: a(97), z(122)

import hashlib
import os 

def clearScreen(): 
    os.system(['clear','cls'][os.name == 'nt']) 

hash1 = '0b18a3d7b9c43ff1750d2baa4606b8d0'
hash2 = '62cc0b4ebb0b57b40778179234246c38'
hash3 = '17c0f75d610ec414e5c9be1a6059b65a'
counter = 0

def hashCrack(characters, counter):
	hashCallOne = hashlib.md5()
	for first in characters:
		password = first
		hashCallOne.update(password)
		firstHash = hashCallOne.hexdigest()
		fancyPrintAndCheck(firstHash, password, counter)
		for second in characters:
			hashCallTwo = hashlib.md5()
			password = first + second
			hashCallTwo.update(password)
			secondHash = hashCallTwo.hexdigest()
			fancyPrintAndCheck(secondHash, password, counter)
			for third in characters:
				hashCallThree = hashlib.md5()
				password = first + second + third
				hashCallThree.update(password)
				thirdHash = hashCallThree.hexdigest()
				fancyPrintAndCheck(thirdHash, password, counter)
				for fourth in characters:
					hashCallFour = hashlib.md5()
					password = first + second + third + fourth
					hashCallFour.update(password)
					fourthHash = hashCallFour.hexdigest()
					fancyPrintAndCheck(fourthHash, password, counter)
					for fifth in characters:
						hashCallFive = hashlib.md5()
						password = first + second + third + fourth + fifth
						hashCallFive.update(password)
						fifthHash = hashCallFive.hexdigest()
						fancyPrintAndCheck(fifthHash, password, counter)
						for sixth in characters:
							hashCallSix = hashlib.md5()
							password = first + second + third + fourth + fifth + sixth
							hashCallSix.update(password)
							sixthHash = hashCallSix.hexdigest()
							fancyPrintAndCheck(sixthHash, password, counter)
							for seventh in characters:
								hashCallSeven = hashlib.md5()
								password = first + second + third + fourth + fifth + sixth + seventh
								hashCallSeven.update(password)
								seventhHash = hashCallSeven.hexdigest()
								fancyPrintAndCheck(seventhHash, password, counter)
								for eighth in characters:
									hashCallEight = hashlib.md5()
									password = first + second + third + fourth + fifth + sixth + seventh + eighth
									hashCallEight.update(password)
									eighthHash = hashCallEight.hexdigest()
									fancyPrintAndCheck(eighthHash, password, counter)

def fancyPrintAndCheck(hashValue, password, counter):
	clearScreen()
	print 'Cracking hash...\n'
	print '\t', hashValue	
	if counter > 3:
		exit()
	if hashValue == hash1:
		crackedHashInfo = 'Hash1 is:', password
		crackedHashes = open('crackedHashes.txt', 'a')	
		crackedHashes.write(crackedHashInfo)
		crackedHashes.close()
		counter += 1
	elif hashValue == hash2:
		crackedHashInfo = 'Hash2 is:', password
		crackedHashes = open('crackedHashes.txt', 'a')	
		crackedHashes.write(crackedHashInfo)
		crackedHashes.close()
		counter += 1
	elif hashValue == hash3:
		crackedHashInfo = 'Hash3 is:', password
		crackedHashes = open('crackedHashes.txt', 'a')	
		crackedHashes.write(crackedHashInfo)
		crackedHashes.close()
		counter += 1


crackedHashes = open('crackedHashes.txt', 'a')
crackedHashes.write('Starting...')
crackedHashes.close()
characters = ''
for i in xrange(97,123):
	characters += chr(i)

hashCrack(characters, counter)



