from List import LinkedList

new_list = LinkedList()

# ----- TESTING APPEND ----- #
new_list.append('First')
new_list.append('Second')
new_list.append('Third')

# ----- TESTING GET ----- #
new_list.prepend('Now it is first')

print(new_list)

# ----- TESTING GET ----- #
try:
	print(new_list.get(2))
	print(new_list.get(3))
except IndexError:
	print("Error message: Out of Index")

# ----- TESTING LEN ----- #
print(len(new_list))
print(new_list.length())