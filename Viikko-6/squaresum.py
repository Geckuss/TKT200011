class SquareSum:
    def __init__(self):
        self.sum_x = 0
        self.sum_y = 0
        self.sum_xx = 0
        self.sum_yy = 0
        self.sum_xy = 0
        self.n = 0

    def add(self, x, y):
        self.sum_x += x
        self.sum_y += y
        self.sum_xx += x * x
        self.sum_yy += y * y
        self.sum_xy += x * y
        self.n += 1

    def calc(self, a, b):
        return self.sum_yy + a * a * self.sum_xx + self.n * b * b - 2 * a * self.sum_xy - 2 * b * self.sum_y + 2 * a * b * self.sum_x