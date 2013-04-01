from patronMod import patron
from bookMod import book
from fileInteraction import *

# patron = patron(lastName, firstName)

books = ['thisOne','andThisOne']
bookString = ','.join(books)
newPatron('bill','minear',bookString)