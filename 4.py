# Write a program to check if the given number is a palindrome number.
number = int(input("Enter number:"))
temp = number
rev = 0
while(number > 0):
    digit = number % 10
    rev = rev*10+digit
    number = number//10
if (temp == rev):
    print("YES , IT IS PALLINDROME NUMBER !")
else:
    print("NO,IT IS NOT A PALLINDROME NUMBER !")