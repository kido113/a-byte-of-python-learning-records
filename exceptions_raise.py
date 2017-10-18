class ShortInputException(Exception):
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	text = input('enter something-->')
	if len(text) < 3:
		raise ShortInputException(len(text),3)
	#其他工作可继续正常运行
except EOFError:
	print('why didi do an EOF on me?')
except ShortInputException as ex:
	print(('ShortInputException: the input was ' + 
			'{0} long, expect at least {1}').format(ex.length, ex.atleast))
else:
	print('no Exception was raised.')
		