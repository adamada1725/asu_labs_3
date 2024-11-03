from typing import TypeVar
from math import sqrt
from tkinter import Tk, PhotoImage, ttk, StringVar, Label
from settings import WINDOW_SIZE, TITLE, ICON, FONT

N = TypeVar("N", int, float)

def calculate_area_heron(a: N, b: N, c: N) -> int | float:
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def on_calculate_click():
    try:
        a = float(input_field_1.get())
        b = float(input_field_2.get())
        c = float(input_field_3.get())
        
        if a + b > c and a + c > b and b + c > a:
            area = calculate_area_heron(a, b, c)
            result_var.set(f"Площадь треугольника: {area:.4f} у.е.\u00B2")
            result_label.config(foreground="black")
        else:
            result_var.set("Ошибка: Невозможно образовать треугольник с такими сторонами")
            result_label.config(foreground="red")
    except ValueError:
        result_var.set("Ошибка: Введите числовые значения")
        result_label.config(foreground="red")

def init() -> Tk:
    global input_field_1, input_field_2, input_field_3, result_var, result_label
    
    w = Tk()
    w.geometry(WINDOW_SIZE)
    w.title(TITLE)
    w.iconphoto(False, PhotoImage(file=ICON))
    w.resizable(False, False)
    w.configure(background="#e0e0e0")

    info_text_label = ttk.Label(
        w, text="Введите стороны треугольника", font=FONT, padding=10, borderwidth=1, relief="raised"
    )
    info_text_label.pack(anchor="w", padx=10, pady=10)

    input_field_1 = ttk.Entry(w, font=FONT)
    input_field_2 = ttk.Entry(w, font=FONT)
    input_field_3 = ttk.Entry(w, font=FONT)
    
    input_field_1.pack(anchor="w", padx=10, pady=5)
    input_field_2.pack(anchor="w", padx=10, pady=5)
    input_field_3.pack(anchor="w", padx=10, pady=5)

    result_button = ttk.Button(w, text="Вычислить", padding=10, command=on_calculate_click)
    result_button.pack(anchor="w", padx=10, pady=10)

    # Переменная для хранения и отображения результата
    result_var = StringVar()
    result_label = Label(w, textvariable=result_var, 
                         font=FONT,
                         background="#e0e0e0",
                         wraplength=500,
                         justify="left")
    result_label.pack(anchor="w", padx=10, pady=10)

    return w

def main():
    root = init()
    root.mainloop()

if __name__ == "__main__":
    main()
