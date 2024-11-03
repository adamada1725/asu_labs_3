import tkinter as tk
from tkinter import messagebox, Tk, PhotoImage
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk # type: ignore

from settings import AVATAR, WINDOW_SIZE, TITLE, ICON, FONT, WINDOW_SIZE_SMALL

class FibonacciApp:
    def __init__(self, root: Tk):
        self.root = root
        self.root.geometry(WINDOW_SIZE)
        self.root.title(TITLE)
        self.root.iconphoto(False, PhotoImage(file=ICON))
        self.root.resizable(False, False)
        self.root.configure(background="#e0e0e0")
        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        # Меню "Файл"
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Выход", command=self.root.quit)
        menu_bar.add_cascade(label="Файл", menu=file_menu)

        # Меню "Правка"
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Вырезать", command=self.cut_text)
        edit_menu.add_command(label="Копировать", command=self.copy_text)
        edit_menu.add_command(label="Удалить", command=self.clear_text)
        menu_bar.add_cascade(label="Правка", menu=edit_menu)

        # Меню "Справка"
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="О программе", command=self.show_about)
        menu_bar.add_cascade(label="Справка", menu=help_menu)

        self.root.config(menu=menu_bar)

    def create_widgets(self):
        # Поле для ввода количества чисел
        self.entry_label = tk.Label(self.root, 
                                    text="Введите количество чисел Фибоначчи:",
                                    font=FONT)
        self.entry_label.pack(pady=5)

        self.entry = tk.Entry(self.root, font=FONT)
        self.entry.pack(pady=5)

        # Кнопка для запуска расчета
        self.calc_button = tk.Button(self.root, 
                                     text="Показать числа Фибоначчи", 
                                     command=self.calculate_fibonacci,
                                     font=FONT)
        self.calc_button.pack(pady=5)

        # Поле для вывода результата
        self.result_text = ScrolledText(self.root, 
                                        height=10,
                                        width=50, 
                                        state='disabled',
                                        font=FONT)
        self.result_text.pack(pady=5)

        # Контекстное меню для поля вывода
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Вырезать", command=self.cut_text)
        self.context_menu.add_command(label="Копировать", command=self.copy_text)
        self.context_menu.add_command(label="Удалить", command=self.clear_text)

        self.result_text.bind("<Button-3>", self.show_context_menu)

    def calculate_fibonacci(self):
        try:
            n = int(self.entry.get())
            fibonacci_numbers = self.get_fibonacci(n)
            self.show_result(fibonacci_numbers)
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректное число.")

    def get_fibonacci(self, n):
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib[:n]

    def show_result(self, fibonacci_numbers):
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        for i, num in enumerate(fibonacci_numbers):
            self.result_text.insert(tk.END, f"{i}) {num}\n")
        self.result_text.config(state='disabled')

    def cut_text(self):
        self.result_text.event_generate("<<Cut>>")

    def copy_text(self):
        self.result_text.event_generate("<<Copy>>")

    def clear_text(self):
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state='disabled')

    def show_context_menu(self, event):
        self.context_menu.tk_popup(event.x_root, event.y_root)

    def show_about(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("О программе")
        about_window.geometry(WINDOW_SIZE_SMALL)
        about_window.iconphoto(False, PhotoImage(file=ICON))
        about_window.resizable(False, False)

        # Заголовок
        label = tk.Label(about_window, 
                         text="Программа для вывода чисел Фибоначчи",
                         font=FONT,
                         wraplength=150)
        label.pack(pady=10)

        # Информация об авторе
        author_label = tk.Label(about_window, 
                                text="Автор: Абакумов Адам",
                                font=FONT)
        author_label.pack(pady=5)
        
        try:
            image = Image.open(AVATAR)
            image = image.resize((150, 150))
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(about_window, image=photo)
            image_label.image = photo
            image_label.pack(pady=10)
        except Exception as e:
            error_label = tk.Label(about_window, 
                                   text="Изображение не найдено.",
                                   font=FONT)
            error_label.pack(pady=10)
            print(e)

        close_button = tk.Button(about_window, 
                                 text="Закрыть", 
                                 command=about_window.destroy,
                                 font=FONT)
        close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = FibonacciApp(root)
    root.mainloop()
