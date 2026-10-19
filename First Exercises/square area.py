def main():
    print("This multiples two numbers together")
    prompt1 = "Input the first number: "
    number = float(get_number(prompt1))
    prompt2 = "Input the second number: "
    number2 = float(get_number(prompt2))
    print(number * number2)
def get_number(prompt):
    while True:
        number = input(prompt)
        try:
            int(number)
        except:
            try:
                float(number)
            except:
                print("please write a number in base ten")
            else:
                break
        else:
            break
    return number


main()