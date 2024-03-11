


# Write a program to find prime number with in a range using function.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print("Prime numbers within the range:")
for num in range(start_range, end_range + 1):
    if is_prime(num):
        print(num)


# Output:
# Enter the start of the range: 1
# Enter the end of the range: 20
# Prime numbers within the range:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
