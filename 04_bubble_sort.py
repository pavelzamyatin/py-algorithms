import random, time

unsorted_list = [random.randrange(0,99) for i in range(0,99)]
random.shuffle(unsorted_list)

#print('Unsorted list = ', unsorted_list)

def decorator_time(func):

    def wrapper(*args, **kwargs):
        
        start = time.time()
        lst = func(*args, **kwargs)
        stop = time.time() - start

        return lst, stop

    return wrapper

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

bubble_sorted_list, sec1 = bubble_sort(unsorted_list)
shaker_sorted_list, sec2 = shaker_sort(unsorted_list)


print('[BUBLE ] Sorted list:', bubble_sorted_list)
print('[SHAKER] Sorted list:', shaker_sorted_list)

print('[BUBLE ] Time to sort:', round(sec1, 6), 'sec')
print('[SHAKER] Time to sort:', round(sec2, 6), 'sec')