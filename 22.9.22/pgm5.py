# Print all the numbers from 1 to 100
flag = True
n = 0
while (flag):
    print(n)
    n += 1
    if n > 100:
        flag = False

# method 2
for i in range(1, 100):
    print(i)


# method 3
ctr = 0
while (True):
    print(ctr)
    if ctr > 100:
        break
    ctr = ctr + 1
