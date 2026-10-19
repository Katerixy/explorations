fruit_list = ["apple", "banana", "mango", "kiwi", "lemon", "orange", "tomato"]

def main(fl):
    f = input("What is your favorite food?")
    f = f.lower()
    if f in fl:
        print("Great choice!")
    else:
        print("That fruit isn't in my list...")

main(fruit_list)