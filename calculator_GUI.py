import tkinter as tk

def initializationWIndow():
    root = tk.Tk()

    root.geometry('460x460')
    root.title('Calculator')

    return root

def initializationScreen(root):

    screen = [tk.Label(root, bg="#C0CBCB", text='test', width=55, anchor='w', borderwidth=2) for i in range(3)]

    for i in range(len(screen)):
        screen[i].grid(row=i, column=0, ipady=15, ipadx=1)

    return screen


def initializationDataArea(root, screen):
    dataArea = tk.Entry(root, borderwidth=0, highlightcolor='white', highlightbackground='white')
    dataArea.grid(row = len(screen), column=0, ipadx=135, ipady=10)


    return dataArea



if __name__ == '__main__':
    root = initializationWIndow()

    screen = initializationScreen(root)

    daraArea = initializationDataArea(root, screen)

    root.mainloop()



