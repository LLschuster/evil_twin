def clamp(value, min, max):
    if value > max:
        return max
    if value < min:
        return min
    return value

class Vector2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y