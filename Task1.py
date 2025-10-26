""" Task is 
Write a Program to input marks of 5 subjects, calucate total,average and grade without using class"""


print("Enter a 5 subjects")
maths=int(input("enter a maths subject marks"))
Physics=int(input("enter a Pythics subject marks "))
Chemistry =int(input("enter a chemistry  subject marks"))
English=int(input("enter a English subject  marks"))
Computers=int(input("enter a computer subject  marks"))
total= maths+Physics+Chemistry+English+Computers
average=(total)/5

if average >= 90:
    grade = 'A+'
elif average >= 80:
    grade = 'A'
elif average >= 70:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 50:
    grade = 'D'
else:
    grade = 'F'
print("\n--- Results ---")
print("Total marks is", total)
print("Average  of the marks is",average)
print("Grade is ",grade)

"""Output is
Enter a 5 subjects
enter a maths subject marks10
enter a Pythics subject marks 20
enter a chemistry  subject marks30
enter a English subject  marks40
enter a computer subject  marks50

--- Results ---
Total marks is 150
Average  of the marks is 30.0
Grade is  F"""