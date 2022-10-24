"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
if len(numbers) % 2 == 1:
    median = numbers[int((len(numbers))/2)]
    print(median)
else:
    middlevalue1 = numbers[int((len(numbers))/2)]
    middlevalue2 = numbers[int((len(numbers))/2)-1]
    median = (middlevalue1 + middlevalue2)/2
    print(median)
