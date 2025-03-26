# Задача 1. Вычисление корней квадратного уравнения

num_a = float(input("Input a: "))
num_b = float(input("Input b: "))
num_c = float(input("Input c: "))

num_D = num_b**2 - 4*num_a*num_c

num_X1 = (-num_b + num_D**0.5) / (2*num_a)
num_X2 = (-num_b - num_D**0.5) / (2*num_a)

print(f"Results: x1 = {num_X1}, x2 = {num_X2}")

# Задача 2: Вычисление суммы и произведения цифр числа

temp_num = int(input("\nInput three-digit number: "))

hndrds = temp_num // 100
tens = (temp_num % 100) // 10
units = (temp_num % 100) % 10

num_sum = hndrds + tens + units
num_mul = hndrds * tens * units

print(f"Sum = {num_sum}, Multiplication = {num_mul}")

#Задача 3: Доступ в систему
#Столкнулась с тем что в задании "login_correct = ….(input("Правильный логин? (True/False): "))
#(вместо точек нужно сделать приведение типа)", но тогда встает проблема если подставить bool, то всё что мы введем
#будет считаться True, тут либо просить пользователя нажимать Enter( Реализовано в задаче 4), либо без приведения
#сравнивать со строкой(реализовано в данной задаче)

access = False
login_correct = input("\nWatch out for uppercase and lowercase!\nIs login correct? (True/False): ") == "True"
password_correct = input("Is password correct? (True/False): ") == "True"
access_token = input("Has access token? (True/False): ") == "True"

access = (login_correct and password_correct) or access_token

print(f"Access status : {access}")

# Задача 4: Проверка доступа к контенту с учётом блокировки

access = False

sub = bool(input("\nWatch out for uppercase and lowercase!\nIs the subscription active? (True/if False press Enter): "))
age_limit = int(input("Enter user age ")) >= 18
admin_pass = bool(input("Are you an admin? (True/if False press Enter): "))
blocked = bool(input("Is the user blocked? (True/if False press Enter): "))

access = ((sub and age_limit) or admin_pass) and not blocked
#на случай если админ не может быть младше 18
#access = ((sub and age_limit) or (admin_pass and age_limit)) and not blocked

print(f"Access status : {access}")
