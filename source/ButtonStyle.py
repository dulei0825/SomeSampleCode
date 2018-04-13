from tkinter import *

class ButtonStyle:
    def __init__(self, root):
        btn_SUNKEN = Frame(root, width=50, height=50, relief=SUNKEN, bd=1)
        btn_SUNKEN.pack()

        btn_SUNKEN = Frame(root, width=50, height=50, relief=SUNKEN, bd=5)
        btn_SUNKEN.pack()


        btn_GROOVE = Frame(root, width=50, height=50, relief=GROOVE, bd=1)
        btn_GROOVE.pack()

        btn_GROOVE = Frame(root, width=50, height=50, relief=GROOVE, bd=5)
        btn_GROOVE.pack()


        btn_SOLID = Frame(root, width=50, height=50, relief=SOLID, bd=1)
        btn_SOLID.pack()

        btn_SOLID = Frame(root, width=50, height=50, relief=SOLID, bd=5)
        btn_SOLID.pack()


        btn_RAISED = Frame(root, width=50, height=50, relief=RAISED, bd=1)
        btn_RAISED.pack()

        btn_RAISED = Frame(root, width=50, height=50, relief=RAISED, bd=5)
        btn_RAISED.pack()


        btn_RIDGE = Frame(root, width=50, height=50, relief=RIDGE, bd=1)
        btn_RIDGE.pack()

        btn_RIDGE = Frame(root, width=50, height=50, relief=RIDGE, bd=5)
        btn_RIDGE.pack()


        btn_FLAT = Frame(root, width=50, height=50, relief=FLAT, bd=1)
        btn_FLAT.pack()

        btn_FLAT = Frame(root, width=50, height=50, relief=FLAT, bd=5)
        btn_FLAT.pack()




if __name__ == "__main__":
    root = Tk()
    root.configure(background="#c0c0c0")
    app = ButtonStyle(root)
    root.mainloop()
    
