# Print all the numbers from 100 to 0

flag = True
n = 100
while (flag):
    if n < 0:
        flag = False
    else:
        print(n)
        n -= 1
