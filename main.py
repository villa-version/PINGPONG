from player import Player
from Rect import Rect
from Bullet import Bullet

class Main():

    def __init__(self):
        self.player = Player(width/2, height/2+200, 75, 25, 10)
        self.bullet = Bullet(width/2, height, 10, 10, -5, -5)
        self.player.load_bullet(self.bullet)
        self.rects = []
        size_of_rects = 10
        quantity_rects = width/size_of_rects
        for i in range(0,quantity_rects):
            self.rects.append(Rect(size_of_rects/2+size_of_rects*i, height/2-200, size_of_rects, 25))
        self.bullet.load_rects(self.rects)

    def run(self):
        self.player.run()
        self.bullet.run()
        for r in self.rects:
            r.run()

    def move_player(self, dir):
        self.player.move(dir)
