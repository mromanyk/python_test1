import random

# Generate a list of 100 random numbers from 1 to 1000
random_numbers = [random.randint(1, 1000) for _ in range(100)]

# Bubble sort implementation
def bubble_sort(array):
    n = len(array)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

# Print the original list
# print("Original list:")
# print(random_numbers)

# Sort the list
bubble_sort(random_numbers)

# Print the sorted list
# print("Sorted list:")
# print(random_numbers)

# Sum only the even numbers
even_sum = 0
even_number = 0
for num in random_numbers:
    if num % 2 == 0:
        even_number += 1
        even_sum += num
even_averagevalue = even_sum/even_number
# print("Sum of even numbers: ", even_sum, "even_number: ", even_number)
print("even_averagevalue: ", even_averagevalue)

# Sum only the odd numbers
odd_sum = 0
odd_number = 0
for num in random_numbers:
    if num % 2 != 0:
        odd_number += 1
        odd_sum += num
odd_averagevalue = odd_sum/odd_number
# Print the sum of the odd numbers
# print("Sum of odd numbers:", odd_sum, "odd_number: ", odd_number)
print("odd_averagevalue: ", odd_averagevalue)