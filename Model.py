import glob


class Model:

    def __init__(self):
        self.database_name = 'databases/hangman_words_ee.db'
        self.image_files = glob.glob('images/*.png')  # all hangman images
        # new game
        self.new_word = None  # sõna, mida tuleb arvata
        self.user_word = []  # tühi list, user find letter
        self.all_user_chars = []  # any letter entered incorrectly
        self.counter = 0  # error counter (wrong letters), loendab valed tähed kokku, pole vaja vist?
        # leaderboard
        self.palyer_name = 'UNKNOWN'
        self.leaderboard_file = 'leaderboard.txt'
        self.score_data = []  # sisaldab eelneva faili sisu. leaderboard file contents



