#prime number
#solution 1 fast approach
def prime_num_checker(number):
    if number % number == 0 and (number%2 != 0) and (number%3 !=0) and (number%5 !=0): 
        print("It is a prime number")
    elif number/2 == 1 or number/3==1 or number/5==1:
        print("It is a prime number")
    else:
        print("It is not a prime number")
prime_num_checker(89)
#solution 2 slower approach
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i ==0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It is not a prime number")
prime_checker(90)