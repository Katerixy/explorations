def main():
    num = input("enter a number: ")
    even_check(num)

def even_check(num):
    even = False
    try:
        num = int(num)
    except:
        string = "This isn't a number!"
    else:
        if num % 2 == 0:
            string = "This is even"
            even = True
        else:
            string = "This is odd"
    print(string)
    return even

main()