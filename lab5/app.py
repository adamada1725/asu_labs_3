from tkinter import Toplevel
from tkinter import Label
from tkinter import PhotoImage
from tkinter import Button
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from PIL import Image, ImageTk

from base import AppBase
from utils import PrimeNumberFrame
from settings import *

class App(AppBase):
    
    def __init__(self):
        super().__init__()

        self.prime_number_frame = PrimeNumberFrame(self.root)
        
        self.prime_number_frame.pack()

        self.info_label = Label(text=f"Программа для вывода простых чисел\n"
                                      "Введите число, до которого нужно посчитать простые числа",
                                wraplength=220)

        self.info_label.place(width=220, relx=1, anchor="ne")

    def close_handler(self) -> None:
        if self.prime_number_frame.output_text.get("1.0", "end"):
            if askyesno("Выход", "Вы уверены, что хотите выйти?"):
                AppBase.close()
        else:
            AppBase.close()
    
    def save(self):
        output = self.prime_number_frame.output_text.get("1.0", "end").strip()
        
        if not output:
            showwarning("Сохранить", "Поле вывода пусто!")
            return

        with open("output.txt", "w") as f:
            f.write(output)
        
        showinfo("Сохранить", "Вывод успешно сохранен в output.txt")
    
    def cut_text(self):
        self.prime_number_frame.output_text.event_generate("<<Cut>>")

    def copy_text(self):
        self.prime_number_frame.output_text.event_generate("<<Copy>>")

    def clear_text(self):
        self.prime_number_frame.output_text.config(state='normal')
        self.prime_number_frame.output_text.delete(1.0, "end")

    def show_about(self):
        about_window = Toplevel(self.root)
        about_window.title("О программе")
        about_window.geometry(WINDOW_SIZE_SMALL)
        about_window.iconphoto(False, PhotoImage(file=ICON))
        about_window.resizable(False, False)

        # Заголовок
        label = Label(about_window, 
                         text="Программа для вывода чисел Фибоначчи",
                         font=FONT,
                         wraplength=150)
        label.pack(pady=10)

        # Информация об авторе
        author_label = Label(about_window, 
                             text="Автор: Абакумов Адам",
                             font=FONT)
        author_label.pack(pady=5)
        
        try:
            image = Image.open(AVATAR)
            image = image.resize((150, 150))
            photo = ImageTk.PhotoImage(image)
            image_label = Label(about_window, image=photo)
            image_label.image = photo
            image_label.pack(pady=10)

        except Exception as e:
            error_label = Label(about_window, 
                                text="Изображение не найдено.",
                                font=FONT)
            error_label.pack(pady=10)
            print(e)

        close_button = Button(about_window, 
                                 text="Закрыть", 
                                 command=about_window.destroy,
                                 font=FONT)
        close_button.pack(pady=10)