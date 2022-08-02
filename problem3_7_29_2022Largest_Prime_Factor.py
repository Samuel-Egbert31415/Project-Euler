#The problem can be found at https://projecteuler.net/problem=3

#-------------------------------------------------------------------
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#--------------------------------------------------------------------

#This loop will find primes, then use those primes to see if they are prime factors
#of 600851475143.  It will continue to find primes until 600851475143 is completetly factored

import sympy # To reduce computational complexity,
             # it makes sense to grab the primes from a library.

# import time
the_next_prime = 0 # just to start at the smallest primes going upward

quotient = 600851475143 # will be the big number divided by our primes as we go. We will initialize it as the big number to start

prime_divisors = []

# Take the big number and divide it by a prime
# keep dividing it till you can't
# go on to the next prime and divide till can't

while (sympy.isprime(quotient) == False) and (quotient != 1):  #if the quotient is prime, we know we are done

    #Try to divide the quotient by the next known prime as many times as possible
    while (quotient / sympy.nextprime(the_next_prime)).is_integer() == True:
        prime_divisors.append(sympy.nextprime(the_next_prime))
        quotient = quotient / sympy.nextprime(the_next_prime)
        print(prime_divisors)

    #When we can't we will find the next prime on the number line to try
    else:
        the_next_prime = sympy.nextprime(the_next_prime)

print(prime_divisors)

# the output is [71, 839, 1471, 6857]
# 6857 is the biggest prime factor







