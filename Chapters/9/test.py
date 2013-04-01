import random

def getRandPic():
	imageDictionary = {0:'cat.gif', 1:'guy.gif', 2:'earthImage.gif'}
	randImage = imageDictionary[random.randrange(0,3)]
	return randImage

print getRandPic()