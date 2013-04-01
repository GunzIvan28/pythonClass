import md5

hash3 = '17c0f75d610ec414e5c9be1a6059b65a'

m = md5.new('ovaltine')
if m.hexdigest() == hash3:
	print 'Match!'
else:
	print 'Nope.'