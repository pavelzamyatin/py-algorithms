import random, time

LST = [i for i in range(1,4000)]

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

    return [i for i in range(1, int(num/2)+1) if num%i == 0]

@decorator_time
def find_amicable_numbers(lst):

    num_div_dict = {num:find_divs_for_num(num) for num in LST}
    amicable_list = []

    for key, value in num_div_dict.items():
        print(key, ':' ,value)    

    for num in lst:
        for key, value in num_div_dict.items():
            if num == sum(value) and key == sum(num_div_dict[num]) and num != key :
                amicable_list.append({num:num_div_dict[num]})


    return amicable_list


# ----- TESTS ----- #

result, time = find_amicable_numbers(LST)

print('RANGE FROM 1 TO', len(LST))
print('RESULT:')

for num in result:
    print(num)
print('-------')
print('TIME:', round(time, 5), 'sec')