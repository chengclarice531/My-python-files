print('\\ for loop \\')
print(' loop through a list:')
thislist = ['apple', 'banana', 'cherry']
for x in thislist:
	print('  ' + x)
print(' loop through the index numbers:')
for i in range(len(thislist)):
	print('  ' + thislist[i])
print(' using list comprehension:')
[print('  ' + x) for x in thislist]
print('\\ while loop \\')
thislist = ['apple', 'banana', 'cherry']
i = 0
while i < len(thislist):
	print('  ' + thislist[i])
	i += 1

