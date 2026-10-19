import time

x = 10
def write(words):
    collection = []
    for char in words:
        start = time.time()
        time.sleep(0.05)
        print(char, end = "", flush=True)
        end = time.time()
        collection.append(end-start)
    print()
    print(collection)

if x > 5:
    write("x is greater than 5")
else:
    write("x is not greater than 5")
write("hello world")

