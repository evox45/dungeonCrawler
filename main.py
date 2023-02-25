from lib import menu, fightable, hero
from lib.mobs import mob
from lib.mobs.goblin import Goblin
from lib.mobs.tree import TreeBoss

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
    print("\n\n")
    print("We are now playing the game")
    player = hero.Hero()

    level = 0

    # Big game loop
    while player.isAlive():


        print("Level {}".format(level))
        print("Players health is currently{}HP".format(player.curHealth))
        
        if level % 3 == 0 and level != 0:
            enemy = TreeBoss()
        else:
            enemy = Goblin()

        # Our fighting loop
        while player.isAlive() and enemy.isAlive():
            print("Player attacks with a {}".format(player.primaryWeapon.name))
            enemy.takeDmg(player.attack())

            player.takeDmg(enemy.attack())

        print("Killed a {}".format(enemy.name))
        

        # Allow for looting
        if player.isAlive() and not enemy.isAlive():
            print("\nLoot some items")
            # Generate a new menu object
            lootMenu = menu.Menu()

            # TODO Fix bug with empty inventory for enemy spawning the menu
            # Add all items from enemy inventory to the menu
            for idx, item in enumerate(enemy.inventory.contains):
                # Adding item, function to execute on selection, and which item should be taken out
                lootMenu.addMenuItem(item.name, enemy.inventory.takeOut, idx)

            # Display 
            lootMenu.displayMenu()

            # Get user input
            userInput = input("Select> ")

            # Add the loot to the user's inventory
            player.inventory.add(lootMenu.runItem(userInput))

        print("Player's Inventory")
        for item in player.inventory.contains:
            print(item.name)

        print("\n")

        level += 1


if __name__ == "__main__":
    main()