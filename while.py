number = 23
running = True

while running:
	guess = int(input('Enter a integer: '))

	if guess == number:
		print('you guessed it.')
		running = False

	elif guess < number:
		print('it is a little higher than that.')

	else:
		print('it is a little lower than that.')

else:
	print('the while loop is over')

print('done')