import random, time

LIST = [i for i in range(1,2000)]

def decorator_time(func):
    """This function adds time value of execution of original sort
    func and return sort list and time in sec"""

    def wrapper(*args, **kwargs):
        
        start = time.time()
        lst = func(*args, **kwargs)
        stop = time.time() - start

        return lst, stop

    return wrapper

def find_divs_for_num(num):
	"""Function can find all divisors for number"""

	list = []

	for i in range(1, num-1):
		if num%i == 0:
			list.append(i)

	return list

dict = {num:find_divs_for_num(num) for num in LIST}

# for key, value in dict.items():
# 	print(key, ':' ,value)

@decorator_time
def find_amicable_numbers(lst):

	amicable_dict = {}

	for num in lst:
		for key, value in dict.items():
			if num == sum(value) and key == sum(find_divs_for_num(num)) and num != key :
				amicable_dict[num] = key

	return amicable_dict


# ----- TESTS ----- #

result, time = find_amicable_numbers(LIST)

print('-------')
print('RANGE FROM 1 TO', len(LIST))
print('RESULT:', result)
print('TIME:', round(time, 5), 'sec')