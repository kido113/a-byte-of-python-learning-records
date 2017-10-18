def say(massage, times=1):
	print(massage * times)

say('hello')
say('world',5)

def func(a, b = 5, c = 10):
	print('a is',a, 'b is', b, 'c is',c)

func(3,7)
func(10,c = 6)
func(b = 2,c = 9,a = 8)