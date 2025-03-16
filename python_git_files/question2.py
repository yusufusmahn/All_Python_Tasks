number1 = int(input('enter first integer: '))
number2 = int(input('enter second integer: '))
number3 = int(input('enter third integer: '))

if number1 >= number2 and number1 >= number3:
	maximum = number1
	if number2 >= number3: 
		second_maximum = number2
		least_maximum = number3
	else:
		second_maximum = number3
		least_maximum = number2

elif number2 >= number1 and number2 >= number3:
	maximum = number2
	if number1 >= number3: 
		second_maximum = number1
		least_maximum = number3
	else:
		second_maximum = number3
		least_maximum = number1

elif number3 >= number1 and number3 >= number2:
	maximum = number3
	if number1 >= number2:
		second_maximum = number1
		least_maximum = number2
	else:
		second_maximum = number2
		least_maximum = number1


print('output: ',least_maximum,second_maximum,maximum)




