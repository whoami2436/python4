class Chess:
    def __init__(self, color) :
        self.color = color

    def move (self):
        pass
    
class Pawn(Chess):
    def move(self):
        print("Pawn's ability to take a step forward")

class Knight(Chess):
    def move(self):
        print("The horse's ability to move in an L-shape")

class Bishop(Chess):
    def move(self):
        print("The elephant's ability to move diagonally")

class Rook(Chess):
    def move(self):
        print("Ability of the goal to move forward, backward, right or left")

class Queen(Chess):
    def move(self):
        print("Queen's ability to move in all directions")

class King(Chess):
    def move(self):
        print("King's ability to move one square")

pawn = Pawn("Black")
knight = Knight("White")

pieces = [pawn, knight]

for piece in pieces:
    print(piece.color)
    piece.move()