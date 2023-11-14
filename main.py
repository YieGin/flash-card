from tkinter import *
import random
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}
#pandas
try: 
    data = pd.read_csv("./data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
   

def next_card():
        global current_card, flip_timer
        window.after_cancel(flip_timer)
        current_card = random.choice(to_learn)
        canvas.itemconfig(card_titel, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        canvas.itemconfig(canvas_image, image=front_image)
        flip_timer = window.after(3000, func=flime_card)
    
def flime_card():
    canvas.itemconfig(card_titel, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_image)
    
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/word_to_learn.csv", index=False)

    next_card()

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)


flip_timer =  window.after(3000, func=flime_card)
#canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image =  PhotoImage(file="./images/card_front.png")
back_image =  PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
card_titel = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "bold"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#Button false
button_false = PhotoImage(file="./images/wrong.png")
button = Button(image=button_false, highlightthickness=0,)
button.grid(column=0, row=1)

#Button right
button_right = PhotoImage(file="./images/right.png")
button = Button(image=button_right, highlightthickness=0, command=is_known)
button.grid(column=1, row=1)
next_card()

window.mainloop()