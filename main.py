class Player:
    """Create Character object"""

    def __init__(self):
        self.Player_Name = None
        self.Player_Race = None
        self.Player_Class = None
        self.Player_Background = None
        self.Player_Abilities = None

    def greet(self):
        print(self.Player_Name, "Welcome to the team")


def main():
    player = new_player()
    print(player.__dict__)
    player.greet()


def new_player():
    player = Player()

    player.Player_Name = input("Player Name: ")
    player.Player_Race = input("Player Race: ")
    player.Player_Class = input("Player Class: ")
    player.Player_Background = input("Player Background: ")
    player.Player_Abilities = input("Player Abilities: ")

    return player


if __name__ == "__main__":
    main()
