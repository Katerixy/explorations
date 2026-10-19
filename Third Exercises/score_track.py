scores = {"John":3, "Carl":100, "Lily":98}

def main(scores):
    get_all(scores)
    print("Class average is", round(avg(scores), 2))


def get_all(scores):
    for key,value in scores.items():
        print(key, "got", value)

def avg(scores):
    total = 0
    for value in scores.values():
        total += value
    avg = total / len(scores)
    return avg

main(scores)
