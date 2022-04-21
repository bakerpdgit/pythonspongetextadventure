def locationA(): # ruined castle
    print("You are in a ruined castle, just inside the gatehouse.")
    print("There is a building to the North and a walled area to the East.")
    
    print("Which way do you want to go?")
    choice = input()
    
    if choice == "N":
        locationB() # This line moves you to location B from location A
    elif choice == "E":
        locationC() # This line moves you to location C from location A
    else:
        print("You cannot go that way...")

def locationB(): # the great hall
    print("You are in the great hall.")
    
def locationC(): # the keep
    print("You are in the keep.")       
    
# Start the game
print("Welcome to my adventure game...")
locationA()