import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG, filemode="w", 
                    filename="mults.log", encoding="utf-8")
log = logging.getLogger(__name__)

def main(argv: list) -> int:
    
    log.debug(f"sys.argv: {argv}")
    
    if len(argv)==2 and argv[1]=="/?":
        print(f"Введите название входного файла с числами в качестве первого параметра "
              f"и название выходного файла в качестве второго параметра.\n"
              f"Входной файл должен иметь расширение .txt и состоять строк, состоящих из "
              f"последовательностей чисел.\nНапример: \n5 2 8 8 1\n9 9 9\n1 19 20 1")
        return 0
    
    if len(argv)!=3:
        print("Ошибка!\nНеверное количество параметров. Для справки введите /?")
        return 1
    
    try:
        input_f, output_f = argv[1:3]
        with open(input_f) as input:
            log.debug(f"input: {input}")
            input: list[str] = input.read().split("\n")
            log.debug(f"input: {input}")
        with open(output_f, mode="w") as output:
            res = [str(os.system(f"mult.exe {seq}")) for seq in input]
            log.debug(f"res: {res}")
            output.write("\n".join(res))
            print(f"Результат успешно записан в {output_f}!")

    except FileNotFoundError as e:
        log.info(f"{e, str(e)}")
        print("Ошибка!\nНе найден файл \"input.txt\"")
        return 1
    
    except Exception as e:
        log.error(f"{e, str(e)}")
        print(f"Неизвестная ошибка:\n{e, str(e)}")
        return 1
        
if __name__=="__main__":
    sys.exit(main(sys.argv))