import tkinter as tk

window = tk.Tk()

#greeting = tk.Label(text="Hello, Tkinter")

#greeting.pack()

#button = tk.Button(text="Click me!",width=25,height=5,bg="blue",fg="yellow",)

#entry = tk.Entry(fg="yellow", bg="blue", width=50)

#entry.pack()

#print(entry)
#textbox = tk.Text()
#textbox.pack()


#frame = tk.Frame()
#frame.pack()

def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")

button.bind("<Button-1>", handle_click)

button.pack()

window.mainloop()
