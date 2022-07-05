from tkinter import *

root = Tk()
root.title("ParkingSpot")
root.minsize(500, 500)

entry_box = Entry()
entry_box.pack()

entry_button = Button(text="Entry")
exit_button = Button(text="Exit")






entry_button.pack()
exit_button.pack()


root.mainloop()