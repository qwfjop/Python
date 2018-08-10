import time
def fractional_decomposition(n):
    fixed_n = []
    fixed_n.append(n)
    i = 3
    li = []
    #if n % 2 == 0:
    #    li.append(2)
    while fixed_n[0] / 2 + 1 > i:
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
    return(li)
n = 2
max = int(input("How big the range is?\n"))
start_time = time.time()
sosu = [2]
while max > n:
    if len(fractional_decomposition(n))==0:
        sosu.append(n)
        n = n + 1
    else:
        n = n + 1
print("There are \n"+str(sosu))
print("There are "+str(len(sosu))+" prime numbers")
print("--- %s seconds ---" % (time.time() - start_time))
