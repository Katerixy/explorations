#once upon a time there was a knight named (any).

#knight [name] saw a new quest on a board. It said:
# "A dragon on top of the mountain stole my chickens! I will give 100 gold to the brave warrior who saves them."
#does the knight do the quest? (yes/no)

#yes: the knight goes up to the mountain, and sees the dragon. it is sleeping. next to it are three very scared chickens
#fight the dragon while it is asleep, or try to sneak past it to the chickens? (fight/sneak)

#fight: knight [name] slays the dragon, gathers the chickens, and heads home.
#with the 100 gold, what does [name] buy? (ice cream/sun glasses)

#ice cream: the knight enjoys the ice cream, then goes to sleep at their castle
#the end

#sun glasses: knight [name] gets cool sun glasses, and gets some compliments!
#the end

#sneak: the knight sneaks past the dragon. As they get to the chickens, the dragon wakes up!
#with some quick thinking, the knight slips past and runs away back to town.
#with the well-earned 100 gold, what does [name] buy? (ice cream/ sunglasses)

#no:
#knight [name] decides today is not the day for adventuring, and heads back home to their castle.
#the end

def main():
    #story is a dictionary
    #dict keys are: name, start, and then names that correspond to choices
    #within a keys value is a tuple
    #both tuple sections have a list
    #list of tuple[0] has text
    #text can be divide so each part is printed on a new line
    #list of tuple[1] has choices
    #user must choose a choice from the choices list, else the story doesn't move on
    #choices in choice box MUST correspond to a dict key. Otherwise, the story wont go anywhere
    #choices list CAN be empty. This ends the story instead of finding a key to continue the story

    #can be improved by creating one more value to each choice: (eg. instead of tuple[1] = [choice1, choice2],
    # tuple[1] = [(choice1, corresponding dict key), (choice 2, corresponding dict key2)]

    story = {"name": (["Once upon a time there was a knight named: "
                        ], []),
             "start": (["Knight [name] saw a new quest on a board. It said:",
                        "'A dragon on top of the mountain stole my chickens! I will give 100 gold to the brave warrior who saves them.'",
                        "Does the knight do the quest? (yes/no)"
                        ], ["yes", "no"]),
             "yes": (["the knight goes up to the mountain, and sees a sleeping dragon. next to it are three very scared chickens",
                      "fight the dragon while it is asleep, or try to sneak past it to the chickens? (fight/sneak)"
                      ], ["fight", "sneak"]),
             "no": (["knight [name] decides today is not the day for adventuring, and heads back home to their castle.",
                     "The End"
                     ], []),
             "fight": (["knight [name] slays the dragon, gathers the chickens, and heads home.",
                        "with the 100 gold, what does [name] buy? (ice cream/sunglasses)"
                        ], ["ice cream", "sunglasses"]),
             "sneak": (["the knight sneaks past the dragon. As they get to the chickens, the dragon wakes up!",
                        "with some quick thinking, the knight takes the chickens, slips past, and runs away back to town."
                        "with the well-earned 100 gold, what does [name] buy? (ice cream/sunglasses)"
                        ], ["ice cream", "sunglasses"]),
             "ice cream": (["the knight enjoys the ice cream, then goes to sleep at their castle",
                            "The End"
                            ], []),
             "sunglasses": (["knight [name] gets cool sun glasses, and some compliments!",
                             "The End"
                             ], []),

             }
    write_story(story)
#starts the story with introduction, then runs a recursive function
#story must have a name key and a start key from where the story can start
def write_story(story):
    text = 0
    choices = 1
    name_story = story["name"][text]
    for part in range(len(name_story)):
        print(name_story[part])
    name = input()
    story_web(story["start"], story, name)


def story_web(story_part, story, name):
    text = 0
    choices = 1

    for section in range(len(story_part[text])):
        part_section = story_part[text][section]
        if "[name]" in part_section:
            part_section = part_section.replace("[name]", name)
        print(part_section)
    if story_part[choices] == []:
        return

    while True:
        choice = input()
        if choice in story_part[choices]:
            story_web(story[choice], story, name)
            break
        else:
            print("Not a valid answer! Try something else")
    return
if __name__ == "__main__":
    main()