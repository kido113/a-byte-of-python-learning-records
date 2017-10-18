def print_max(a,b):
	if a > b:
		print (a, 'is maximum')
	elif a == b:
		print (a, 'is equal to', b)
	else:
		print(b, 'is maximum')

#直接传递字面值
print_max(3,4)

#参数形式传递变量
x = 5
y = 6
print_max(x,y)