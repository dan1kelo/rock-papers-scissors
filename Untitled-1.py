from enum import Enum

class Variants(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Player:
    def __init__(self, variant=Variants.ROCK, name="Player"):
        self.variant = variant
        self.name = name

    def whoWins(self, other):
        if self.variant == other.variant:
            return "Ничья"
        elif (self.variant == Variants.ROCK and other.variant == Variants.SCISSORS) or \
             (self.variant == Variants.SCISSORS and other.variant == Variants.PAPER) or \
             (self.variant == Variants.PAPER and other.variant == Variants.ROCK):
            return f"{self.name} победил!"
        else:
            return f"{other.name} победил!"

def main():
    name1 = input("Введите имя первого игрока: ")
    name2 = input("Введите имя второго игрока: ")
    choice1 = int(input(f"Выбор {name1} (1-ROCK, 2-PAPER, 3-SCISSORS): "))
    choice2 = int(input(f"Выбор {name2} (1-ROCK, 2-PAPER, 3-SCISSORS): "))

    player1 = Player(Variants(choice1), name1)
    player2 = Player(Variants(choice2), name2)

    result = player1.whoWins(player2)
    print(result)

if __name__ == "__main__":
    main()
