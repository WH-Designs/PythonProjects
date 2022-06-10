import random

from adts.linked_list import LinkedList
from lab_conga_line.Zombie import Zombie


class CongaLine:

    def __init__(self):
        self._line = LinkedList()
        self._random = random

    def engine(self):
        color = self.random_color(self._random.randint(0, 6))
        self._line.prepend(Zombie(color))
        print(f'{color} zombie is now leading the conga')

    def caboose(self):
        color = self.random_color(self._random.randint(0, 6))
        self._line.append(Zombie(color))
        print(f'{color} zombie now brings up the rear')

    def jump_in_line(self):
        color = self.random_color(self._random.randint(0, 6))
        rand_position = self._random.randint(0, len(self._line))
        self.insert_item(rand_position, color)
        print(f'{color} zombie just jumped in line')

    def everyone_out(self):
        travel = self._line.head

        while travel is not None:
            if travel is self._line.tail:
                if travel == travel.previous:
                    self._line.extract(travel)
                    self._line.remove_last()
            else:
                if travel == travel.next:
                    self._line.extract(travel)
                    self._line.extract(travel.next)

            travel = travel.next

        print(f'Every matching zombie just exited the conga')

    def you_are_done(self):
        travel = self._line.head

        while travel is not None:
            if travel is self._line.tail:
                if travel == travel.previous:
                    self._line.extract(travel)
                    self._line.remove_last()
                    break
            else:
                if travel == travel.next:
                    self._line.extract(travel)
                    self._line.extract(travel.next)
                    break

        '''
            while travel is not None:
            if travel == travel.next:
                self._line.extract(travel)
                break
        '''

        print(f'First matching pair you are out of here')

    def brains(self):
        color = self.random_color(self._random.randint(0, 6))
        self._line.prepend(Zombie(color))
        self._line.append(Zombie(color))
        middle = self.find_middle()
        self._line.insert_before(middle, Zombie(color))

        print(f'{color} zombie brought friends to the party')

    def rainbow_brains(self):
        color = self.random_color(self._random.randint(0, 6))
        self._line.prepend(Zombie(color))

        self._line.append(Zombie('R'))
        self._line.append(Zombie('Y'))
        self._line.append(Zombie('G'))
        self._line.append(Zombie('B'))
        self._line.append(Zombie('M'))
        self._line.append(Zombie('C'))

        print(f'{color} zombie brought everyone')

    def __str__(self):
        return str(self._line)

    def __len__(self):
        return len(self._line)

    def find_middle(self):
        zombies = []

        travel = self._line.head

        while travel is not None:
            zombies.append(travel.item)
            travel = travel.next

        middle = zombies[int(len(zombies) / 2)]

        return middle

    def get_item_at_position(self, position):
        zombies = []

        travel = self._line.head

        while travel is not None:
            zombies.append(travel.item)
            travel = travel.next

        item = zombies[position]

        return item

    def insert_item(self, position, color):
        if position == 0:
            self._line.prepend(Zombie(color))
        elif position == len(self._line):
            self._line.append(Zombie(color))
        else:
            item = self.get_item_at_position(position)
            self._line.insert_after(item, Zombie(color))

    @staticmethod
    def random_color(rand_int: int):
        random_color = 'R'

        if rand_int == 0:
            random_color = 'Y'
        elif rand_int == 1:
            random_color = 'G'
        elif rand_int == 2:
            random_color = 'B'
        elif rand_int == 3:
            random_color = 'M'
        elif rand_int == 4:
            random_color = 'C'

        return random_color
