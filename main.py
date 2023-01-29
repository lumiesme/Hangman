from Controller import Controller


class Hangman:

    def __init__(self):
        Controller().main()

if __name__ == '__main__':
    # TODO read commandline db name
    # TODO if letter inputed second time read as error  # peaks näitama aint 1 korra tähte kui mitu kord nt A paned, modelis get_user_inputi juures tee, enne if lauset.
    Hangman()