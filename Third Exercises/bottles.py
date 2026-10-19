def bottles():
    bottle = " bottles"
    bottle_2 = " bottles"
    for i in range(99, 0, -1):
        if i == 1:
            bottle = " bottle"
            bottle_2 = " bottles"
        elif i == 2:
            bottle_2 = " bottle"
        strings = [str(i) + bottle + " of beer on the wall,", str(i) + bottle + " of beer", "You take one down, pass it around", str(i-1) + bottle_2 + " of beer on the wall", ""]
        n_print(strings)
    last_strings = ["No more bottles of beer on the wall,", "no more bottles of beer.", "Go to the store, and buy some more", "99 bottles of beer on the wall..."]
    n_print(last_strings)

def n_print(strings):
    for string in strings:
        print(string)

bottles()