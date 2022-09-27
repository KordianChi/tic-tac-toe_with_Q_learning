from tkinter import Tk, Radiobutton, END, IntVar, BooleanVar, Checkbutton
from tkinter import Entry
from tkinter import Button
from random import randint

class Board(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x200')
        self.title('Tic Tac Toe')

        self.square_11 = Entry(self, width=4)
        self.square_12 = Entry(self, width=4)
        self.square_13 = Entry(self, width=4)
        self.square_21 = Entry(self, width=4)
        self.square_22 = Entry(self, width=4)
        self.square_23 = Entry(self, width=4)
        self.square_31 = Entry(self, width=4)
        self.square_32 = Entry(self, width=4)
        self.square_33 = Entry(self, width=4)

        self.board = [[self.square_11, self.square_12, self.square_13],
                      [self.square_21, self.square_22, self.square_23],
                      [self.square_31, self.square_32, self.square_33]]

        self.board_list = [self.square_11, self.square_12, self.square_13,
                           self.square_21, self.square_22, self.square_23,
                           self.square_31, self.square_32, self.square_33]



        y_pos = 30
        for row in self.board:
            x_pos = 30
            for element in row:
                element.place(x=x_pos, y=y_pos)
                element.insert(END, '-')
                x_pos += 30
            y_pos += 30

        self.turn_btn = Button(text='Next Turn', command=self.next_turn)
        self.turn_btn.place(x=40, y=120)

        self.turn_btn = Button(text='Clear all', command=self.clear_all)
        self.turn_btn.place(x=40, y=150)

        self.difficult_level = IntVar()
        self.difficult_level.set(0)

        self.human_r = Radiobutton(text='Human', variable=self.difficult_level, value=0)
        self.monkey_r = Radiobutton(text='Monkey', variable=self.difficult_level, value=1)
        self.human_r.place(x=130, y=40)
        self.monkey_r.place(x=130, y=60)

        self.winner_ent = Entry(self, width=8)
        self.winner_ent.place(x=110, y=120)
        self.winner_ent.insert(END, 'Draw')

        self.human_first = BooleanVar()
        self.human_first.set(True)
        self.human_first_chk = Checkbutton(self, text='Human move first', variable=self.human_first)
        self.opponent_indicator = 'x'

        self.human_first_chk.place(x=130, y=20)



    def next_turn(self):

        if self.difficult_level.get() == 1:
            if not self.human_first.get():
                self.opponent_indicator = 'o'
            while True:
                position = randint(0, 8)
                if self.board_list[position].get() == '-':
                    self.board_list[position].delete(0, 'end')
                    self.board_list[position].insert(END, self.opponent_indicator)
                    break

        for element in self.board_list:
            if element.get() == 'o' or element.get() == 'x':
                element.config(state='disabled')


        for k in [0, 3, 6]:
            if self.board_list[k].get() == self.board_list[k + 1].get() == self.board_list[k + 2].get() and self.board_list[k].get() != '-':
                self.winner_ent.delete(0, 'end')
                self.winner_ent.insert(END, f'{self.board_list[k].get()} win')
                for element in self.board_list:
                    element.config(state='disabled')

        for k in [0, 1, 2]:
            if self.board_list[k].get()== self.board_list[k + 3].get() == self.board_list[k + 6].get() and self.board_list[k].get() != '-':
                self.winner_ent.delete(0, 'end')
                self.winner_ent.insert(END, f'{self.board_list[k].get()} win')
                for element in self.board_list:
                    element.config(state='disabled')

        if self.board_list[0].get() == self.board_list[4].get() == self.board_list[8].get() and self.board_list[0].get() != '-':
            self.winner_ent.delete(0, 'end')
            self.winner_ent.insert(END, f'{self.board_list[0].get()} win')
            for element in self.board_list:
                element.config(state='disabled')

        if self.board_list[2].get() == self.board_list[4].get() == self.board_list[6].get() and self.board_list[2].get() != '-':
            self.winner_ent.delete(0, 'end')
            self.winner_ent.insert(END, f'{self.board_list[2].get()} win')
            for element in self.board_list:
                element.config(state='disabled')




    def clear_all(self):

        for element in self.board_list:
            element.config(state='normal')
            element.delete(0, 'end')
            element.insert(END, '-')

        self.winner_ent.delete(0, 'end')
        self.winner_ent.insert(END, 'Draw')
        self.opponent_indicator = 'x'



