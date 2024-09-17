from tkinter import*

expression = ""
def calculator(event):
    global expression
    character = event.widget.cget("text")
    print(f"{character}")
    display.set(character)
    if character == "=":
        answer = eval(expression)
        expression = str(answer)
        display.set(expression)
    elif character == "C":
        expression = ""
        display.set(expression)
    else:
        expression =expression+ character
        display.set(expression)
        




window = Tk()
window.title("Calculator")
#window.configure(bg = "black")

display = StringVar()



entry = Entry(window, font=("Arial", 12), bg="black", fg="white", textvariable = display)
entry.grid(row=0, column=0, columnspan=4, sticky = "we", ipady=10)

button_7 = Button(window, text="7", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
button_7.grid(row = 1, column = 0)
button_7.bind("<Button-1>", calculator)

button_8 = Button(window, text="8", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
button_8.grid(row = 1, column = 1)
button_8.bind("<Button-1>", calculator)

button_9 = Button(window, text="9", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
button_9.grid(row = 1, column = 2)
button_9.bind("<Button-1>", calculator)

plus = Button(window, text="+", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
plus.grid(row = 1, column = 3)
plus.bind("<Button-1>", calculator)

button_4 = Button(window, text="4", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
button_4.grid(row = 2, column = 0)
button_4.bind("<Button-1>", calculator)

button_5 = Button(window, text="5", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
button_5.grid(row = 2, column = 1)
button_5.bind("<Button-1>", calculator)

button_6 = Button(window, text="6", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
button_6.grid(row = 2, column = 2)
button_6.bind("<Button-1>", calculator)

minus = Button(window, text="-", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
minus.grid(row = 2, column = 3)
minus.bind("<Button-1>", calculator)

button_1 = Button(window, text="1", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
button_1.grid(row = 3, column = 0)
button_1.bind("<Button-1>", calculator)

button_2 = Button(window, text="2", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
button_2.grid(row = 3, column = 1)
button_2.bind("<Button-1>", calculator)

button_3 = Button(window, text="3", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
button_3.grid(row = 3, column = 2)
button_3.bind("<Button-1>", calculator)

multiplication = Button(window, text="*", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
multiplication.grid(row = 3, column = 3)
multiplication.bind("<Button-1>", calculator)

button_0 = Button(window, text="0", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
button_0.grid(row = 4, column = 0)
button_0.bind("<Button-1>", calculator)

decimal = Button(window, text=".", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
decimal.grid(row = 4, column = 1)
decimal.bind("<Button-1>", calculator)

division = Button(window, text="/", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
division.grid(row = 4, column = 2)
division.bind("<Button-1>", calculator)

equals = Button(window, text="=", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
equals.grid(row = 4, column = 3)
equals.bind("<Button-1>", calculator)

clear = Button(window, text="C", font=("Arial", 12), bg="gray", fg="white", width=4, height = 2, borderwidth= 10, relief=RAISED)
clear.grid(row = 5, column = 0, columnspan=4, sticky = "we" )
clear.bind("<Button-1>", calculator)


window.mainloop()
