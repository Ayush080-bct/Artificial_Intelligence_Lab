import tkinter as tk

root = tk.Tk()
root.title("My First GUI")

label = tk.Label(root, text="Hello, Aayush!")
label.pack()

button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack()

root.mainloop()
