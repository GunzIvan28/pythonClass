def newPatron(firstName, lastName, numberOfBooks):
	"""Need to strip spaces."""
	"""Adds new patron to patronFile.txt"""  
	# books = [book.replace('/',' ') for book in books]
	# bookString = '/'.join(books)
	patronFile = open('patronFile.txt', 'a')
	patronFile.write((','.join([firstName,lastName,numberOfBooks]) + '\n'))
	patronFile.close()

def removePatron(patronInfo):
	patronFile = open('patronFile.txt', 'r')
	lines = patronFile.readlines()
	patronFile.close()
	patronFile = open('patronFile.txt', 'w')
	for line in lines:
		line = line.split(',')
		if line[0] != patronInfo[0] or line[1] != patronInfo[1]:
			line = ','.join(line) + '\n'
			patronFile.write(line)

def checkForPatron(firstName='', lastName=''):
	"""Checks file for existing patron."""
	patronFile = open('patronFile.txt', 'r')
	for line in patronFile:
		line = line.rstrip('\n').split(',')
		if line[1] == lastName and line[0] == firstName:
			patronFile.close()
			return line
	patronFile.close()
	return False
