#This problem can be found at https://projecteuler.net/problem=7

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

# Idea/pseudocode:
# function that increments a number and checks if it had any prime divisors
# would be good to add newly discovered primes to a list
# the function could then check and use the list for prime divisors for each increment

#if perfectly divisible by another prime, it isn't a prime
# if not it COULD be a prime, gotta check the next prime until all primes are checked

import time
import math

#slow program
# prime_nums = [2,3] # I'll start with the first two primes
# nth_prime_index = 2
# num_to_check = 3
#
# while nth_prime_index < 10002:
#     num_to_check = num_to_check + 1
#     for prime in prime_nums:
#
#         if num_to_check % prime == 0:
#             break
#         elif prime_nums.index(prime) == len(prime_nums) - 1 :
#             nth_prime_index = nth_prime_index + 1
#             prime_nums.append(num_to_check)
#             print(prime_nums[-10:])




#FASTER PROGRAM
#I realized that I don't have to make it check ALL of the previous primes
#Example, say im checking the number 18.  It would make no sense to check 17 because 17*2 (the smallest prime) is 34 which is already way bigger than 18.
# for that same reason if Im testing 18 I also wouldn't need to test 13  or 11,

prime_nums = [2,3] # I'll start with the first two primes
nth_prime_index = 2
num_to_check = 3

while nth_prime_index < 10001:
    num_to_check = num_to_check + 1
    for prime in prime_nums:

        if num_to_check % prime == 0:
            break
        elif prime_nums.index(prime) == math.floor((len(prime_nums))/2):
            nth_prime_index = nth_prime_index + 1
            print(nth_prime_index)
            prime_nums.append(num_to_check)
            break

print(prime_nums)
print(prime_nums[10000])

#Output
 # [2,3,5 . . .
# 02199, 102203, 102217, 102229, 102233, 102241, 102251, 102253, 102259, 102293, 102299, 102301, 102317, 102329, 102337, 102359, 102367, 102397, 102407, 102409, 102433, 102437, 102451, 102461, 102481, 102497, 102499, 102503, 102523,
#  102533, 102539, 102547, 102551, 102559, 102563, 102587, 102593, 102607, 102611, 102643, 102647, 102653, 102667, 102673, 102677, 102679, 102701, 102761, 102763, 102769, 102793, 102797, 102811, 102829, 102841, 102859, 102871, 10287
# 7, 102881, 102911, 102913, 102929, 102931, 102953, 102967, 102983, 103001, 103007, 103043, 103049, 103067, 103069, 103079, 103087, 103091, 103093, 103099, 103123, 103141, 103171, 103177, 103183, 103217, 103231, 103237, 103289, 103
# 291, 103307, 103319, 103333, 103349, 103357, 103387, 103391, 103393, 103399, 103409, 103421, 103423, 103451, 103457, 103471, 103483, 103511, 103529, 103549, 103553, 103561, 103567, 103573, 103577, 103583, 103591, 103613, 103619, 1
# 03643, 103651, 103657, 103669, 103681, 103687, 103699, 103703, 103723, 103769, 103787, 103801, 103811, 103813, 103837, 103841, 103843, 103867, 103889, 103903, 103913, 103919, 103951, 103963, 103967, 103969, 103979, 103981, 103991,
#  103993, 103997, 104003, 104009, 104021, 104033, 104047, 104053, 104059, 104087, 104089, 104107, 104113, 104119, 104123, 104147, 104149, 104161, 104173, 104179, 104183, 104207, 104231, 104233, 104239, 104243, 104281, 104287, 10429
# 7, 104309, 104311, 104323, 104327, 104347, 104369, 104381, 104383, 104393, 104399, 104417, 104459, 104471, 104473, 104479, 104491, 104513, 104527, 104537, 104543, 104549, 104551, 104561, 104579, 104593, 104597, 104623, 104639, 104
# 651, 104659, 104677, 104681, 104683, 104693, 104701, 104707, 104711, 104717, 104723, 104729, 104743]

#10001st prime 104743



