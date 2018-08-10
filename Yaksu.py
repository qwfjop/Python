n = int(input("Enter"))
def yaksu(n):
    yaksu = []
    smaller_than_n = []
    i = 1
    while n - 1 > i:
        i = i + 1
        smaller_than_n.append(i)
    for division in smaller_than_n:
        if n % division == 0:
            yaksu.append(division)
    return(yaksu)
print(yaksu(n))
