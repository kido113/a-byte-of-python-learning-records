print('simple assignment')
shoplist = ['apple','mango','carrot','banana']
mylist = shoplist

del shoplist[0]

print('shoplist is',shoplist)
print('mylist',mylist)

print('copy by making a full slice')
mylist = shoplist[:]
del mylist[0]
del shoplist[1]

print('shoplist is ',shoplist)
print('mylist is',mylist)