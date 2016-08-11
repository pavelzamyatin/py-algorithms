from List import LinkedList

lst = LinkedList()
new_lst = LinkedList()

# ----- TESTING APPEND ----- #
lst.append('First')
lst.append('Second')
lst.append('Third')
new_lst.append('Only one element')

# ----- TESTING GET ----- #
lst.prepend('Now it is first')

print(lst)

# ----- TESTING GET ----- #
try:
	print(lst.get(2))
	print(lst.get(3))
except IndexError:
	print("IndexError: Out of Index")

# ----- TESTING LEN ----- #
print('Len method:', len(lst))
print('Length method:', lst.length())

# ----- TESTING POP ----- #
print('Pop method result:', lst.pop())
print(lst)
print('Len after pop:', len(lst))


print('New list:', new_lst)
print('Pop method result:', new_lst.pop())
print('New list after pop:',new_lst)