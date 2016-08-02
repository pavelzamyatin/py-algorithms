import random, time

unsorted_list = [random.randrange(0,9999) for i in range(0,9999)]
random.shuffle(unsorted_list)

print('Unsorted list = ', unsorted_list)

def decorator_time(func):

    def wrapper(*args, **kwargs):
        
        start = time.time()
        lst = func(*args, **kwargs)
        stop = time.time() - start

        return lst, stop

    return wrapper

@decorator_time
def bubble_sort(lst):
    
    for x in range(len(lst)-1):
        
        for i in range(len(lst)-1):

            tmp = lst[i]
            
            if lst[i] > lst[i+1]:
                lst[i] = lst[i+1]
                lst[i+1] = tmp

    return lst

sorter_list, sec = bubble_sort(unsorted_list)

print('Sorted list:', sorter_list)
print('Time to sort:', round(sec, 3), 'sec')