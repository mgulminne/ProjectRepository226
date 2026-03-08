n = int(input("please enter a number between 10 and 100: "))
while n < 10 or n > 100:
    print("invalid input")
    n = int(input("please enter a number between 10 and 100: "))

fizz = 0
buzz = 0
fizzbuzz = 0

for i in range(1,n+1):
    if i % 7 ==0:
        print(i,"is skipped")
        continue

    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        fizzbuzz += 1

    elif i % 3 == 0:
        print("fizz")
        fizz += 1

    elif i % 5 == 0:
        print("buzz")
        buzz += 1

    else:
        print(i)


print("----SUMMARY----")
print("FİZZ COUNT",fizz)
print("BUZZ COUNT ",buzz)
print("FIZZBUZZ COUNT ",fizzbuzz)
