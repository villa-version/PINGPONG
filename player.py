class Player():

    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed

    def run(self):
        self.show()
        self.dist_between_player_and_bullet()

    def show(self):
        fill(0,0,0)
        rect(self.x, self.y, self.w, self.h)

    def load_bullet(self, bullet):
        self.bullet = bullet

    def dist_between_player_and_bullet(self):
        if self.x - self.w/2 <= self.bullet.x and self.x + self.w/2 >= self.bullet.x:
            if self.y - self.h/2 < self.bullet.y < self.y:
                self.bullet.speed_y = -abs(self.bullet.speed_y)
            elif self.y + self.h/2 > self.bullet.y > self.y:    
                self.bullet.speed_y = abs(self.bullet.speed_y)

    def move(self, dir):
        if dir == 'LEFT':
            self.x -= self.speed
        elif dir == 'RIGHT':
            self.x += self.speed
