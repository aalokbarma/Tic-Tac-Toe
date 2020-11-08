from tkinter import *
from tkinter import messagebox as box
from tkinter import ttk
# import pygame
# import time
#
# Clock=pygame.time.Clock()
#x="r"
#while x=="r":

def stop_game():
    box.showinfo("messege","Match Ended")
    root.update()
    loop()

if stop_game==True:
    mainloop()


def loop():
    def callback(r, c):
        global player

        if player == 'X' and states[r][c] == 0 and stop_game == False:
            b[r][c].configure(text='X', fg='blue', bg='white')
            states[r][c] = 'X'
            player = 'O'

        if player == 'O' and states[r][c] == 0 and stop_game == False:
            b[r][c].configure(text='O', fg='orange', bg='black')
            states[r][c] = 'O'
            player = 'X'

        check_for_winner()

    def check_for_winner():
        global stop_game

        for i in range(3):
            if states[i][0] == states[i][1] == states[i][2]=='X':
                b[i][0].config(bg='red')
                b[i][1].config(bg='red')
                b[i][2].config(bg='red')

                box.showinfo("Winner", "Player 'X' won the match.\nThanks for Playing.")
                stop_game = True

        # for i in range(3):
            if states[0][i]== states[1][i]== states[2][i]=='X':
                b[0][i].config(bg='red')
                b[1][i].config(bg='red')
                b[2][i].config(bg='red')

                box.showinfo("Winner", "Player 'X' won the match.\nThanks for Playing.")
                stop_game = True

            if states[0][0] == states[1][1] == states[2][2]=='X':
                b[0][0].config(bg='red')
                b[1][1].config(bg='red')
                b[2][2].config(bg='red')

                box.showinfo("Winner", "Player 'X' won the match.\nThanks for Playing.")
                stop_game = True

            if states[2][0]== states[1][1]== states[0][2]=='X':
                b[2][0].config(bg='red')
                b[1][1].config(bg='red')
                b[0][2].config(bg='red')

                box.showinfo("Winner", "Player 'X' won the match.\nThanks for Playing.")
                stop_game = True

        # if stop_game==True:
        #     box.showinfo("Winner","Player 'X' won the match.\nThanks for Playing.")
            # quit()

            # x_change=1

        for i in range(3):
            if states[i][0]== states[i][1]== states[i][2]=='O':
                b[i][0].config(bg='red')
                b[i][1].config(bg='red')
                b[i][2].config(bg='red')

                box.showinfo("Winner", "Player 'O' won the match.\nThanks for Playing.")
                stop_game = True

        # for i in range(3):
            if states[0][i]== states[1][i]== states[2][i]=='O':
                b[0][i].config(bg='red')
                b[1][i].config(bg='red')
                b[2][i].config(bg='red')

                box.showinfo("Winner", "Player 'O' won the match.\nThanks for Playing.")
                stop_game = True

            if states[0][0]== states[1][1]== states[2][2]=='O':
                b[0][0].config(bg='red')
                b[1][1].config(bg='red')
                b[2][2].config(bg='red')

                box.showinfo("Winner", "Player 'O' won the match.\nThanks for Playing.")
                stop_game = True

            if states[2][0]== states[1][1]== states[0][2]=='O':
                b[2][0].config(bg='red')
                b[1][1].config(bg='red')
                b[0][2].config(bg='red')

                box.showinfo("Winner", "Player 'O' won the match.\nThanks for Playing.")
                stop_game = True


        # if stop_game==True:
        #     box.showinfo("Winner","Player 'O' won the match.\nThanks for Playing.")
        #     quit()
        #     y_change=1
        #
        # x+=x_change
        # y+=y_change










    # root=Tk()
    # root.title("Tic Tac Toe")



    #def point_count():

    #if stop_game==False:
        #box.showwarning("Warning","You have to finish the game yet.")
    #window=Tk()

    #name = ttk.Label(window, text=f"Player 'X' won the match :- {x} times.")
    #name.grid(row=0, column=0 )

    #surname = ttk.Label(window, text=f"Player 'O' won the match :- {y} times.")
    #surname.grid(row=1, column=0)

    #window.mainloop()


    #def submit():
    #if stop_game==False:
        #box.showwarning("Warning","You have to finish the game yet.")
    #if stop_game==True:
        #box.showinfo("Macth Ended","You won the match.")




    b = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

    states = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            b[i][j] = Button(font=("Arial", 60), width=4, bg='powder blue', command=lambda r=i, c=j: callback(r, c))
            b[i][j].grid(row=i, column=j)




    # if stop_game==True:
    #     box.showinfo("Match ended","You won the Match.")

    # y=input("Press 'r' to restart.")
    # x=y.lower()
def submit():
    x=0
    y=0
    x_change=0
    y_change=0
    if stop_game == False:
        box.showwarning("Warning", "You have to finish the game yet.")

    if stop_game==True:

        if box.showinfo("Winner", "Player 'X' won the match.\nThanks for Playing."):
            x_change=1
        if box.showinfo("Winner", "Player 'O' won the match.\nThanks for Playing."):
            y_change=0

        x += x_change
        y += y_change

        root=Tk()

        playerx=ttk.Label(root, text=f"Player 'X' won the match :- {x} times.")
        playerx.grid(row=1,column=0)

        playero=ttk.Label(root, text=f"Player 'O' won the match :- {y} times.")
        playero.grid(row=3,column=0)

        root,mainloop()

        # box.showinfo("Poins", f"Player 'X' won the Match :- {x} times.\nPlayer 'O' won the match :- {y} times.")
    # if stop_game == True:
    #     box.showinfo("Messege", "Thank you for playing.")
    #     quit()


    #root.update()



root=Tk()
root.title("#King_A_B_DeVil.")

submit_button = ttk.Button(root, text="Submit",command=submit)
submit_button.grid(row=4, column=1,padx=15,pady=20)

# b=[[0,0,0],
#         [0,0,0],
#         [0,0,0]]
# states=[[0,0,0],
#         [0,0,0],
#         [0,0,0]]
# for i in range(3):
#     for j in range(3):
#         b[i][j]=Button(font=("Arial",60),width=4,bg='powder blue',command= lambda r=i,c=j:callback(r,c))
#         b[i][j].grid(row=i,column=j)

# def endScreen():
#     global pause, score
#
#     pause = 0
#     stop_game = False
#     while stop_game:
#         pygame.time.delay(100)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 stop_game = True
#                 pygame.quit()
#             if event.type==pygame.MOUSEBUTTONDOWN:
#                 stop_game=True
#
# while stop_game:
#     endScreen()

player='X'
stop_game=False

loop()
mainloop()
