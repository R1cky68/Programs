# This program takes in what placement you've done and gives them a rating and information
Placement = input("What placement are you interested in? Or would you like to know the options? \n")

def newPlacement():
    details = dict()
    details["Name: "] = input("Select the name of the placement ")
    details["Speciality: "] = input("What speciality is this? ")
    details["Supervisor: "] = input("Who's the supervisor here? ")
    details["Environment: "] = input("How's the environment? ")
    details["Difficulty:" ] = input("Rate the difficulty now ")
    return details

if (Placement == "Options"):
    print("Options are Maryborough, Greenslopes, Mater")
    Placement = input("What placement are you interested in? Or would you like to know the options?")
    
elif (Placement == "Maryborough"):
    print("Maryborugh: \n What would you like to know? \n")
    Selection = input("Speciality \nSupervisor \nEnvironment \nDifficulty \n")
    if (Selection == "Speciality"):
        print("Neurology")
    elif (Selection == "Supervisor"):
        print("Bronwyn Castelli")
    elif (Selection == "Environment"):
        print("Pretty chill since rural")
    elif (Selection =="Difficulty"):
        print("Impossible, especially for a first")
    
elif (Placement == "Greenslopes"):
    print("Maryborugh: \n What would you like to know? \n")
    Selection = input("Speciality \nSupervisor \nEnvironment \nDifficulty \n")
    if (Selection == "Speciality"):
        print("Cardiorespiratory")
    elif (Selection == "Supervisor"):
        print("Courtney Trenerry, Jeremy Solley")
    elif (Selection == "Environment"):
        print("Chill as")
    elif (Selection =="Difficulty"):
        print("Engaging and doable, top tier")

elif (Placement == "Mater"):
    print("Mater: \n What would you like to know? \n")
    Selection = input("Speciality \nSupervisor \nEnvironment \nDifficulty \n")
    if (Selection == "Speciality"):
        print("Orthopaedics")
    elif (Selection == "Supervisor"):
        print("Michael Murphy")
    elif (Selection == "Environment"):
        print("Relatively hectic")
    elif (Selection =="Difficulty"):
        print("Challenging but not stupid hard")

else:
    print("You want to create your own? Alright can do that \n")
    details = newPlacement()
    print("This is the placement:", details)
