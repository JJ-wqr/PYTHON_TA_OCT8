# This shows the zones where if it is "True" then you can access it. The locked zones with "False" can be unlocked if and only if the robot or user acquires an unlock item from the accessible zones.
zones = {
    "Zone A": {"item": "power cell", "locked": False},
    "Zone B": {"item": "hazard", "locked": True, "unlock_item": "power cell"},
    "Zone C": {"item": "battery pack", "locked": False},
    "Zone D": {"item": "power cell", "locked": True, "unlock_item": "battery pack"},
    "Zone E": {"item": "hazard", "locked": False},
    "Zone F": {"item": "power cell", "locked": False},
    "Zone G": {"item": "hazard", "locked": True, "unlock_item": "power cell"},
    "Zone H": {"item": "battery pack", "locked": False},
    "Zone I": {"item": "power cell", "locked": True, "unlock_item": "battery pack"},
    "Zone J": {"item": "hazard", "locked": False},
    "Zone K": {"item": "battery pack", "locked": True, "unlock_item": "power cell"},
    "Zone L": {"item": "power cell", "locked": False},
    "Zone M": {"item": "hazard", "locked": False},
    "Zone N": {"item": "power cell", "locked": False},
    "Zone O": {"item": "battery pack", "locked": False},
    "Zone P": {"item": "hazard", "locked": False},
    "Zone Q": {"item": "power cell", "locked": True, "unlock_item": "battery pack"},
}

# The initial value of battery when starting, inventory, and also the zones explored which will be filled once the game starts. 
battery_level = 100
inventory = []
explored_zones = set()

# This function will be displaying the messages after every zone exploration. It will be looped.
def display_status():
    # Displays the current battery level, inventory, and explored zones when progresing
    print(f"🔋 Battery Level: {battery_level}%")
    print(f"📦 Inventory: {inventory}\n")

# This function will function to display explorable zones and locked zones where it will require an "unlock_item" in order to access the zone.
def show_available_zones():
    #Displays the available zones for exploration.
    available_zones = []
    for zone, details in zones.items():
        if zone not in explored_zones:
            if details["locked"] and details["unlock_item"] not in inventory:
                print(f"{zone} is locked. You need a {details['unlock_item']} to enter yes yes. yes? yes 🔒")
            else:
                available_zones.append(zone)
    return available_zones

# This function will function o update the state of the game when the player visits or explores a zone. It will also provide message or notice if user or the robot finds something.
def move_to_zone(choice):
    # Explore the zone and it will update any change in the game
    global battery_level

    # Decrease battery when moving to a new zone
    battery_level -= 10  
    # Game over when battery level is 0 or below.
    if battery_level <= 0:
        print("⚡ Battery ran out while moving! Game over.")
        return False  

    # Simialr to the function of the previous function above, it will update the game where it will specifically update the user or robot's inventory. In addition, it will also be the function where it functions to increase or decrease the robot's battery life or capacity. 
    explore_zone(choice)
    # Return True means the game will keep going and the loop will not break.  
    return True  

#Collects battery
def collect_item(item):
    """Adds an item to the robot's inventory if it's a power cell."""
    if item == "power cell":
        inventory.append(item)
        print("✅ Power cell added to inventory!")

def display_inventory():
    # Tjos function will thisplay the dispkay of tehe ivnventory.s
    print("📦 Current Inventory:")
    for item in inventory:
        print(f"  - {item}")
        # Optional print satatemnt for tje to meet the programming propserites of programmming
    print()  

def explore_zone(choice):
    # This function will function o update the state of the game when the player visits or explores a zone. It will also provide message or notice if user or the robot finds something.
    global battery_level
    global inventory

    # It will feedback the of the zone info and what you get in there.
    zone_info = zones[choice]
    print(f"🔍 You found a {zone_info['item']} in {choice}!")

    # Update inventory and mark zone as explored
    explored_zones.add(choice)  # It will mark the zone that is epxlored
    if zone_info["item"] == "power cell":
        collect_item("power cell")  # It will initiate the collect item function
    elif zone_info["item"] == "hazard":
        battery_level -= 20  # Drain battery if a hazard is encountered
        print("⚠️ Hazard encountered! Battery drained by 20%.")
    elif zone_info["item"] == "battery pack":
        battery_level += 20  # Recharge battery if a battery pack is found
        print("🔋 Battery pack found! Battery recharged by 20%.")


# This will function as the rule of the game. Which is that running out of battery is game over and collecting all batteries means winning the game. When a condition is met, it will return True where it will end the loop similar to the break function and vice versa.
def check_game_over():
    # Decides if it is win or game over based on the battery level and also the batteries or power cells whatever
    if battery_level <= 0:
        print("⚡ Battery ran out! Game over bruh.")
        return True
    elif len(inventory) >= 8:  # In here it is 8 batteries well the game features 8 batteries. 
        print("🎉 Congratulations! You've collected all power cells and won the game!  FINALLY I CAN SLEEP!")
        return True
    return False

# This will be displayed when executing the code or starting the game.
print("🌟 Welcome to the Excruciating Robot Exploring zone based on the zone you choose game.")
print("Your mission is to collect power cells to unlock new zones as the power cells function as a key to unlock the locked zones.")

# Use of while function to make the loop feature of the game. If the battery is above 0, then the game will continue and will also display the many feedback for the user to see based from the functions made for the game.
while battery_level > 0:
    display_status()
    
    # Show available zones that is currently explorable or accessible. 
    available_zones = show_available_zones()

    # This if condition will stop the loop or break the loop when all zones are explored or locked.
    if not available_zones:
        print("🚫 All zones explored or locked. Game over!")
        break

    # This will display the zones that the user can explore currently and will also remove the available zone to be explored if it is explored already.
    print("🌍 Choose a zone to explore:", ", ".join(available_zones))
    choice = input("Enter a zone name or 'quit' to exit: ").strip()

    # This functions if player wants to manually end the game and will display appropriate message.
    if choice.lower() == 'quit':
        print("👋 Thanks for playing!")
        break

    # Functions to check if the zone is valid or in the dictionary. If the zone is explored, the user will supposedly be unable to enter the same zone thus a message will be shown to the user to choose another zone that is still unexplored yet.
    if choice not in zones:
        print("❌ Invalid zone. Please choose again and choose another zone.")
        continue
    if choice in explored_zones:
        print("⚠️ You've already explored this zone. Please pick a different zone thanks. Is robot supposed to be talking like this im so sleepy.")
        continue

    # To see if a particular zone is locked and will require the "unlock_item" to make the once inaccessible zone to be accessible.
    if zones[choice]["locked"] and zones[choice]["unlock_item"] not in inventory:
        print(f"{choice} is locked. You need a {zones[choice]['unlock_item']} to enter yes yes? yes locked sad🔒")
        continue  # Skip to the next loop step without exploring the zone.

    # Robot will explore zone based on chosen zone input
    if move_to_zone(choice):
    # This will see the game over conditions for it to know if it should break the loop or not.
        if check_game_over():
            break
# This will output thanks for playing
print("🛑 Thank you for testing or playing the Robot Exploring game thing.")

