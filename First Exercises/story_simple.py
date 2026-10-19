#there once was a knight named [name] who defeated [number] dragons in their life. knight [name] got [50*number] gold, and bought [hat/sunglasses]

def main():
    print("write one word for each prompt to get a story!")
    name = input("Your name: ")

    number = input("A number: ")
    while True:
        try:
            number = int(number)
        except:
            print("Input a number in base ten")
        else:
            break
        number = input("A number: ")
    item = input("Do you like hats or sunglasses more? ")
    while True:
        if item == "hats":
            item = "a hat"
            break
        elif item == "sunglasses":
            item = "sunglasses"
            break
        print("Input 'hats' or 'sunglases'")
        item = input("Do you like hats or sunglasses more? ")
    if number == 1:
        dragons = "dragon"
    else:
        dragons = "dragons"
    print(f"There once was a knight named {name} who defeated {number} {dragons} in their life. Knight {name} got {50*number} gold, and bought {item}")


main()
