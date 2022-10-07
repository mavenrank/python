# program number 14, 15, 16 & 17
# Find the biggest among two, three, ten and n numbers
def maxnum(*numbers):
    print(type(numbers))  # -> takes as a tuple
    largest_num = numbers[0]
    for i in numbers:

        if i > largest_num:
            largest_num = i
    return largest_num


print(maxnum(-23, -264, -23, -244))
