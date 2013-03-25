def new(self, firstName, lastName):
	"""Adds new patron to patronFile.txt"""  
	patronFile = open('patronFile.txt', 'a')
	patronFile.write((','.join([firstName,lastName]) + '\n'))
	patronFile.close()

def check(self, firstName='', lastName=''):
	"""Checks file for existing patron."""
	patronFile = open('patronFile.txt', 'r')
	for line in patronFile:
		line = line.rstrip('\n').split(',')
		if line[2] == lastName and line[1] == firstName:
			patronFile.close()
			return line
	return False
