from paymod import Rates, Item, Account

rate = Rates()

while True:
	try:
		price = input("Enter the item's value: ")
		break
	except (NameError, SyntaxError):
		print 'Value not numeric. Press ENTER and try again.'

item = Item(price, rate.downPay, rate.interest, rate.payment)
acc = Account(item.startPrice, item.payment)
print item
print acc

for i in xrange(0, 12):
	if i == 0:
		print item.startPrice
	else:
		print acc.totalBalance - (item.payment * i)