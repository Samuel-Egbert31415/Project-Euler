#This problem can be found at https://projecteuler.net/problem=6
#----------------------------------------------------------------
#The sum of the squares of the first ten natural numbers is:
# 1^2 + 2^2 . . . 10^2 = 385
#The square of the sum of the first ten natural numbers is:
# (1 + 2 +  . . . + 10)^2 = 3025
#The difference between the sum of squares and the square of the sum is:
#3025 - 385 = 2640
#Find the difference between sum of squares of the first 100 natural numbers and the square of the sum
#------------------------------------------------------------------
square_of_sums_list = []
sum_of_squares_list = []
differences = []
ratios = [] # just for fun :)
for natural_number in range(1,101):
    square_of_sums = sum(range(1, natural_number + 1))**2
    square_of_sums_list.append(square_of_sums)

    sum_of_squares = sum(map(lambda n: n**2, range(1, natural_number + 1)))
    sum_of_squares_list.append(sum_of_squares)

    differences.append(square_of_sums - sum_of_squares)
    ratios.append(square_of_sums/sum_of_squares)

print("Differences:", '\n', differences, '\n')
print("Ratios:", '\n', ratios)




