import random

# Define the rooms
rooms = {
    "clearing": {
        "description": "You are in a clearing in the forest. There are trees to the north, south, east, and west. There are paths to the north, south, east, and west.",
        "exits": ["north", "south", "east", "west"],
    },
    "path north": {
        "description": "You are on a path through the forest. There is a tree to the north and a bush to the south. There are enemies to the north and east.",
        "exits": ["north", "south", "east"],
    },
    "path south": {
        "description": "You are on a path through the forest. There is a stream to the north and a rock to the south. There are enemies to the south and west.",
        "exits": ["north", "south", "west"],
    },
    "path east": {
        "description": "You are on a path through the forest. There is a hill to the north and a cave to the south. There are enemies to the north and east.",
        "exits": ["north", "south", "west"],
    },
    "path west": {
        "description": "You are on a path through the forest. There is a river to the north and a meadow to the south. There are enemies to the north and west.",
        "exits": ["north", "south", "east"],
    },
    "tree": {
        "description": "You are standing in front of a large tree. There is a hole in the trunk.",
        "exits": ["south"],
    },
    "bush": {
        "description": "You are standing in front of a large bush. There is a bird's nest in the branches.",
        "exits": ["north"],
    },
    "stream": {
        "description": "You are standing on the bank of a stream. There is a bridge to the north and a path to the south.",
        "exits": ["north", "south", "east"],
    },
    "rock": {
        "description": "You are standing on a large rock. There is a cave to the north.",
        "exits": ["north", "south"],
    },
    "hill": {
        "description": "You are standing on the top of a hill. There is a view of the forest in all directions.",
        "exits": ["south"],
    },
    "cave": {
        "description": "You are in a cave. There is a tunnel to the north and a dead end to the south.",
        "exits": ["north", "south"],
    },
    "tunnel": {
        "description": "You are in a tunnel. It is dark and damp.",
        "exits": ["south"],
    },
}

# Define the enemies
enemies = {
    "wolf": {
        "attack": 10,
        "health": 20,
    },
    "goblin": {
        "attack": 5,
        "health": 10,
    },
}

# Define the player's current room
current_room = "clearing"

# Define the player's stats
player_health = 100

# Start the game loop

    # Print the current room's description
def print_room():
    print(rooms[current_room]["description"])
while True:
    b = 0
    if b == 0:
        print_room()
        b = b + 1
    # Check if there are any enemies in the current room
    if "enemies" in rooms[current_room]:
            enemy = random.choice(rooms[current_room]["enemies"])

            print("An {} attacks you!".format(enemy))

        # Fight the enemy
            while player_health > 0 and enemy["health"] > 0:
                player_choice = input("Attack or defend? ")

            if player_choice == "attack":
                enemy["health"] -= player_health
                print("You attack the {} and deal {} damage.".format(enemy, player_health))
            elif player_choice == "defend":
                player_health -= enemy["attack"]
                print("The {} attacks you and deals {} damage.".format(enemy, enemy["attack"]))
            else:
                print("I don't understand your command.")

            if player_health <= 0:
                print("You have died.")
            elif enemy["health"] <= 0:
                print("You have defeated the {}!")
            b = 0
