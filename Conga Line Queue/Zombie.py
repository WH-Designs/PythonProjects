
class Zombie:

    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        self._color = new_color

    def __eq__(self, other):
        return self._color == other._color

    def __str__(self):
        return self._color
