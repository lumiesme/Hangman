from datetime import datetime
import glob
import sqlite3

from Leaderboard import Leaderboard


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
        self.player_name = 'UNKNOWN'
        self.leaderboard_file = 'leaderboard_1.txt'
        self.score_data = []  # sisaldab eelneva faili sisu. leaderboard file contents

    def start_new_game(self):
        self.get_random_word()
        # print(self.new_word)  # siis näeme konsoolis uut nime, mis ta valis. Test
        self.user_word = []
        self.all_user_chars = []  # kantsulud tähendavad, et teeks tühjaks
        self.counter = 0

        # kõik tähed asendatakse allkriipsuga
        for x in range(len(self.new_word)):
            self.user_word.append('_')

        print(self.new_word)   # test autojuht
        print(self.user_word)  # test ['_', '_', '_', '_', '_', '_', '_', '_',]

    def get_random_word(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.execute('SELECT * FROM words ORDER BY RANDOM() LIMIT 1')   # loo ühendust databaasiga. Sql lause, sest databaas on see fail, kus sõnad
        self.new_word = cursor.fetchone()[1]  # 0 on id, 1 on word. veerunimi.   # fetchone - võtab ühe sõna. See on kursori sees tegelikul, aga tegime kahe reaga, võib ka 1ga teha
        connection.close()  # ühendus andmebaasiga tuleb ka sulgeda, selleks sulgeme ühenduse nii

    def get_user_input(self, userinput):
        if userinput:
            user_char = userinput[:1]  # only first letter
            if (user_char.upper() in self.user_word) or (user_char.upper() in self.all_user_chars):
                self.counter += 1
            elif user_char.lower() in self.new_word.lower():
                self.change_user_input(user_char)  # found letter
            else:  # letter not found
                self.counter += 1
                self.all_user_chars.append(user_char.upper())  # kõik valed tähed pannakse all user char listi, tekivad punasega wrong lahtrissse. paned suure tähega listi



    def change_user_input(self, user_char):
        # replace all _ with found letters
        current_word = self.chars_to_list(self.new_word)
        x = 0
        for c in current_word:
            if user_char.lower() == c.lower():
                self.user_word[x] = user_char.upper()  # asendab tähe mängus kui läks täppi ja teeb trükitäheks
            x +=1

    @staticmethod
    def chars_to_list(string):
        # string to list, tee sõna listiks, st eraldi tähtedeks nt auto .. 'A', 'u', 't', 'o'
        chars = []
        chars[:0] = string
        return chars

    def get_all_user_chars(self):
        return ', '.join(self.all_user_chars)

    def set_player_name(self, name, seconds):
        line = []
        now = datetime.now().strftime('%Y-%m-%d %T')  # datetime now on kuupäeva effekt
        if name.strip():
            self.player_name = name.strip()
        line.append(now)
        line.append(self.player_name)  # kasutaja nimi mis edetabelis näha, allpool kõik muud andmed.
        line.append(self.new_word)  # see sõna mida kasutaja arvas
        line.append(self.get_all_user_chars())  # tagastab stringina kõik kasutaja valesti sisestatud tähed
        line.append(str(seconds))   # teeb sekundid str

        with open(self.leaderboard_file, 'a+', encoding='utf-8') as f:  # failinimi, lisamine ja kodeeering
            f.write(';'.join(line) + '\n')

    def read_leaderboard_file_contents(self):
        self.score_data = []
        empty_List = []
        all_lines = open(self.leaderboard_file, 'r', encoding='utf-8').readlines()  # ühe reaga kogu faili lugemine listi
        for line in all_lines:
            parts = line.strip().split(';')
            empty_List.append(Leaderboard(parts[0], parts[1], parts[2], parts[3], int(parts[4])))
        self.score_data = sorted(empty_List, key=lambda x: x.time, reverse=False)   # obj x mis saime tbl, siis sortime aja järgi

        return self.score_data







