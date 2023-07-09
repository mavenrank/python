# Find the sum of all the digits of a number

number = int(input("Enter the number : "))
sum = 0
total_digits = 0
remainder = 0
flag = True
while (flag):
    remainder = number % 10
    print("Remainder is : " + str(remainder))
    sum = sum + remainder
    number = int(number / 10)
    # this is important - we need the integral part,
    # by converting to int we get only the integral part
    if (number == 0):
        flag = False
    total_digits = total_digits + 1

print("Total digits ", total_digits)
print("Sum of digits:", sum)
