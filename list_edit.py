print('Change list items')
thislist = ['apple', 'banana', 'cherry', 'melon']
print(thislist)
thislist[2] = 'strawberry'
print(thislist)
thislist[1:3] = ['lime', 'eggplant']
print(thislist)
thislist[1:2] = ['watermelon', 'durian']
print(thislist)
thislist[1:3] = ['corn']
print(thislist)
thislist.insert(3, 'lemon')
print(thislist)

print('Add list items')
thislist = ['apple', 'banana', 'cherry', 'melon']
print(thislist)
thislist.append('orange')
print(thislist)
thislist.insert(3, 'strawberry')
print(thislist)
tropical = ['mango', 'pineapple', 'jackfruit', 'papaya']
thislist.extend(tropical)
print(thislist)
thistuple = ("kiwi", "cherry tomato")
thislist.extend(thistuple)
print(thislist)

print('Remove list items')
thislist.remove('orange')
#If more than one item with same specified value, the remove() method removes the first occurrence.
print(thislist)
thislist.pop(2)
print(thislist)
thislist.pop()
print(thislist)
del thislist[0]
print(thislist)
thisdellist = ['apple', 'banana']
del thisdellist
thislist.clear()
print(thislist)
#clear only empties the list, but del remove the entire list
