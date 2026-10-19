def main():
    number1 = get_number("Input first number: ")
    number2 = get_number("Input second number: ")
    operand = get_operand("Input operand: ")
    if operand == "+":
        answer = number1 + number2
    elif operand == "-":
        answer = number1 - number2
    elif operand == "*":
        answer = number1 * number2
    elif operand == "/":
        if number2 == 0:
            answer = "Cannot divide by 0"
        else:
            answer = number1 / number2
    print(answer)

def get_number(prompt):
    while True:
        number = input(prompt)
        try:
            number = int(number)
        except:
            try:
                number = float(number)
            except:
                print("please write a number in base ten")
            else:
                break
        else:
            break
    return number

def get_operand(prompt):
    while True:
        operand = input(prompt)
        if operand in ["+", "*", "-", "/"]:
            break
        else:
            print("input +, *, -, or /")
    return operand

main()