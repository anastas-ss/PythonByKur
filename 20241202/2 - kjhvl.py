class Square:
    __match_args__ = ('x', 'y', 'w')

    def __init__(self, x, y, w):
        self.x, self.y, self.w  = x, y, w

    @property
    def h(self):
        return self.w

    @property
    def s(self):
        return self.w * self.w

    @property
    def center(self):
        return (self.x + self.w / 2, self.y + self.w / 2)

    @property
    def h(self):
        return self.w
    
    @h.setter
    def h(self, val):
        self.w = val

    @s.setter
    def s(self, _):
        pass

    @center.setter
    def center(self, val):
        match len(val):
            case 2:
                self.x = val[0] - self.w / 2
                self.y = val[1] - self.w / 2
            case 4:
                self.x += val[2]
                self.y += val[3]


