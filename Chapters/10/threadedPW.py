import itertools

letters = []
for num in xrange(97, 123):
	letters.append(chr(num))

def wordReturn(letters, number):
	for letterList in itertools.product(''.join(letters), repeat=number):
		word = ''.join(letterList)
		return word

def test(word):
	print word

test(wordReturn(letters,4))