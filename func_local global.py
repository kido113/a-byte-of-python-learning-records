x = 50

def func(x):
	print('x is ',x) #局部变量x = 全局变量x
	x = 2 #局部变量x改变
	print('changed local x to', x)

func(x)
print('x is still',x)





y = 50

def func2():#不需要形式参数
	global y #直接调用全局变量y

	print('y is ',y)
	y = 2 #全局变量y
	print('changed global y to ',y)

func2()
print('value of y is',y)