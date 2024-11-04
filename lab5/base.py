from abc import abstractmethod

from tkinter import Tk
from tkinter import Menu
from tkinter import FALSE
from tkinter import PhotoImage

from settings import *

class AppBase:

    def __init__(self):
        self.root = Tk()

        self.root.option_add("*tearOff", FALSE)

        self.root.config(menu=self.create_menu())

        self.config()

    def create_menu(self) -> Menu:
        file_menu = Menu(self.root)
        file_menu.add_command(label="Сохранить", command=self.save_handler)
        file_menu.add_command(label="Выход", command=self.close_handler)

        editing_menu = Menu(self.root)
        editing_menu.add_command(label="Вырезать", command=self.cut_text)
        editing_menu.add_command(label="Копировать", command=self.copy_text)
        editing_menu.add_command(label="Удалить", command=self.clear_text)

        info_menu = Menu(self.root)
        info_menu.add_command(label="О программе", command=self.show_about)
        
        menu = Menu(self.root)
        menu.add_cascade(label="Файл", menu=file_menu)
        menu.add_cascade(label="Правка", menu=editing_menu)
        menu.add_cascade(label="Справка", menu=info_menu)

        return menu

    def config(self) -> None:
        self.root.geometry(WINDOW_SIZE)
        self.root.title(TITLE)
        self.root.iconphoto(False, PhotoImage(file=ICON))
        self.root.resizable(False, False)
        self.root.configure(background=BG_COLOR)
    
    def save_handler(self) -> None:
        self.save()

    @abstractmethod
    def save(self):
        ...
    
    @abstractmethod
    def cut_text(self):
        ...

    @abstractmethod
    def copy_text(self):
        ...

    @abstractmethod
    def clear_text(self):
        ...
    
    @abstractmethod
    def show_about(self):
        ...

    def close_handler(self) -> None:
        self.close()

    def close(self) -> None:
        self.root.destroy()
    
    def run(self) -> None:
        self.root.mainloop()