import tkinter as tk

placeholder = ""

window = tk.Tk()

window.title("Moja apka")

label = tk.Label(window, text = "Cześć, witaj w mojej pierwszej aplikacji GUI").pack()
button = tk.Button(window, text = "Wciśnij mnie").pack()

window.mainloop()