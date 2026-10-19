friends = ['David','Alexander','Edmond','Evan', 'Luka',
           'Triston','Kourosh','Catherine','Kateryna', 'Sai']
favorite_movies = [
    ['Interstellar','Minions'],
    ['Cars','Batman'],
    ['Tenet','The Pianist'],
    ['Titanic'],
    ['Batman','Titanic'],
    ['The Edge of Tomorrow','Black Hawk Down'],
    ['John Wick','Minions'],
    ['Inception','Seven Samurai'],
    ['Flow','Die Hard'],
    ['Wolf of Wallstreet', 'Ready Player One']
]
healthy_food = ["apple", "salmon", "avocado", "seafood", "olive oil", "spinach", "yogurt"]
vegan_food = ["cookies", "apple", "avocado", "candy", "olive oil", "fake chicken", "spinach"]
numbers = [1, 2, 3, 4, 5]

def check_all(f, n, h_f, v_f):
    lf = lower_case(f)
    print(lf)
    af = a_filter(f)
    print(af)
    greet_a(f)
    print_l()
    print(sum_n(n))
    print("total is:", user_n())
    print(like_f(h_f, v_f))
def check_new(f, n, h_f, v_f):
    print(like_f(h_f, v_f))

def lower_case(friends):
    lower_friends = []
    for i in range(len(friends)):
        lower_friends.append(friends[i].lower())
    return friends

# Filter names keeping ones starting with 'A'
def a_filter(friends):
    new_friends = []
    for friend in friends:
        if friend[0] == "A":
            new_friends.append(friend)
    return new_friends

def greet_a(friends):
    for friend in friends:
        if friend[0] == "A":
            greet = "Hello, "
        else:
            greet = "Bye, "
        print(greet + friend + "!")

def print_l():
    for i in range(10):
        if i < 9:
            continue
        print("last for loop, number:" , i)

def sum_n(n_list):
    total = 0
    for n in n_list:
        total += n
    return total

def user_n():
    total = 0
    num = ""
    while num != 0:
        num = input("Enter a number: ")
        try:
            num = int(num)
        except:
            print("not a number.")
        else:
            total += num
    return total

def like_f(healthy, vegan):
    f_list = []
    for i in healthy:
        for j in vegan:
            if i == j:
                f_list.append(i)
    return f_list

check_all(friends, numbers, healthy_food, vegan_food)