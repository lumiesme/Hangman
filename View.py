from tkinter import *    # tkinterit kasutad selleks, et näha graafiliselt kogu mängu
import tkinter.font as tkfont
from PIL import Image, ImageTk

class View(Tk):

    def __init__(self, controller, model):
        super().__init__()   # super on selleks, et kasutame Tk interit, et saaks kogu sisu kasutada
        self.controller = controller
        self.model = model
        self.userinput = StringVar()

        # fondid

        self.big_font_style = tkfont.Font(family = 'Courier', size=18, weight='bold')
        self.default_font_style_bold = tkfont.Font(family='Verdana', size=10, weight='bold')
        self.default_font_style = tkfont.Font(family='Verdana', size=10)

        # window properties
        self.geometry('515x200')
        self.title('Hangman TAK22')
        self.center(self)  # center on funkt.mida kirjutanud veel ei ole, lingilt kopeerisime selle, teamsichatis

        # create two frames (allpool tegin def ka, jrk on oluline kui mitu muutujat. kui all on top ja bottom siis peab olema ka siin top ja bottom, mitte bottom ja top)
        self.frame_top, self.frame_bottom, self.frame_image = self.create_two_frames()

        self.image = ImageTk.PhotoImage(Image.open(self.model.image_files[len(self.model.image_files) - 1]))
        self.label_image = None

        # create all buttons, labels and entry
        self.btn_new, self.btn_cancel, self.btn_send = self.create_all_buttons()
        self.lbl_error, self.lbl_time, self.lbl_result = self.create_all_labels()
        self.char_input = self.create_input_entry()

    def main(self):
        self. mainloop()

    @staticmethod
    def center(win):  # alguses kirj.self,win peale seda panin kursori sõnale ja tegin centeri peal klõpsu (pirnike) ja "make metod static" ja siis tekkis staticmethod, mis tähendab muutumatu
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def create_two_frames(self):
        frame_top = Frame(self, bg='#0096FF', height=50)  # blue
        frame_bottom = Frame(self, bg='#EBEB00')  # yellow

        frame_top.pack(fill='both')     # EXAPND st et kõik vaba osa täidetakse värviga
        frame_bottom.pack(expand=True, fill='both')

        # hangman image frame
        frame_img = Frame(frame_top, bg='white', width=130, height=130)
        frame_img.grid(row=0, column=3, rowspan=4, padx=5, pady=5)      # rowspan tähendab, et üle nelja rea teed, 4 rida teeb üheks reaks, vasakul 4 rida nuppe ja paremal üks suur kast

        return frame_top, frame_bottom, frame_img   # meetod tagastab 2 asja, method return three objects


    def create_all_buttons(self):
        # New game
        btn_new = Button(self.frame_top, text='New game', font=self.default_font_style)
        Button(self.frame_top, text='Leaderboard', font=self.default_font_style).grid(row=0, column=1, padx=5, pady=2,
                                                                                      sticky=EW)  #sticky on see, et venitab läänest-itta east to west
        # cancel and send
        btn_cancel = Button(self.frame_top, text='Cancel', font=self.default_font_style, state='disabled')
        btn_send = Button(self.frame_top, text='Send', font=self.default_font_style, state='disabled')

        # place three buttons on frame
        btn_new.grid(row=0, column=0, padx=5, pady=2, sticky=EW)
        btn_cancel.grid(row=0, column=2, padx=5, pady=2, sticky=EW)
        btn_send.grid(row=1, column=2, padx=5, pady=2, sticky=EW)
        return btn_new, btn_cancel, btn_send  # tagastab need nupud

    def create_all_labels(self):
        Label(self.frame_top, text='input letter', font=self.default_font_style_bold).grid(row=1, column=0, padx=5, pady=2)
        lbl_error = Label(self.frame_top, text='Wrong 0 letter(s)', anchor='w', font=self.default_font_style_bold)  #anchor on selleks et kirjutada vasakule poole, näitab millised valed tähed on pandud
        lbl_time = Label(self.frame_top, text='0:00:00', font=self.default_font_style)
        lbl_result = Label(self.frame_bottom, text='Let\'s play'.upper(), font=self.big_font_style)  # kui juba rõhumärke kasutanud, siis selleks ,et veelkord teksti ees kirj, siis tagurpidi kaldkriips ja uuesti rõhumärk

        self.label_image = Label(self.frame_image, image=self.image)
        self.label_image.pack()

        lbl_error.grid(row=2, column=0, columnspan=3, sticky=EW, padx=5, pady=2)
        lbl_time.grid(row=3, column=0, columnspan=3, sticky=EW, padx=5, pady=2)
        lbl_result.pack(padx=5, pady=2)
        return lbl_error, lbl_time, lbl_result  # tagastamine

    def create_input_entry(self):
        char_input = Entry(self.frame_top, textvariable=self.userinput, justify='center', font=self.default_font_style)
        char_input['state'] = 'disabled'
        char_input.grid(row=1, column=1, padx=5, pady=2)
        return char_input

