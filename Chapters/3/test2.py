#!/usr/bin/python

INT_RATE = .01
DOWN_RATE = .10
PAY_RATE = .05

price = input('Enter a price: ')
base = price - (price * DOWN_RATE)
balanceRemaining = base 
monthlyPrincipal = balanceRemaining * PAY_RATE
monthlyInterest = balanceRemaining * INT_RATE
monthlyPayment = monthlyPrincipal + monthlyInterest

while monthlyPayment == 0 or monthlyPayment > 0:
	print 


