# program number 18
# Find the number of zeros in a given number
num = input("Enter a sample number : ")
ctr = 0
for i in str(num):
    if i == '0':
        ctr += 1
print(ctr)

num = int(input("Enter a number : "))  # 1000
x = num
ctr = 0
flag = True
while (flag):
    rem = x % 10
    if rem == 0:
        ctr += 1
    x = int(x / 10)                     #hack used here
    if x == 0:
        flag = False
print(ctr)