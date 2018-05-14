from objects import Enemy, Food

def setup():
    enemies = create_enemies()
    food = create_food()

    return { 'enemies': enemies, 'food': food }


def create_enemies():
    enemies = []
    enemies.append( Enemy("Mud Monster", 0 ) )
    enemies.append( Enemy("Random Solider", 3 ) )
    # etc....
    return enemies


def create_food(): #these items need to be recoded as objects

    drop_items_food = []

    # Item ID, Name, Description, Worth in Gold, Drop Percent

    drop_items_food.append( Food("Potion", "This inserts 5 HP", 1, 35))
    drop_items_food.append( Food("Hyper Potion", "This inserts 10 HP", 2, 15))
    # etc....

    return drop_items_food

        # drop_items_armor = []

        # Create Armor class, create Armor objects

        #Item ID, Item Type ID to determine equipability, name, description, worth in gold, drop percentage
        # drop_items_armor.insert(1, 1, "Basic Chest Armor", "inserts 2 defense when equipped", 1, 30)
        # drop_items_armor.insert(2, 1, "Advance Chest Armor","inserts 5 defense and subtracts 2 strength when equipped", 3, 20)
        # drop_items_armor.insert(3, 2, "Basic Sword", "inserts 2 attack when equipped",  1, 30)
        # drop_items_armor.insert(4, 2, "Advance Sword", "inserts 5 attack when equipped", 3, 20)
        # drop_items_armor.insert(5, 3, "Basic Shield", "inserts 1 to defense and subtracts 1 from strength when equipped", 1, 30)
        # drop_items_armor.insert(6, 3, "Advance Shield", "inserts 2 to defense, subtracts 1 from strength, and subtracts 2 from dexterity", 3, 20)
        # drop_items_armor.insert(7, 4, "Basic Crossbow", "inserts 5 to attack when equipped", 3, 20)
        # drop_items_armor.insert(8, 4, "Advance Crossbow", "inserts 12 to attack and subtracts 2 from strength when equipped", 10, 10)
        # drop_items_armor.insert(9, 5, "Basic Helmet", "inserts 1 to defense when equipped", 1, 15)
        # drop_items_armor.insert(10, 5, "Advance Helmet", "inserts 3 to defense and 1 to stamina when equipped", 2, 20)
        # drop_items_armor.insert(11, 6, "Basic Leggings", "inserts 1 defense when equipped", 1, 30)
        # drop_items_armor.insert(11, 6, "Advance Leggings", "inserts 3 defense and subtracts 1 dexterity when equipped", 3, 20)
        # drop_items_armor.insert(12, 7, "Chainmail", "Extra underbody armour. insert 1 to defense when equipped", 1, 30)
