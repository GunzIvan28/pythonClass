from paymod import Rates, Account

rate = Rates()
acc = Account(rate.itemCalcs(2000.00))
print acc
print acc.loanLength()

# while True:
# 	try:
# 		price = input("Enter the item's value: ")
# 		break
# 	except (NameError, SyntaxError):
# 		print 'Value not numeric. Press ENTER and try again.'


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