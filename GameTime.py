from datetime import datetime


class GameTime:

    def __init__(self, label_time):
        self.label_time = label_time    # label where is time
        self.counter = 0
        self.running = False

    def update(self):
        if self.running:
            if self.counter == 0:
                display = '0:00:00'
            else:
                tt = datetime.utcfromtimestamp(self.counter)
                string = tt.strftime('%T')  # asemel võib kirjutqada ka nii: %H:%M:%S, aga %T tähendab sama
                display = string

            self.label_time['text'] = display
            self.label_time.after(1000, self.update)   # self.update ilma () kindlasti
            self.counter += 1

    def start(self):
        self.running = True
        self.update()

    def stop(self):
        self.running = False

    def reset(self):
        self.counter = 0
        self.label_time['text'] = '0:00:00'

