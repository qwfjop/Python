def ejection(n):
    fixed_n = []
    fixed_n.append(n)
    i = 2
    li = []
    while fixed_n[0] > i:
        if n % i == 0:
            li.append(i)
            n = n / i
            if n % i != 0:
                i = i + 1
            else:
                li.append(i)
                n = n / i
        if n % i != 0:
            i = i + 1
