class Game:
    def __init__(self, start, end):
        self.range = [*range(start, end + 1, 1)]
        self.count = 0

    def split_list(a_list):
        half = len(a_list)//2
        return a_list[:half], a_list[half:]

    def play(self):
        print(len(self.range)//2)
    #    self.split_list(self.range)


game1 = Game(1, 20)
game1.play()
