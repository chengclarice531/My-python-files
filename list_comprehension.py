#using for
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []

for x in fruits:
	newlist.append(x)
print('This is the newlist: ', newlist)

#using list comprehension
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = [x for x in fruits]
print('Producing newlist by using list comprehension: ', newlist)
newlist = [x for x in fruits if x!= 'apple']
print("Newlist without apple:", newlist)
newlist = [x for x in range(10)]
print(newlist)
# uppercase the outcome
newlist = [x.upper() for x in fruits]
print('uppercase the list: ', newlist)
# set all outcomes to hello
newlist = ['hello' for x in fruits]
print('all outcomes are hello: ', newlist)
#return orange instead of banana
newlist = [x if x!= 'banana' else 'orange' for x in fruits]
print('replace banana with orange: ', newlist)
