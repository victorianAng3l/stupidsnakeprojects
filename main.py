inputted = int(input("Input Number Here: "))
is_prime = 0
happy_number_sum = 0
is_happy = 0
happy_loop_count = 0
print("Calculating...", end="")
def mersenne_test(inp):
    global is_mersenne
    i = 1
    while ((2 ** i) - 1) != inp:
        if i >= 1000:
            is_mersenne = 0
            break
        else:
            i += 1
    else:
        is_mersenne = 1
    if is_mersenne == 1:
        return "a mersenne prime"
    else:
        return "prime"
def odd_check(inp):
    if str(float(inp/2)) == str(float(int(inp/2))):
        print("\r" + str(inp) + " is an even number.")
    else:
        print("\r" + str(inp) + " is an odd number.")
def happy_check(inp):
    global happy_number_sum, is_happy, happy_loop_count
    happy_loop_count += 1
    happy_number_sum = 0
    for n in range(int(len(str(inp)))):
        happy_number_sum = happy_number_sum + int(str(inp)[n]) ** 2
    if happy_number_sum != 1:
        is_happy = 0
        if happy_loop_count >= 100:
            is_happy = 0
        else:
            happy_check(happy_number_sum)
    elif happy_number_sum == 1:
        is_happy = 1
    if is_happy == 1:
        if is_prime == 1:
            print("\rIn addition to that, it is also a happy number.", end="")
        else:
            print("\rAlthough, it is a happy number.", end="")
    else:
        if is_prime == 0:
            print("\rIn addition to that, it also, is not a happy number.", end="")
        else:
            print("\rAlthough, it is not a happy number.", end="")
def prime_check(inp):
    global is_prime
    if inp == 1:
        print("It is neither prime, nor composite.")
    else:
        for i in range(inp - 2):
            if int(inp / (i + 2)) != float(inp / (i + 2)):
                is_prime = 1
            else:
                is_prime = 0
                i = 0
                break
        if is_prime == 1:
            print("\r" + "It is also " + mersenne_test(inputted) + ".")
        else:
            print("\r" + "It is also composite.")
odd_check(inputted)
prime_check(inputted)
happy_check(inputted)
