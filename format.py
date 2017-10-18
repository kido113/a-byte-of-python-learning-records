#format

print ('{0:.3f}'.format(1.0/3))
print ('%.3f' %1.52)

print ('%s' %'hello')
print ('{}' .format('hello'))

print ('{0} {1} {1}' .format('hello','hi'))

print ('{:>08}'.format(12))
print ('{:>8}'.format(12))
print ('{:^8}'.format(12))

print ('a', end = '')
print ('b', end = ' ')
print ('c')