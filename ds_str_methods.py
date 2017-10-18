name = 'swaroop'

if name.startswith('swa'):
	print('yes')

if 'a' in name:
	print('yes2')

if name.find('war')!= -1:#找不到字符串返回-1
	print('yes3')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))#join 联结