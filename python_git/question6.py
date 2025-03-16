day1 = 'monday'
day2 = 'tuesday'
day3 = 'wednesday'
day4 = 'thursday'
day5 = 'friday'
day6 = 'saturday'
day0 = 'sunday'

day = int(input('enter todays day: '))
elapsed_day = int(input('enter the number of days elapsed since today: '))

future_day = day + elapsed_day


if future_day == 2:
	if day == 1:
		day = 'monday'
		print(f'today is {day} and the future day is tuesday')

if future_day == 3:
	if day == 2:
		day = 'tuesday'
		print(f'today is {day} and the future day is wednesday')

if future_day == 4:
	if day == 3:
		day = 'wednesday'
		print(f'today is {day} and the future day is thursday')

if future_day == 5:
	if day == 4:
		day = 'thursday'
		print(f'today is {day} and the future day is friday')

if future_day == 6:
	if day == 5:
		day = 'friday'
		print(f' today is {day}and the future day is saturday')

if future_day == 7:
	if day == 6:
		day = 'saturday'
		print(f'today is {day} and the future day sunday')

if future_day == 0:
	if day == 0:
		day = 'sunday'
		print(f'today is {day} and the future is sunday')
	








