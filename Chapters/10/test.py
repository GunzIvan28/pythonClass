"""


"""


from threading import Thread
import itertools
import md5

hashDictionary = {0:'0b18a3d7b9c43ff1750d2baa4606b8d0',
				  1:'62cc0b4ebb0b57b40778179234246c38',
				  2:'17c0f75d610ec414e5c9be1a6059b65a'}
letters = []
# localtime = str(time.asctime(time.localtime(time.time())))

for num in xrange(97, 123):
	letters.append(chr(num))

class MyThread(Thread):

	def __init__(self, hashDictionary, charSet, charLen):
		Thread.__init__(self)
		self._charLen = charLen
		self._charSet = charSet
		self._hashDictionary = hashDictionary

	def run(self):
		self._wordReturn()

	def _wordReturn(self):
		for letterList in itertools.product(''.join(self._charSet), repeat=self._charLen):
			self._word = ''.join(letterList)
			self._pwInfo = self._hashCompare(self._word)
			if self._pwInfo != None:
				self._writeToFile(self._pwInfo)
				print 'Thread', self._charLen, 'complete.'
				print 'Word:', self._pwInfo[1]
				exit()
		print 'Thread', self._charLen, 'complete.'
		print 'No word found.'
		exit()

	def _hashCompare(self, word):
		self._hashedWord = md5.new(word)
		if self._hashedWord.hexdigest() == self._hashDictionary[0]:
			return ['1', word]
		elif self._hashedWord.hexdigest() == self._hashDictionary[1]:
			return ['2', word]
		elif self._hashedWord.hexdigest() == self._hashDictionary[2]:
			return ['3', word]
		else:
			return None

	def _writeToFile(self, pwInfo):
		self._pwFile = open('crackedHashes.txt', 'a')
		self._pwFile.write(','.join(self._pwInfo) + '\n')
		self._pwFile.close()

for i in xrange(1,9):
	newThread = MyThread(hashDictionary, letters, i)
	newThread.start()









# for i in xrange(0,10):
# 	myList.append(MyThread(i))
# for each in myList:
# 	each.start()


# Build string based on numOfChars:
# 	check and increment all of last char
# 	next = last char - 1
# 	if no:
# 		increment last char - 1
