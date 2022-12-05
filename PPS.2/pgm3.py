# check length
# 1 integer - prime check -> rev string, swap real and imagine part in complex
# 2 string - palindrome check -> complex conjugated, integers negated
# 1 & 2 satisfied -> print middle element
# none satisfied -> string converted to list object


def check_prime(number):
    # If given number is greater than 1
    flag = False
    if number > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(number/2)+1):
            # If number is divisible by any number between
            # 2 and n / 2, it is not prime
            if (number % i) == 0:
                flag = False  # (number, "is not a prime number")
                break
        else:
            flag = True  # (number, "is a prime number")
    else:
        flag = False  # print(number, "is not a prime number")
    return flag


def check_palindrome(string):   
    flag = False
    string = string.lower()
    rev = string[::-1]
    if rev == string:
        flag = True
    else:
        flag = False
    print(flag)
    return flag


def is_complex(number):
    if number.__class__.__name__ == "complex":
        return True
    else:
        return False


def conjugate(complex_number):
    return complex_number.conjugate()


def swap_complex_number(complex_number):
    print(complex_number)
    r = complex_number.real
    i = complex_number.imag
    return complex(i, r)


def reverse_string(string):
    return string[::-1]

# sample = [(5+3j),”Madam”, 6, -1]


def process(sample_list):
    # first condition
    is_prime = False
    is_palindrome = False
    for item in sample_list:
        t = item.__class__.__name__
        if t == "int":
            is_prime = check_prime(item)  # condition 1
        elif t == "str":
            is_palindrome = check_palindrome(item)  # condition 2
            

    result_list = []

    for item in sample_list:
        if is_prime:  # first condition
            print("is_prime")
            t = item.__class__.__name__
            if t == "int":
                result_list.append(item)
            elif t == "str":
                result_list.append(reverse_string(item))
            elif t == "complex":
                result_list.append(swap_complex_number(item))

        elif is_palindrome:  # second condition
            print("is_palindrome")
            t = item.__class__.__name__
            if t == "int":
                result_list.append(-item)
            elif t == "str":
                result_list.append(reverse_string(item))
            elif t == "complex":
                result_list.append(conjugate(item))

        elif is_prime and is_palindrome:  # both satisfied
            print("both")
            n = len(sample_list/2)
            result_list.append(sample_list[n])

        elif (not is_prime and not is_palindrome):  # not satisfied
            print("neither")
            t = item.__class__.__name__
            if t == "str":
                result_list.append(list(item))
            else:
                result_list.append(item)

    return result_list


#print(process([(5+3j),"madam", 6, -1]))
# x print(process(["Hello", "Python", 3, 25, (-1+7j)]))
print(process(["Malayalam", (3+3j), (7-2j), "CSE",7]))
#print(process(["Hello", 12,(3-8j)]))
# print(process([111]))
