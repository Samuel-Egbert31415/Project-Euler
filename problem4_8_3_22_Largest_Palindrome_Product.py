#This problem can be found at https://projecteuler.net/problem=4
#================================================================
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#=================================================================

#pseudo-code idea
# two for loops nested for product A*B
# one loop to iterate across all 3 digit A for a given B
# one loop to increment B
# as we do this, check if palindrome and add to a list
# at the end find the max of the list

# other thoughts about idea:
# keep in mind commutative property (2*8 = 8*2), so that means I can cut computation in half if I consider this symmetry
# By what fraction does it reduce computation, my intuition is 1/2, maybe not worth the extra effort?
# perhaps I'll come back to a faster algorithm as a stretch goal

import time

palindromes = []

#less computationally efficient code

for A in range(1,1000):
    print('loop A====', A)
    for B in range(1,1000):
        time.sleep(0.000001)
        wordy_number = str(A*B) # since strings are subscriptable, they are easy to reverse :)
        if wordy_number == wordy_number[::-1]:
            print('ifloop')
            print('palindrome', wordy_number)
            palindromes.append(int(wordy_number))

palindromes.sort(reverse = True)
print(palindromes)

#stretch goal, more computationally efficient code












