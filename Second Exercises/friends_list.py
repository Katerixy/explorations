def main():
    friends = ["John", "Ramona", "Lily", "Frisk", "Bob"]
    friends.append("Dominique")
    friends.pop(3)
    friends.pop(1)
    friends.remove("John")
    friends.insert(2, "Moth")
    f_likes = [["movies", "calculus", "Bob"], ["the color blue", "books", "glasses"], ["iphones", "target", "crisp notes"], ["chairs", "burgers", "sitting"]]
    for i in range(len(friends)):
        friends[i] = [friends[i]]
        friends[i].extend(f_likes[i])
    for friend in friends:
        print(f"{friend[0]} likes {friend[1]}, {friend[2]}, and {friend[3]}")
main()