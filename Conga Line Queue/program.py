import random

from adts.linked_list import LinkedList
from lab_conga_line.Conga_Line import CongaLine


def main():
    rand = random
    round_count = 0
    conga_line = CongaLine()

    conga_line.rainbow_brains()

    for i in range(rand.randint(2, 6)):
        conga_line.brains()

    number_of_rounds = int(input('Enter how many rounds you want to run:\n'))

    for i in range(number_of_rounds):
        print('*******************')

        print(f'Round: {round_count}')

        print('The Zombie Line keeps on growing!')

        print(f'Size: {len(conga_line)} :: {conga_line}')

        generate_random_action(rand.randint(0, 6), conga_line)

        if len(conga_line) == 0:
            print('Party is Over')
            break
        else:
            print('Conga line is now')
            print(f'Size: {len(conga_line)} :: {conga_line}')

        round_count += 1

        print('*******************')


def generate_random_action(rand_int, conga_line):
    if rand_int == 0:
        conga_line.engine()
    if rand_int == 1:
        conga_line.caboose()
    if rand_int == 2:
        conga_line.jump_in_line()
    if rand_int == 3:
        conga_line.everyone_out()
    if rand_int == 4:
        conga_line.you_are_done()
    if rand_int == 5:
        conga_line.brains()
    if rand_int == 6:
        conga_line.rainbow_brains()


if __name__ == '__main__':
    main()
