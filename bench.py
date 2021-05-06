from datetime import datetime, timedelta
loadtime = datetime.now()
import fileworkbase
print("Время загрузки библиотеки", datetime.now() - loadtime)

fileworkbase.space = "/workspace/fileworkbase"

def bench_read():
    frs = 0
    currentSecs = datetime.now()
    a = currentSecs + timedelta(seconds=1)

    while(True):
        fileworkbase.read("loremipsum.txt")
        frs += 1
        currentSecs = datetime.now()

        if(currentSecs >= a):
            print("[OlshaMB] Чтение файлов в секунду", frs)
            
            return frs

def bench_write():
    frs = 0
    currentSecs = datetime.now()
    a = currentSecs + timedelta(seconds=1)

    while(True):
        fileworkbase.write("loremipsum.txt", """Hello, there!
Hello, there! 2
Hello, there! 3""")
        frs += 1
        currentSecs = datetime.now()

        if(currentSecs >= a):
            print("[OlshaMB] Запись файлов в секунду", frs)
            
            return frs


def bench_read_standart():
    frs = 0
    currentSecs = datetime.now()
    a = currentSecs + timedelta(seconds=1)

    while(True):
        open("loremipsum.txt", "r").read()
        frs += 1
        currentSecs = datetime.now()

        if(currentSecs >= a):
            print("[Python] Чтение файлов в секунду", frs)

            return frs

def bench_write_standart():
    frs = 0
    currentSecs = datetime.now()
    a = currentSecs + timedelta(seconds=1)

    while(True):
        file = open("loremipsum.txt", "w")
        file.write("""Hello, there!
Hello, there! 2
Hello, there! 3""");
        file.close()
        frs += 1
        currentSecs = datetime.now()

        if(currentSecs >= a):
            print("[Python] Запись файлов в секунду", frs)

            return frs

def main():
    print("")
    write_olsha = bench_write()
    read_olsha = bench_read()
    write_python = bench_write_standart()
    read_python = bench_read_standart()

    print("")

    if(read_python < read_olsha):
        print("Библиотека OlshaMB лучше читает файлы на", read_olsha - read_python, ". Это в", read_olsha / read_python, "разлучше")
    else:
        print("Библиотека Python лучше читает файлы на", read_python - read_olsha, ". Это в", read_olsha / read_python, "раз лучше")
    if(write_python < write_olsha):
        print("Библиотека OlshaMB лучше записывает файлы на", write_olsha - write_python, ". Это в", write_olsha / write_python, "раз лучше")
    else:
        print("Библиотека Python лучше записывает файлы на", write_python - write_olsha, ". Это в", write_olsha / write_python, "раз лучше")

    print("")

if __name__ == "__main__":
    main()