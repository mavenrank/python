# Reverse the given sumber and print it.
num = 12345
print(str(num)[::-1])

num = int(input("Enter a number to be reversed : "))
rev = 0
temp = num
while (temp!=0):
    r = temp % 10
    rev = rev*10 + r
    temp = int(temp/10)
print(rev)
