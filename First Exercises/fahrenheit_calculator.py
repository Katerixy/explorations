#Temperature in degrees Celsius (°C) * 9/5) + 32;

def main():
    celsius = get_number("Input a temperature in celsius: ")
    fahrenheit = round(celsius * 9/5 + 32, 2)
    celsius = round(celsius, 2)
    print(f"{celsius} degrees in celsius is {fahrenheit} degrees in fahrenheit")

def get_number(prompt):
    while True:
        number = input(prompt)
        try:
            number = float(number)
        except:
            print("please write a number in base ten")
        else:
             break
    return number

main()