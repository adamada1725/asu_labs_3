import sys
import logging
from functools import reduce

logging.basicConfig(level=logging.DEBUG, filemode="w", 
                    filename="mult.log", encoding="utf-8")
log = logging.getLogger(__name__)

def mult(sequence: list) -> int:
    try:
        if len(sequence)<=1:
            print("Необходимо ввести не менее 2 чисел!")
            return 1
        return reduce(lambda i,j: i*j, (map(int, sequence)))
    except ValueError as e:
        log.info(f"{e, str(e)}")
        print(f"--> {sequence}\nМожно вводить только целые числа! Для справки введите /?")
        return 1
    except Exception as e:
        log.error(f"{e, str(e)}")
        print(f"Неизвестная ошибка:\n{e, str(e)}")
        return 1

def main(argv: list) -> int:
    log.debug(f"sys.argv: {argv}")
    if len(argv)==2 and argv[1]=="/?":
        print("Введите последовательность чисел (не менее двух) разделенных пробелом чтобы получить произведение")
        return 0
    return mult(argv[1:])

if __name__=="__main__":
    sys.exit(main(sys.argv))