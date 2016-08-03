import random, time

unsorted_list = [random.randrange(0,999) for i in range(0,999)]
random.shuffle(unsorted_list)

# print('Unsorted list = ', unsorted_list)

def decorator_time(func):
    """This function adds time value of execution of original sort
    func and return sort list and time in sec"""

    def wrapper(*args, **kwargs):
        
        start = time.time()
        lst = func(*args, **kwargs)
        stop = time.time() - start

        return lst, stop

    return wrapper

# https://en.wikipedia.org/wiki/Bubble_sort
@decorator_time
def bubble_sort(lst):

    
    left = 0
    right = len(lst)-1

    while left <= right:
        
        for i in range(left, right, +1):
            
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]

        right -= 1

    return lst

# https://en.wikipedia.org/wiki/Cocktail_shaker_sort
@decorator_time
def shaker_sort(lst):

    left = 0
    right = len(lst)-1

    while left <= right:

        for i in range(left, right, +1):
            
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]

        right -= 1

        for y in range(left,right, -1):

            if lst[y-1] > lst[y]:
                lst[y], lst[y-1] = lst[y-1], lst[y]

        left += 1

    return lst

# https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort
@decorator_time
def odd_even_sort(lst):

    left = 0
    right = len(lst)-1

    while True:

        counter = False

        for i in range(left, right):


            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                counter = True

        for i in range(left+1, right):

            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                counter = True

        if counter == False: break

    return lst

# ----- TESTS ----- #

bubble_sorted_list, sec1 = bubble_sort(unsorted_list)
shaker_sorted_list, sec2 = shaker_sort(unsorted_list)
odd_even_sorted_list, sec3 = odd_even_sort(unsorted_list)


print('[BUBLE  ] Sorted list:', bubble_sorted_list)
print('[SHAKER ] Sorted list:', shaker_sorted_list)
print('[ODDEVEN] Sorted list:', odd_even_sorted_list)

print('[BUBLE  ] Time to sort:', round(sec1, 5), 'sec')
print('[SHAKER ] Time to sort:', round(sec2, 5), 'sec')
print('[ODDEVEN] Time to sort:', round(sec3, 5), 'sec')