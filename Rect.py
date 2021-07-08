class Rect():

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def run(self):
        self.show()

    def show(self):
        fill(255,255,255)
        rect(self.x, self.y, self.w, self.h)
