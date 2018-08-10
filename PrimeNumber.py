n = 3
print(2)
def factor(n):
    factor = []
    smaller_than_n = []
    i = 1
    while n - 1 > i:
        i = i + 1
        smaller_than_n.append(i)
    for division in smaller_than_n:
        if n % division == 0:
            factor.append(division)
    return(factor)
while True:
    if len(factor(n)) == 0:
        #time.sleep(0.15)
        print(n)
    n = n + 2
