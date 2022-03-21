from adts.hash_map import HashMap


def main():
    def string_hash_function(key: str) -> int:
        sum: int = 0

        for ch in key:
            sum += ord(ch)

        return sum % 23

    lines = list()

    hash_map = HashMap(23, string_hash_function)

    print('Lyrics Compressor')
    print('Make a selection:\n0: compress file into memory\n1: show word line positions\n2: decompress the output file')
    selection = int(input())

    print()

    run = 'Y'

    while run == 'Y':
        if selection == 0:
            file_name = input('Enter in a file path: ')

            with open(file_name) as file:
                lines = file.readlines()

            word_position = 1

            for line in lines:
                for word in line.split(' '):
                    if word not in hash_map:
                        if '\n' in word:
                            hash_map[word] = f'{-word_position}'
                        else:
                            hash_map[word] = f'{word_position}'
                    else:
                        hash_map[word] += f', {word_position}'
                    word_position += 1

            run = str(input('Do you want to continue running? (Y)es or (N)o:\n')).upper()
        elif selection == 1:
            print()
            for key, value in hash_map.items():
                print(key.rstrip() + ':', value)

            print()
            run = str(input('Do you want to continue running? (Y)es or (N)o:\n')).upper()
        elif selection == 2:
            print()
            output_file_name = input('Enter the output file name: ')

            with open(output_file_name, 'w') as file:
                for line in lines:
                    for word in line.split(' '):
                        file.write(word + ' ')

            run = str(input('Do you want to continue running? (Y)es or (N)o:\n')).upper()

        if run == 'Y':
            print()
            print('Make a selection:\n0: compress file into memory\n1: show word line positions\n2: decompress the output file')
            selection = int(input())


if __name__ == '__main__':
    main()
