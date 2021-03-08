#File containing fizz buzz function

def TestFizzBuzz(x):
    count = 1 
    for number in range(100):
        if count % 3 == 0:
            print('Fizz')
            if count == x:
                return 'Fizz'
        count +=1
    return '0'
