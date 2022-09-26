from tkinter import Tk, Radiobutton, END
from tkinter import Entry
from tkinter import Button

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

        self.human_r = Radiobutton(text='Human')
        self.human_r.place(x=130, y=20)

        self.winner_ent = Entry(self, width=8)
        self.winner_ent.place(x=110, y=120)
        self.winner_ent.insert(END, 'Draw')
        self.turn_indicator = 'O'

    def next_turn(self):

        for element in self.board_list:
            if element.get() == 'O' or element.get() == 'X':
                element.config(state='disabled')

        for k in [0, 3, 6]:
            if self.board_list[k].get() == self.board_list[k + 1].get() == self.board_list[k + 2].get() and self.board_list[k].get() != '-':
                self.winner_ent.delete(0, 'end')
                self.winner_ent.insert(END, f'{self.turn_indicator} win')

        for k in [0, 1, 2]:
            if self.board_list[k].get()== self.board_list[k + 3].get() == self.board_list[k + 6].get() and self.board_list[k].get() != '-':
                self.winner_ent.delete(0, 'end')
                self.winner_ent.insert(END, f'{self.turn_indicator} win')

        if self.board_list[0].get() == self.board_list[4].get() == self.board_list[8].get() and self.board_list[0].get() != '-':
            self.winner_ent.delete(0, 'end')
            self.winner_ent.insert(END, f'{self.turn_indicator} win')

        if self.board_list[2].get() == self.board_list[4].get() == self.board_list[6].get() and self.board_list[2].get() != '-':
            self.winner_ent.delete(0, 'end')
            self.winner_ent.insert(END, f'{self.turn_indicator} win')

        if self.turn_indicator == 'O':
            self.turn_indicator = 'X'
        else:
            self.turn_indicator = 'O'


    def clear_all(self):

        for element in self.board_list:
            element.config(state='normal')
            element.delete(0, 'end')
            element.insert(END, '-')

        self.winner_ent.delete(0, 'end')
        self.winner_ent.insert(END, 'Draw')
        self.turn_indicator = 'O'



