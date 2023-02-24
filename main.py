from lib import menu, fightable, hero
from lib.mobs import mob
from lib.mobs.goblin import Goblin

def main():
    print("Welcome to my Dugeon game")

    mainMenu = menu.Menu()

    mainMenu.addMenuItem("Start Game", gameLoop)
    mainMenu.addMenuItem("Scores", print, "print this stuff also")
    mainMenu.addMenuItem("Quit", exit)

    mainMenu.displayMenu()

    menuIdx = input("Select> ")

    mainMenu.runItem(menuIdx)


def gameLoop():
    print("We are nwo playing the game")
    player = hero.Hero()

    # Big game loop
    while player.isAlive():

        goblin = Goblin()

        # Our fighting loop
        while player.isAlive() and goblin.isAlive():
            print("Player attacks with a {}".format(player.primaryWeapon.name))
            goblin.takeDmg(player.attack())

            player.takeDmg(goblin.attack())

        print("Killed a goblin")
        print(player.curHealth)

        # Allow for looting
        if player.isAlive() and not goblin.isAlive():
            # Generate a new menu object
            lootMenu = menu.Menu()

            # TODO Fix bug with empty inventory for enemy spawning the menu
            # Add all items from enemy inventory to the menu
            for idx, item in enumerate(goblin.inventory.contains):
                # Adding item, function to execute on selection, and which item should be taken out
                lootMenu.addMenuItem(item.name, goblin.inventory.takeOut, idx)

            # Display 
            lootMenu.displayMenu()

            # Get user input
            userInput = input("Select> ")

            # Add the loot to the user's inventory
            player.inventory.add(lootMenu.runItem(userInput))

        print("Player's Inventory")
        for item in player.inventory.contains:
            print(item.name)


if __name__ == "__main__":
    main()