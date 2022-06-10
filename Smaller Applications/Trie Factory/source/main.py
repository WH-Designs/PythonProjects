from trie import Trie
from blessed import Terminal


def trie_factory():
    trie = Trie()

    with open('wiktionary.txt') as file:
        lines = file.readlines()

        count = 0
        for line in lines:
            if count == 0:
                count += 1
                continue

            tokens = line.split('\t')
            trie.add((tokens[1]).strip())

    return trie


def main():
    trie = trie_factory()
    count = 0

    terminal = Terminal()

    with terminal.cbreak():
        print("Enter search term: ", end='')
        ch = terminal.inkey()
        search_term = ''
        matches_copy = []

        while not ch.isdigit():
            search_term += ch
            print('\033c')
            print(f"Enter search term: {search_term}", end='')

            if len(search_term) >= 3:
                matches = trie.search_by_prefix(search_term)
                print()
                for i, match in enumerate(matches):
                    print(f'{i + 1}: {match}')
                    matches_copy.append(match)
                    count += 1
                    if count == 5:
                        break

            ch = terminal.inkey()

        print(f'You chose {matches_copy[int(ch) - 1]}')


if __name__ == '__main__':
    main()
