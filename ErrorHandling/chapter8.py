

try:
    num = int(input('Enter a number less than 10: '))

    if num < 10:
        print('your number is', num)
    else:
        raise TypeError('Number is not less than 10')
    
except TypeError as e:
    print('Error Occured: ', e)