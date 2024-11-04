from tkinter import Tk
from tkinter import Button
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showerror

from settings import *

class PrimeNumberFrame:

    def __init__(self, root: Tk):

        self.root = root

        self.main_frame = Frame(self.root, relief='solid', background=BG_COLOR_DARK,
                                height=WINDOW_HEIGHT, borderwidth=1)
        
        self.output_frame = Frame(self.main_frame, relief='solid', background=BG_COLOR_DARK,
                                  width=300, height=WINDOW_HEIGHT, borderwidth=1)
        
        self.input_frame = Frame(self.main_frame, relief='solid', background=BG_COLOR_DARK,
                                  width=100, height=70, borderwidth=1)

        self.output_text = ScrolledText(self.output_frame)

        self.input_field = Entry(self.input_frame)
        
        self.submit_btn = Button(self.input_frame, text="Вывести", command=self.submit_btn_handler)

        self.label1 = Label(self.input_frame, text="Введите число")

    def submit_btn_handler(self) -> None:
        try:
            input_num = int(self.input_field.get())
            
            if input_num < 0:
                raise ValueError
            
            self.print_prime_numbers(input_num)
        
        except ValueError as e:
            showerror("Ошибка!",
                      "Введите целое неотрицательное число!")

    def print_prime_numbers(self, n: int):
        self.output_text.delete("1.0", "end")
        prime_numbers = PrimeNumbers.get_primes(n)
        self.output_text.insert("1.0", "\n".join(map(str, prime_numbers)))

    def pack(self) -> None:
        
        self.output_text.pack(fill="both", expand=True)
        
        self.label1.pack(anchor="ne")
        
        self.input_field.pack(anchor="ne")
        
        self.submit_btn.pack()

        self.input_frame.pack_propagate(False)
        self.input_frame.grid(row=0, column=1, sticky="n")

        self.output_frame.pack_propagate(False)
        self.output_frame.grid(row=0, column=0)

        self.main_frame.pack_propagate(False)
        self.main_frame.pack(anchor="w")

class PrimeNumbers:

    @staticmethod
    def get_primes(n: int) -> list[int]:
        ans = [2]*n
        prime_count = 1
        q=3
        while prime_count < n:
            idx = 0
            isprime = True
            while ans[idx]*ans[idx]<=q:
                if q % ans[idx] == 0:
                    isprime = False
                    break
                idx += 1
            if isprime:
                ans[prime_count] = q
                prime_count += 1
            q+=2
        return ans

    @staticmethod
    def get_eratosthenes(n: int) -> list[int]:
        sieve = [False if i % 2 == 0 else True for i in range(n)]
        primes = [2]
        for p in range(3, n, 2):
            if sieve[p]:
                primes.append(p)
                for i in range(p * p, n, p * 2):
                    sieve[i] = False
        return primes
    
    @staticmethod
    def get_sundaram(n: int) -> list[int]:
        numbers = list(range(3, n+1, 2))
        half = (n)//2
        initial = 4

        for step in range(3, n+1, 2):
            for i in range(initial, half, step):
                numbers[i] = 0
            initial += 2*(step+1)

            if initial > half:
                return [2] + [i for i in numbers if i]