from fileInteraction import *
from patronMod import patron
from bookMod import book

# newPatron('bill', 'minear', '3')
bookInfo = checkForBook('aBook','me')
if bookInfo != False:
	theBook = book(bookInfo)
	updateBook(theBook.returnForWriting())
