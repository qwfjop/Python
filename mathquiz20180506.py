(o_score) = 0
(x_score) = 0
import random
while True:
    x1 = random.randint(10, 20)
    strx1 = str(x1)
    x2 = random.randint(10, 30)
    strx2 = str(x2)
    x = x1 * x2
    answer = input(strx1+" * "+strx2+"\n")
    if type(input) == str:
        print("Enter a number")
    if int(answer) == x:
        o_score = o_score + 1
        print("WOW!")
    else:
        x_score = x_score + 1
        print("No!")
    print("O :" + str(o_score) + " | X :" + str(x_score))
    print("---------------------------")
