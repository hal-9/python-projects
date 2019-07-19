import time  # import time module to delay messages

import random  # add random stuff to the code


def print_pause(message_to_print, time_to_sleep):  # to delay text
    print(message_to_print)
    time.sleep(1)


def play_game():
    items = []
    status = []
    enemy = ['Ogre', 'Devilhound', 'Baby Dragon', 'Ghoul', 'Venomous Spider']
    weapon = ['Rusty Sword', 'Old Dagger', 'Trident', 'Blade', 'Axe', 'Hammer']
    ingredient = ['Shroom', 'Cave flower', 'Magical spice', 'Potato']
    random_enemy = random.choice(enemy)
    random_weapon = random.choice(weapon)
    random_ingredient = random.choice(ingredient)
    intro()
    crossroads(items, status, ingredient, enemy, weapon, random_enemy,
               random_weapon, random_ingredient)


def intro():  # the text you see, every time you boot up the program
    print_pause("After a perilous journey through a vast continent, you "
                "arrive at a crossroad that leads many ways. ", 5)
    print_pause("Your traveling has left you with but a coin in your pocket. "
                "You look shaken and in bad shape. ", 5)
    print_pause("In front of you lies a beautiful city, that teems with "
                "life. ", 5)
    print_pause("You need to enter the city, in order to meet up with a long "
                "lost friend.", 5)
    print_pause("To the left you see a road leading to a small farm in the "
                "distance.", 5)
    print_pause("To your right you see a trail leading towards the mountain "
                "on the horizon.\n", 5)


def crossroads(items, status, ingredient, enemy, weapon, random_enemy,
               random_weapon, random_ingredient):
    # the player chooses where to go
    response = input("Where would you like to go?\n\n"
                     "1. Into the city\n"
                     "2. To the farm\n"
                     "3. To the mountain\n"
                     "\n"
                     "Enter 1, 2 or 3.\n")
    if response == "1":
        city(items, status, ingredient, enemy, weapon, random_enemy,
             random_weapon, random_ingredient)
    elif response == "2":
        farm(items, status, ingredient, enemy, weapon, random_enemy,
             random_weapon, random_ingredient)
    elif response == "3":
        cave(items, status, ingredient, enemy, weapon, random_enemy,
             random_weapon, random_ingredient)
    else:  # if input wrong, answer gets rejected and player chooses again
        print_pause("You dont't want to wander off of the streets. That would "
                    "only make things worse.", 3)


def city(items, status, ingredient, enemy, weapon, random_enemy,
         random_weapon, random_ingredient):  # city story ark
    if 'clothes' in items:  # when the player got the clothes from the farm
        print_pause("As you walk towards the city gates once again, decent "
                    "looking and full of confidence, you see some guards "
                    "approaching.", 5)
        print_pause("One guard takes a look at you and immediately notices "
                    "how well you are dressed.", 5)
        print_pause("There must be a lot of folks going in and out of the "
                    "city, as this guard doesn't seem to remember your face ",
                    5)
        print_pause("He figures you for a merchant of not to be distained "
                    "wealth and waves you in without further conversing. ", 5)
        print_pause("You have now achieved your goal by entering the "
                    "city. ", 5)
        print_pause("GAME WON", 5)
        play_again()
    else:
        if 'been_to_the_city_twice' in status:  # player in the city twice
            print_pause("As you come near the gates again, the guard loses "
                        "his patience.", 5)
            print_pause("You hear the sound of his sword leaving the sheath. ",
                        5)
            print_pause("The guard charges towards you and beheads you with a "
                        "single strike.", 5)
            print_pause("You are dead.", 5)
            play_again()
        elif "been_to_the_city" in status:  # player in the city once
            print_pause("As you try to approach the gates again, the guard "
                        "stands in your way immediately.", 5)
            print_pause("'You need me to beat the shit out of you? Get out "
                        "of here you peasant, you hear?'", 5)
            print_pause("Before he turns his words into action, you haste "
                        "back to the crossroads.", 5)
            status.append("been_to_the_city_twice")
            crossroads(items, status, ingredient, enemy, weapon, random_enemy,
                       random_weapon, random_ingredient)
        else:
            print_pause("You walk towards the city gates, which are guarded "
                        "by heavily armed knights.", 5)
            print_pause("One guard looks at you gloatingly. His derogatory "
                        "gesture shows you, they don't want estrays "
                        "like you. ", 5)
            print_pause("You walk back to the crossroad.\n", 5)
            status.append("been_to_the_city")
            crossroads(items, status, ingredient, enemy, weapon, random_enemy,
                       random_weapon, random_ingredient)


