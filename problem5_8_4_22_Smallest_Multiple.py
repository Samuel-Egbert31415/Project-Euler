#This problem can be found at https://projecteuler.net/problem=5
#============================================================
# """2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20"""?
#==============================================================


# Thoughts
# Invoking the fundamental theorem of arithmetic, we have to start with
# number >= 2*3*5*7*11*13*17*19
print("The number we are looking for is at least this big:", 2*3*5*7*11*13*17*19)
# 9699690
#for a number to be divisible by 4 it must be divisible by 2 multiplicity 2
#the number is already divisible by 6 (2*3)
# for a number to be divisible by 8 it must be divisible by 2 multiplicity 3
#  . . . 9, divisible by 3 multiplicity 2
# already divisible by 10 (2*5)
# will be divisible by 12 (2*2*3) because of multiplicity
# already divisible by 14 (2*7)
#  . . . 15 (3*5)
# . . . 16, need 2 in multiplicity 4
# . . . 18 (2*9)
# . . . 20 (5*2*2)

# therefore all we need is three more 2 factors, and one more 3 factor
answer = (2**4)*(3**2)*5*7*11*13*17*19
print("The Answer:", answer)
# The Answer: 232792560

check_list = []
for A in range(2,21):
    if answer % A == 0:
        check_list.append(1)
    else:
        check_list.append(0)

print("check_list:",check_list)

# check_list: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

#Ok so I just used logic through that one, should I do a more brute force method?


