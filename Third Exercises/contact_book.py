def main():
    key = input("Input name:")
    print(search(key))

def search(key):
    lk = key.lower()
    phone_book = {"john": 123456789, "carl": 320486497}
    if lk in phone_book:
        answer = f"{key}'s phone number is: {phone_book[lk]}"
    else:
        answer = f"{key} does not exist in phone book"
    return answer

main()