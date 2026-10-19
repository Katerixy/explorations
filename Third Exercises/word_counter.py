from collections import Counter
def main():
    text = input("Input text for frequencey counter:")
    frequency(text)
def frequency(gram_text):
    item_list = "`!@#$%^&*()_+-={}[]|:;"'<,>.?/'
    text = gram_text
    for item in item_list:
        text=text.replace(item, "")
    text=text.split(" ")
    c = Counter()
    for word in text:
        c[word] += 1
    print(c)
main()