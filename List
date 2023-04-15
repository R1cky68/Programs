# This program aims to have an array of games and ask the user about a particular game. They input a game and if it's in the
# array, it'll show them the array, if not it'll append the array and show them again.
games = ["Botw", "DOOM", "Smash"]

Ans = input("What's your favourite game? \n")

if Ans in games:
    print("Yes, it's in the list. Here it is: \n" + ", " .join(games))

elif Ans == "I don't like games!":
    games.clear()
    print("Never mind, there's no games now. See? \n" + ", " .join(games))

else:
    games.append(Ans)
    print("That game was not in the list. But it's added now! \n" + ", " .join(games))
