import math

# #####
# This file was written by Gary Guo on October 3rd 2016
# To be submitted for the Swift Navigation Software Engineering application.
# At Hive we do not write tests for our code.
# At Hive we do not write formal documentation, we use comments
# however I am not against writing tests or documents
# it's just something that we didn't need at our size :)
# #####

# This function returns the first n Fibonacci numbers printing special strings:
# 'Buzz' if F(n) is divisible by 3
# 'Fizz' when F(n) is divisible by 5
# 'FizzBuzz' when F(n) is divisible by 15
# 'BuzzFizz' when F(n) is prime
# the value F(n) otherwise
# WARNING this function experiences performance latency with input ~> 70


def swift_fibonacci_fizz_buzz(n):
    if n < 1:
        # early out if input is less than 1
        return ''

    output_list = ['1']

    # We are implementing a fibonacci sequence starting with 1
    prev = 0
    current = 1
    for i in range(1, n):
        _prev = prev
        prev = current
        current += _prev
        if current % 3 == 0:
            # if divisible by 3 print 'Buzz'
            output_list.append('Buzz')
        elif current % 5 == 0:
            # if divisible by 5 print 'Fizz'
            output_list.append('Fizz')
        elif current % 15 == 0:
            # if divisible by 15 print 'BuzzFizz'
            # note that there is a potential to combine logic here with 3 and 5
            # code is cleaner and easier to read/maintain with seperated logic
            output_list.append('BuzzFizz')
        elif is_prime(current):
            # if prime print BuzzFizz
            output_list.append('BuzzFizz')
        else:
            # print the actualy number
            output_list.append(str(current))
    print ','.join(output_list)


# checks if a number is prime
# WARNING this function experiences performance latency with input ~> 10^15
def is_prime(n):
    if n == 1 or n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
