import tkinter as tk

root = tk.Tk()
root.title("French number dictations")


def check_accuracy():
    print("Checking correctness...")
    if True:
        label.config(text = "Correct!")
    else:
        label.config(text = "Incorrect, try again.")

frame = tk.Frame(root)
frame.grid(row = 0, column = 0)

label = tk.Label(root, text = "")
label.grid(row = 0, column = 0)
btn = tk.Button(root, text = "Check button", command = check_accuracy)
btn.grid(row = 1, column = 0)
root.mainloop()