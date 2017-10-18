ab ={
	'Swaroop': 'swaroop@swaroopch.com',
	'Larry': 'larry@wall.org',
	'Matsumoto': 'matz@ruby-lang.org',
	'Spammer': 'spammer@hotmall.com'
}
print("Swaroop's address is", ab['Swaroop'])

del ab['Spammer']

print('\nthere are {} contacts in the ab\n'.format(len(ab)))

for name, address in ab.items():
	print('contact{} at{}'.format(name, address))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
	print("Guido's address is",ab['Guido'])


