import random


def firing(cylinder, loaded, player):
    # work out the chance of dying
    chances = len(cylinder)

    # describe the action. first pull has a different message
    if chances == 6:
        print("{} takes the gun. There are {} chambers to go, so {}'s odds are 1 in {}!".format(player, chances, player,
                                                                                                chances))
    elif chances == 1:
        print(
            "{} picks up the gun, knowing that this is the end of the line. {} looks at the crowd, then his opponent and friend.".format(
                player, player))
    else:
        print("{} takes the gun again. There are {} chambers to go, so {}'s odds are 1 in {}!".format(player, chances,
                                                                                                      player, chances))

    # now pop the current chamber from the front of the cylinder list, to check if it matches the loaded value:
    chamber = cylinder.pop(0)
    print("{} pulls the trigger...".format(player))

    if chamber == loaded:
        print("BANG!")
        # tell the movie ending, or the alternate ending:
        if player == "Nick":
            print(
                "{} slumps over the table, a sad victim of undiagnosed PTSD. Michael is left to go back to the U.S. with {}'s body, as he promised.".format(
                    player, player))
        else:
            print(
                "{}'s head is rocked back in his chair. I guess Nick would stay in Vietnam and play till his luck also ran out?".format(
                    player))
    else:
        # if it's empty, it'll click and they'll play again.
        print("Click.")
        return cylinder

#---------------*** main program ***---------------------#

# Initialize the gun and the players:

# players are characters from The Deer Hunter:
players = ["Nick", "Michael"]
random.shuffle(players)
# cylinder is list representing a standard six shot revolver, shuffled for random order
cylinder = list(range(1, 7))
random.shuffle(cylinder)
# the bullet is loaded into the revolver:
loaded = random.randint(1, 6)

turn = 6

# the game will play as long as there are cylinders in the gun - if the gun fires in the firing function, nothing is returned and cylinder will evaluate as empty/ false
while cylinder:
    turn -= 1
    if turn % 2 == 0:
        player = players[0]
    else:
        player = players[1]

    cylinder = firing(cylinder, loaded, player)
