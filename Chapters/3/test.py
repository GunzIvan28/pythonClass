from paymod import Rates, Account

rate = Rates()

while True:
	try:
		price = input("Enter the item's value: ")
		break
	except (NameError, SyntaxError):
		print 'Value not numeric. Press ENTER and try again.'

acc = Account(rate.itemCalcs(price))
# print acc
# print acc.loanLength()

# for i in xrange(0, 12):
# 	if i == 0:
# 		print item.startPrice
# 	else:
		# print acc.totalBalance - (item.payment * i)

# test = [1, 2, 3]
# acc.test(test)

# payTotal = [acc.payment]
# while payTotal[-1] < acc.startPrice:
# 	payTotal.append(payTotal[-1] + acc.payment)
# 	print len(payTotal)
	# print payTotal

# lastPay = acc.startPrice - payTotal
# print lastPay

print '%5s%14s%16s%10s%8s%18s' % \
	('Month', 'Current Total', 'Interest Amount',
	 'Principal', 'Payment', 'Balance Remaining')

print '%5s%14s%16s%10s%8s%18s' % \
	('-' * 5, '-' * 13, '-' * 15, '-' * 9,
	'-' * 7, '-' * 17)

for i in xrange(acc.loanLength()):
	print '%5d%14.2f%16.2f%10.2f%8.2f%18.2f' % \
		(i,
		acc.startPrice - acc.payment,
		acc.interest,
		acc.principal,
		acc.payment,
		acc.startPrice - acc.payment * (i +1))


# current total = starting price - payment * i
# remaining balance = starting price - payment * (i + 1)