class Game():
    def __init__(self, Character, Age):
        self.Character = Character
        self.Age = Age

    def score(self):
        if self.Age >= 18:
           print("wow")
        else:
           print("goodbye")

Random_Player = Game('Male', 18)
Random_Player.score()
print(Random_Player)