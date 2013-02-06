#!/usr/bin/python

INT_RATE = .01
DOWN_RATE = .10
PAY_RATE = .05

price = input('Enter a price: ')
downPayment = price * DOWN_RATE
base = price - downPayment
balanceRemaining = base
monthlyPrincipal = base * PAY_RATE
monthlyInterest = balanceRemaining * INT_RATE
monthlyPayment = monthlyPrincipal + monthlyInterest
i = 1

while balanceRemaining > 0.00:
	print i, balanceRemaining, '\t', monthlyPrincipal, '\t', monthlyInterest,'\t', monthlyPayment
	balanceRemaining = balanceRemaining - monthlyPayment
	monthlyInterest = balanceRemaining * INT_RATE
	monthlyPayment = monthlyPrincipal + monthlyInterest
	i += 1

