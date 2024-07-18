# from tkinter import *

# def insert():
#     entry.insert(0, "Hello")

# def delete():
#     entry.delete(0, END)

# root = Tk()
# root.title("My first app")
# # root.minsize(300,450)
# root.geometry("200x140")

# label = Label(text="Say hello!", font=("Arial", 16, "bold"))
# label.config(bd=10)
# label.pack()

# entry = Entry(width=30)
# entry.pack()

# buttoninsert = Button(text="Click me", bg="#9933ff", fg="#66ff66", width=10, height=1)
# buttoninsert.config(command=insert)
# buttoninsert.pack(side=LEFT, padx=10, pady=15)

# buttoninsert = Button(text="Delete", bg="#99ff33", fg="#cc00cc", width=10, height=1)
# buttoninsert.config(command=delete)
# buttoninsert.pack(side=RIGHT, padx=10, pady=15)

# root.mainloop()


#1

# from tkinter import *

# root = Tk()

# root.title("Colors")
# root.geometry("180x240")

# label = Label(root, anchor="c")
# label.pack()

# entry = Entry(root, justify="center", bd=5)
# entry.pack()

# def red():
#     label.config(text="Red")
#     entry.delete(0, END)
#     entry.insert(0, "#cc0000")

# def orange():
#     label.config(text="Orange")
#     entry.delete(0, END)
#     entry.insert(0, "#ff9900")

# def yellow():
#     label.config(text="Yellow")
#     entry.delete(0, END)
#     entry.insert(0, "#ffff00")


# def green():
#     label.config(text="Green")
#     entry.delete(0, END)
#     entry.insert(0, "#00cc00")


# def blue():
#     label.config(text="Blue")
#     entry.delete(0, END)
#     entry.insert(0, "##0099ff")


# def azure():
#     label.config(text="Azure")
#     entry.delete(0, END)
#     entry.insert(0, "#0000cc")


# def violet():
#     label.config(text="Violet")
#     entry.delete(0, END)
#     entry.insert(0, "##6600cc")

# buttoRed = Button(width=17 , bg="red", command=red)
# buttoRed.pack()

# buttoRed = Button(width=16 , bg="Orange", command=orange)
# buttoRed.pack()

# buttoRed = Button(width=16 , bg="Yellow", command=yellow)
# buttoRed.pack()

# buttoRed = Button(width=16 , bg="Green", command=green)
# buttoRed.pack()

# buttoRed = Button(width=16 , bg="Blue", command=blue)
# buttoRed.pack()

# buttoRed = Button(width=16 , bg="Azure", command=azure)
# buttoRed.pack()

# buttoRed = Button(width=16 , bg="Violet", command=violet)
# buttoRed.pack()

# root.mainloop()


#2
# from tkinter import *



# def showfullname():
#   name = Entry.get()
#   surname = Entry.get()
#   fullname = f"{name} {surname}"
#   fullname.config(text=fullname)

# root = Tk()
# root.title("Entering first and last name")

# name = Label(root, text="Enter a name:")
# name.grid(row=0, column=0, padx=5, pady=5)

# name = Entry(root)
# name.grid(row=0, column=1, padx=5, pady=5)


# surname = Label(root, text="Enter your last name:")
# surname.grid(row=1, column=0, padx=5, pady=5)

# surname = Entry(root)
# surname.grid(row=1, column=1, padx=5, pady=5)


# show = Button(root, text="show", command=showfullname)
# show.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


# fullname = Label(root, text="")
# fullname.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# root.mainloop()

