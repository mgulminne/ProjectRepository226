n = int(input("3 ile 9 arasında bir sayı girin : "))

if 3 <= n <= 9:

    for i in range(1, 2 * n):

        if i <= n:
            k = i
        else:
            k = 2 * n - i


        for j in range(1, k + 1):
            print(j, end=" ")
        print()
else:
    print("invalid input.")
