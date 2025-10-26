"""Task is 
Write a Program to find smallest and largest numbers in list"""

numbers = []
n = int(input("How many numbers do you want to enter? "))
for i in range(n):
    num = int(input(f"Enter number {i + 1} "))
    numbers.append(num)
largest = numbers[0]
smallest = numbers[04]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Numbers entered:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
"""Output is
How many numbers do you want to enter? 4
Enter number 1 10
Enter number 2 20
Enter number 3 30
Enter number 4 40
Numbers entered: [10, 20, 30, 40]
Largest number: 40
Smallest number: 10"""