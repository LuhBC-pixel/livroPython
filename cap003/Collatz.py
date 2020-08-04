def collatz(number):
    if number % 2 == 0:
        return (number // 2)
    else:
        return (3 * number + 1)


print("Enter number:")
while True:
    try:
        numero = int(input())
    except ValueError:
        print("Please enter a valid INTEGER")
    formula = collatz(numero)
    if formula == 1:
        break