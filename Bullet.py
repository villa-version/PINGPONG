class Bullet():

    def __init__(self, x, y, w, h, speed_x, speed_y):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rects = None

    def run(self):
        self.show()
        self.move()
        self.take_damage_to_rects()

    def show(self):
        fill(0,0,0)
        rect(self.x, self.y, self.w, self.h)

    def load_rects(self, rects):
        self.rects = rects

    def take_damage_to_rects(self):
        for item in self.rects[:]:
            if (self.x > item.x - item.w/2 and self.x < item.x + item.w/2 and
                self.y > item.y - item.h/2 and self.y < item.y + item.h/2):
                self.rects.remove(item)

    def move(self):
        self.find_dir()
        self.x += self.speed_x
        self.y += self.speed_y

    def find_dir(self):
        if self.x > width:
            self.speed_x = -abs(self.speed_x)
        elif self.x < 0:
            self.speed_x = abs(self.speed_x)
        elif self.y > height:
            self.speed_y = -abs(self.speed_y)
        elif self.y < 0:
            self.speed_y = abs(self.speed_y)
