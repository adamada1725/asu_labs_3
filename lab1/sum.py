import sys
import logging

logging.basicConfig(level=logging.DEBUG, filemode="w", 
                    filename="sum.log", encoding="utf-8")
log = logging.getLogger(__name__)

def main():
    log.debug(f"sys.argv: {sys.argv}")
    if len(sys.argv)==2 and sys.argv[1]=="/?":
        print("Введите последовательность чисел разделенных пробелом чтобы получить сумму")
        return 0
    try:
        print("Результат:",sum(map(int, sys.argv[1:])))
        return 0
    except ValueError as e:
        log.info(f"{e, str(e)}")
        print("Можно вводить только целые числа! Для справки введите /?")
        return 1
    except Exception as e:
        log.error(f"{e, str(e)}")
        print(f"Неизвестная ошибка:\n{e, str(e)}")
        return 1

if __name__=="__main__":
    main()