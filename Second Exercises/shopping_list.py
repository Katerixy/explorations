def main():
    list = create_list()
    print("your list is:", list)

def create_list():
    list = []
    while True:
        item = input("Add item: ")
        list.append(item)
        answer = input("Do you want to continue adding? (yes/no)\n")
        if answer == "yes":
            pass
        elif answer == "no":
            break
        else:
            print("Let's just continue...")
    return list

main()