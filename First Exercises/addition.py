def main():
    print("This adds two numbers together")
    prompt = "Input the first number: "
    while True:
        number = input(prompt)
        try:
            number = int(number)
        except:
            print("please write a number in base ten")
        else:
            break
    prompt = "Input the second number: "
    while True:
        number2 = input(prompt)
        try:
            number2 = int(number2)
        except:
            print("please write a number in base ten")
        else:
            break
    print()
    print(number + number2)

main()

