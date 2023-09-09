import tkinter as tk
from tkinter.messagebox import askyesno, showinfo

window = tk.Tk()
window.title("tic_tac_toe")


global turn, results, points
turn = "X"
results = ["","","","","","","","",""]
points = [0, 0]


def click(btn):
    global turn
    btn = int(btn)
    if results[btn] == "":
        if turn == "X":
            results[btn] = "X"
            buttons[btn]["bg"]="LightBlue"
            buttons[btn]["fg"]="white"
            buttons[btn]["text"]="X"
            turn = "O"
        else:
            results[btn] = "O"
            buttons[btn]["bg"]="pink"
            buttons[btn]["fg"]="white"
            buttons[btn]["text"]="O"
            turn = "X"
    rules()


def rules():
    if (results[0] == results[1] == results[2]) and results[0] != "":
        win(results[0])
    elif (results[3] == results[4] == results[5]) and results[3] != "":
        win(results[3])
    elif (results[6] == results[7] == results[8]) and results[6] != "":
        win(results[6])
    elif (results[0] == results[3] == results[6]) and results[0] != "":
        win(results[0])
    elif (results[1] == results[4] == results[7]) and results[1] != "":
        win(results[4])
    elif (results[2] == results[5] == results[8]) and results[2] != "":
        win(results[5])
    elif (results[0] == results[4] == results[8]) and results[8] != "":
        win(results[0])
    elif (results[2] == results[4] == results[6]) and results[6] != "":
        win(results[2])
    else:
        game_over()


def win(winner):
    if winner == "X":
        points[0] += 1
        showinfo("The End!", "Player One Win The Game :)")
        question()
    else:
        points[1] += 1
        showinfo("The End!","Player Two Win The Game :)")
        question()

def question():
    answer = askyesno(title="restart",message="Do You Want To Play Again?")
    if answer:
        restart()
    else:
        showinfo("Goodbye!","Have A Great Day :)")


def restart():
    global results
    results = ["","","","","","","","",""]
    turn = "X"
    point()
    creat_board()


def game_over():
    if "" not in results:
        showinfo("Oops!", "Game Over!")
        question()


def point():
    board_frame = tk.Frame(window)
    board_frame.grid(row=0)
    label_player_one = tk.Label(board_frame, text="Player One:", font=("Courier", 13), padx=10)
    label_player_two = tk.Label(board_frame, text="Player Two:", font=("Courier", 13), padx=10)
    label_player_one.grid(row=0, column=0)
    label_player_two.grid(row=0, column=2)

    point_frame = tk.Frame(window)
    point_frame.grid(row=1)
    point_one = tk.Label(point_frame, text=points[0], padx=50, font=("Courier", 18))
    point_two = tk.Label(point_frame, text=points[1], padx=50, font=("Courier", 18))
    point_one.grid(row=0, column=0)
    point_two.grid(row=0, column=1)


def creat_board():
    global buttons
    buttons = []
    count = 0
    board_frm = tk.Frame(window)
    board_frm.grid(row=2)
    for row in range(1, 4):
        for column in range(1, 4):
            number = count
            buttons.append(number)
            buttons[number] = tk.Button(board_frm, command=lambda x=f"{number}":click(x))
            buttons[number].config(width=10, height=4, font=("None", 18, "bold"))
            buttons[number].grid(row=row, column=column)
            count += 1


point()
creat_board()


window.mainloop()