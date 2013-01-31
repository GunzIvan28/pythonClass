#/usr/bin/python

"""
Program: TidBit Computer Store's Payment Schedule
Author: Bill Minear

Purpose:
"""
import os
osName = os.name # For use in clrScr
DOWN_PAYMENT = .10
INTEREST_RATE = .01
MONTHLY_PAYMENT = .05

# Clears screen
def clrScr(osName):
	if osName == 'posix':
		os.system('clear')
	elif osName == 'dos' or osName == 'nt':
		os.system('cls')

while True:
	try:
		clrScr(osName)
		purchasePrice = input('Purchase price: ')
		break
	except (NameError, SyntaxError):
		tryAgain = raw_input('Invalid input. Press ENTER to try again.')

realDownPayment = purchasePrice * DOWN_PAYMENT

currentBalance = (purchasePrice - DOWN_PAYMENT) * MONTHLY_PAYMENT

paymentWithInterest = currentBalance + (currentBalance * INTEREST_RATE)

print realDownPayment
print currentBalance
print '%.2f' % paymentWithInterest