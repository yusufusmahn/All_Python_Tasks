number = int(input('enter a number btw 0 and 1000: '))
sum = 0
while number != 0:
	sum = sum + number
	number = int(input('enter a number btw 0 and 1000: '))
print('the sum of all its digits is:',sum)