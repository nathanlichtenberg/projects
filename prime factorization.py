from sympy import *

while True:
    number = int(input("> "))
    primefac = []
    while number != 1:
    #find the smallest prime factor of number
        for i in range(1,number + 1):
            if isprime(i) and number % i == 0:
                primefac.append(i)
                number //= i
                break
            
    print(primefac)
