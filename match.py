import tkinter as tk
    

def write_slogan():
    print("Tkinter is easy to use!")

counter = 0 
def latest_label(label):
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()

def add_ten():
    global counter
    counter += 10
    
root = tk.Tk()

root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack(side=tk.LEFT)
latest_label(label)
button = tk.Button(root, width=25, command=add_ten)
button.pack(side=tk.LEFT)
latest_label(button)

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=root.destroy)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()
