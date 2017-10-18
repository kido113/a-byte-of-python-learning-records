poem = '''\
Programming is fun
When the work is done
if youwanna make your work also fun:
	use Python!
'''

#打开文件编辑
f = open('poem.txt','w')
#向文件中编写文本
f.write(poem)
f.close()


#如果没有特别指定。将假定启用阅读模式
f = open('poem.txt')
while True:
	line = f.readline()
	#零长度指示EOF
	if len(line) == 0:
		break
	#每行末尾
	#都有换行符
	#因为是从一个文件提取的
	print(line,end = '')
f.close()
