def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)



def exp_x(x, n):


    abs_val = lambda num:num if num >= 0 else -num

    sum = 0
    for i in range(n):

        numa = x ** (2 * i)
        denuma = factorial(2 * i)

        y = abs_val(numa / denuma)


        if i % 2 == 0:
            sum += y
        else:
            sum -= y

    return sum



x_val= float(input("X: "))
n_val = int(input(" (n)  "))

final_val= exp_x(x_val, n_val)
print(":", final_val)


