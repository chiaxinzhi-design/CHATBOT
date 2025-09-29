def calculate(numb1, operator, numb2):
    
    if operator == "+":
        return numb1 + numb2

    if operator == "-":
        return numb1 - numb2

    if operator == "*":
        return numb1 * numb2

    if operator == "/":
        return numb1 / numb2

print(calculate(10, "+", 10))  # should return 20
print(calculate(10, "-", 10))  # should return 0
print(calculate(10, "*", 10))  # should return 100
print(calculate(10, "/", 10))  # should return 1.0
