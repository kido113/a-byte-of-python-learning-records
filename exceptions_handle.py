try:
	text = input('enter something -->')
except Exception as e:
	print(e)
else:
	print('you entered {}'.format(text))