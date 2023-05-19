from tkinter import*
from PIL import ImageTk, Image
root = Tk()

root.title("Endless Dice Game")
root.geometry("600x400")

root.configure(background = "pink")

img = ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

player_1 = Label(root, text = "Player 1", bg = "royal blue", fg = "white")
player_1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player_2 = Label(root, text = "Player 2", bg = "royal blue", fg = "white")
player_2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player_1_score_label = Label(root, bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score_label = Label(root, bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_dice_label = Label(root, bg = "chocolate1", fg = "white")
random_dice_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
root.mainloop()