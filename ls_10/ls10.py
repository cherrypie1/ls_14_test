# У вас есть файл raw_data.txt, который содержит "сырые" данные о транзакциях. Данные имеют неструктурированный формат
# и могут содержать ошибки. Пример содержимого:
# Задача:
# Напишите скрипт, который:
# Читает данные из файла raw_data.txt.
# Удаляет строки с ошибками (где вместо значений стоит ERROR).
# Преобразует оставшиеся данные в формат Дата,Сумма,Менеджер.
# Сохраняет очищенные данные в новый файл cleaned_data.txt.


# предполагается что о уже есть файл raw_data.txt

def clean_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file__1:
        lines = file__1.readlines()
    cleaned_data = []

    for line in lines:
        line = line.strip()
        if 'ERROR' not in line:
            parts = line.split(':')
            date, amount, manager = parts
            cleaned_data.append(f"Дата: {date}, Сумма: {amount}, Менеджер: {manager}")

    with open(output_file, 'w', encoding='utf-8') as file__2:
        for entry in cleaned_data:
            file__2.write(entry + "\n")


clean_data('raw_data.txt', 'cleaned.txt')


# Задача 1.
# Создать и обработать файлы
# 1. Нужно создать файлы:
# Каждый файл имеет формат sales_YYYY_MM.txt, где YYYY — год, а MM — месяц.
# Внутри каждого файла данные представлены в формате:
# Дата:Сумма продаж:Менеджер.
# 2. Напишите скрипт, который:
# - Считает общую сумму продаж за все месяцы.
# - Находит менеджера с наибольшей суммой продаж.
# - Сохраняет результаты в файл report.txt в формате:
# Общая сумма продаж: <сумма>
# Лучший менеджер: <имя менеджера>

data_2023_01 = [
    "2023-01-01:1000:Иван Иванов",
    "2023-01-02:1500:Петр Петров",
    "2023-01-03:2000:Мария Сидорова"
]
data_2023_02 = [
    "2023-02-01:1200:Иван Иванов",
    "2023-02-02:1800:Петр Петров",
    "2023-02-03:2200:Мария Сидорова"
]
data_2023_03 = [
    "2023-03-01:1300:Иван Иванов",
    "2023-03-02:1700:Петр Петров",
    "2023-03-03:2100:Мария Сидорова"
]


def records(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(list(map(lambda x: x + '\n', data)))


def main_func(txt_1, txt_2, txt_3):
    sales_sum = 0
    best_manager = None
    temp_manager = 0

    for txt in [txt_1, txt_2, txt_3]:
        for line in txt:
            data = line.strip().split(':')
            try:
                temp = int(data[1])
                if temp > temp_manager:
                    temp_manager = temp
                    best_manager = data[2]
                sales_sum += temp
            except (IndexError, ValueError) as e:
                print(f"Ошибка при обработке строки: {line.strip()} - {e}")

    return f"Общая сумма продаж: {sales_sum}\nЛучший менеджер: {best_manager}"


records('sales_2023_01.txt', data_2023_01)
records('sales_2023_02.txt', data_2023_02)
records('sales_2023_03.txt', data_2023_03)


try:
    with open('sales_2023_01.txt', 'r', encoding='utf-8') as file_1:
        info_1 = file_1.readlines()
    with open('sales_2023_02.txt', 'r', encoding='utf-8') as file_2:
        info_2 = file_2.readlines()
    with open('sales_2023_03.txt', 'r', encoding='utf-8') as file_3:
        info_3 = file_3.readlines()

    report = main_func(info_1, info_2, info_3)
    records('report.txt', [report])
except FileNotFoundError:
    print(f"Файл не найден")

# Задача 3 Числа фибоначи


def fibonacci(integer):
    if integer <= 0:
        return 0
    elif integer == 1:
        return 1
    else:
      return fibonacci(integer - 1) + fibonacci(integer - 2)


print("Введите число\n")

try:
    n = int(input())
    if n > 0:
        for i in range(n):
            print(f"F({i}) = {fibonacci(i)}")
    else:
        print("Введите число больше нуля")
except ValueError:
    print("Ошибка: Введено не числовое значение")


# Задача 4 декораторы
def my_decorator(func):
    def wrapper():
        print("начало.")
        func()
        print("продолжение следует...")
    return wrapper

@my_decorator
def hello_DE():
    print("моего пути инженера данных")


hello_DE()