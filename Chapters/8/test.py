from fileInteraction import *
from patronMod import patron

# newPatron('bill', 'minear', '3')

# try:
newPatron = patron(checkForPatron('bill','minear'))
print newPatron
# except TypeError:
# 	print 'Patron not found.'
