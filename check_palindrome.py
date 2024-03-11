
#Write a program to check palindrome.
def is_palindrome(n):
    return str(n) == str(n)[::-1]

number = int(input("Enter a number to check if it's a palindrome: "))

if is_palindrome(number):
    print("Yes, the number is a palindrome.")
else:
    print("No, the number is not a palindrome.")


#Output: Enter a number to check if it's a palindrome: 12321
#Yes, the number is a palindrome.
#Enter a number to check if it's a palindrome: 12345
#No, the number is not a palindrome.