def farm(items, status, ingredient, enemy, weapon, random_enemy,
         random_weapon, random_ingredient):  # farm story arc
    if 'desired_item' in items:  # player returns with item
        print_pause("You proudly walk up to the farm.", 3)
        print_pause(f"I have come and brought you the {random_ingredient}. "
                    "It was not easy to get, but I'm here at last, you "
                    "say.", 5)
        print_pause("The farm workers applaud your bravery and the fact, that "
                    "you made sure they feast on a proper meal tonight.", 5)
        print_pause("They give you decent clothes and let you shower as "
                    "a reward.", 5)
        print_pause("It's been quite some time, since your mirror image "
                    "sparked joy in you.", 5)
        print_pause("You might be ready to get into the city. ", 3)
        print_pause("You walk back the road towards the crossroads. ", 3)
        items.append("clothes")
        crossroads(items, status, ingredient, enemy, weapon, random_enemy,
                   random_weapon, random_ingredient)
    else:
        if "been_to_the_farm" in status:  # player returns w/o item
            print_pause("The farmers all tend to their work, not giving you "
                        "any attention.", 5)
            print_pause("It seems like they all await your return from "
                        "the cave.", 5)
            print_pause("You should head there.", 5)
            print_pause("You walk back towards the crossroads.", 5)
            crossroads(items, status, ingredient, enemy, weapon, random_enemy,
                       random_weapon, random_ingredient)
        else:  # player gets to the farm for the first time
            print_pause("You arrive at the farm and ask for advice on how "
                        "to get into the city.", 5)
            print_pause("The farmers laugh at you, as one steps up to you "
                        "and says:'The way you look, you will never get into "
                        "the city.'", 5)
            print_pause("'You need a makeover and as a matter of fact, we've "
                        "got some nice clothes here.'", 5)
            print_pause("'But nothing to spice up our soup for tonight. "
                        "There is a cave some way up the road.'", 5)
            print_pause(f"'We hear there is a {random_ingredient} to "
                        f"find, but you might encounter a {random_enemy} "
                        "in there.'", 5)
            print_pause("'Here, take this. This should help you.'", 5)
            print_pause(f"You have received a {random_weapon}. Motivated "
                        "you head back to the crossroads.", 5)
            items.append("weapon_type")
            status.append("been_to_the_farm")
            crossroads(items, status, ingredient, enemy, weapon, random_enemy,
                       random_weapon, random_ingredient)


def cave(items, status, ingredient, enemy, weapon, random_enemy,
         random_weapon, random_ingredient):  # cave story ark
    print_pause("You walk towards the mountain and see a cave entrance.", 5)
    response2 = input("Would you like to enter the cave?\n"
                      "Answer with yes or no.\n").lower()
    if response2 == "yes":  # the player decides to go into the caves
        if 'weapon_type' in items:  # player heads in cave with weapon
            print_pause("You head into the caves. Following many tight "
                        "passages, you enter a bigger room.", 5)
            print_pause("At the end of the room, you see the "
                        f"{random_ingredient}. But it's guarded by a "
                        f"{random_enemy}.", 5)
            print_pause("You rush towards your foe with your weapon high "
                        "above your head.", 5)
            print_pause("One slice and it's head rolls on the ground. "
                        "You are able to get, what you came for.", 5)
            print_pause("Before you get ambushed by any more creatures, "
                        "you head out and walk back towards the "
                        "crossroads.", 5)
            items.append('desired_item')
            crossroads(items, status, ingredient, enemy, weapon, random_enemy,
                       random_weapon, random_ingredient)
        else:  # when the player heads into the caves unprepared
            print_pause("You enter the caves, feeling anxious as to what "
                        "might await you.", 5)
            print_pause("'Never enter a cave unprepared', your grandfather "
                        "always told you.", 5)
            print_pause(f"And now you know why: a {random_enemy} "
                        "rushes towards you screaming hellishly.", 5)
            print_pause("You have no means of defense and get killed "
                        "instantly.", 5)
            print_pause("GAME OVER", 5)
            play_again()
    elif response2 == "no":  # the player decides to back off
        print_pause("You wonder if this was a wise decision and walk "
                    " back to the crossroads.", 5)
        crossroads(items, status, ingredient, enemy, weapon, random_enemy,
                   random_weapon, random_ingredient)
    else:  # if input wrong, player gets reset in front of the mountain
        print_pause("You are not really sure what to do. As you wander "
                    "around on smaller trails, you eventually find your "
                    "way back to the mountain.", 5)
        cave(items, status, ingredient, enemy, weapon, random_enemy,
             random_weapon, random_ingredient)


def play_again():
    response3 = input("Would you like to start a new adventure?\n"
                      "Enter yes or no.\n")
    if response3 == "yes":
        print_pause("Great! Here we go.", 5)
        play_game()
    elif response3 == "no":
        print_pause("That's a shame. Thanks for playing.", 10)
    else:
        print_pause("Please only answer with yes or no.", 5)
        play_again()


play_game()
