from tkinter import Tk, PhotoImage, ttk

from settings import WINDOW_SIZE, TITLE, ICON

def init() -> Tk:
    w = Tk()
    w.geometry(WINDOW_SIZE)
    w.title(TITLE)
    w.iconphoto(False, PhotoImage(file=ICON))
    w.resizable(False, False)
    w.configure(background="#e0e0e0")
    info_text_label = ttk.Label(text="Введите стороны треугольника",
                                font=("Comic Sans MS", 16),
                                padding=10,
                                borderwidth=1,
                                relief="raised")
    info_text_label.pack(anchor="w", padx=10, pady=10)
    w.mainloop()
    return w

def main(argv: list) -> int:
    pass

if __name__=="__main__":
    root = init()
    