gn_sum = 0


def calc_gn(n, r):
    """"" The
function takes "n" (number of terms) and "r" (common ratio) as parameters"""
    global gn_sum

    if n < 0:
        return

    gn_sum += r ** n
    calc_gn(n - 1, r)


n = 5
r = 2
calc_gn(n, r)
print(gn_sum)
