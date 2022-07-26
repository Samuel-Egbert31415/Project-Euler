#This problem can be found at https://projecteuler.net/problem=2

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

even_fibonacci_nums = [] #that do exceed 4x10^6


prev_sequence_value = 1 # so that the while-loop doesn't throw and error upon first run through
sequence_value = 1

while sequence_value < 4000001:
    if sequence_value%2 == 0:
        even_fibonacci_nums.append(sequence_value)
    holder_value = sequence_value # so that prev_sequence_value can be set to it as the new previous
    sequence_value = sequence_value + prev_sequence_value
    prev_sequence_value = holder_value

#End Loop


print(even_fibonacci_nums[:100]) # wow there actually aren't that many even nums_in the seq
print(sum(even_fibonacci_nums))



