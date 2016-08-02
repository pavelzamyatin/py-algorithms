def arabic_to_roman(arabic_number):

    roman_number = ''

    translation = [
        { 1 : 'I' , 5 : 'V', 10 : 'X'},
        { 1 : 'X' , 5 : 'L', 10 : 'C'},
        { 1 : 'C' , 5 : 'D', 10 : 'M'},
        { 1 : 'M' },
    ]

    numbers = [int(i) for i in str(arabic_number)]
    
    array_numbers = []

    for num in numbers:
        if num > 8: 
            array_numbers.append([1,10])
        elif num < 4:
            array_numbers.append([1 for i in range(num)])
        elif num > 5:
            array_numbers.append([5] + [1 for i in range(num%5)])
        else: 
            array_numbers.append([1 for i in range(5 - num)] + [5])

    array_numbers.reverse()

    for i in range(len(array_numbers)):
        block = array_numbers[i]
        blockstr = ''
        for num in block:
            blockstr += translation[i][num]
        roman_number = blockstr+roman_number

    return roman_number

# tests
print(arabic_to_roman(4))
print(arabic_to_roman(67))
print(arabic_to_roman(539))
print(arabic_to_roman(2168))
