# This is problem 1 from https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
nums_that_are_multiples = []
for i in range(1,1001):
    if (i%3 == 0) or (i%5 == 0):
        nums_that_are_multiples.append(i)

print(nums_that_are_multiples)
print(sum(nums_that_are_multiples))
