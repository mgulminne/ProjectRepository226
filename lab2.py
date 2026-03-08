#digitalrootsequance
num = int(input("enter a number greater than 9 "))

if num <= 9:
    print("enter a number greater than 9")
else:
    steps = 0
    print(num, end="")

    while num > 9:
        digit_sum = 0
        temp = num


        while temp > 0:
            digit_sum += temp % 10
            temp //= 10

        num = digit_sum
        steps += 1

        print(" →", num, end="")

    print(" final value: ", num)
    print("steps counter: ", steps)

