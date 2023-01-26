from random import randint
wr_file = open("Readme.txt", "w+")
wr_file.write("Привет, файл!\n")
num = randint(1, 100)
wr_file.write(f'Рандомное число: {num}')
wr_file.close()

r_file = open("Readme.txt", "r")
for i in r_file.read():
    print(i, end='')
r_file.close()