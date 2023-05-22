from ui import create, read, read_filter, update, delete


def main():
    choices = {'1': create,
               '2': read_filter,
               '3': read,
               '4': update,
               '5': delete}

    while True:
        choice = input("""enter
            '1': create,
            '2': read_filter,
            '3': read,
            '4': update,
            '5': delete
            -----------> """)
        if choice in choices:
            choices[choice]()
            input('press something for continue')
        else:
            print('see you next time')


if __name__ == '__main__':
    main()
