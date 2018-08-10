import random
alpha = random.randint(1, 10)
beta = random.randint(1, 10)
alpha_plus_beta = alpha + beta
alpha_multiply_beta = alpha * beta
equation = "x^2-"+str(alpha_plus_beta)+"+"+str(alpha_multiply_beta)
input_alpha = int(input("What is alpha?\n"))
input_beta = int(input("what is beta?\n"))
print(equation)
if input_alpha == alpha and input_beta == beta:
    print("Correct!")
else:
    print("Wrong!")
