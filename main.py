def new_game():
    import Guesser
    Guesser.guess_word()


def menu():
    print("1. New Game")
    print("2. Exit")


def main():
    menu()
    option = input("What would you like to do?: ")
    if option == '1':
        new_game()
    if option == '2':
        exit(1)


if __name__ == "__main__":
    main()
