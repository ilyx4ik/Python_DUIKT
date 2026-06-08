str_num1 = input("\nВведіть перше число: ")
str_num2 = input("Введіть друге число: ")

num1 = float(str_num1)
num2 = float(str_num2)

calc_sum = num1 + num2
calc_diff = num1 - num2
calc_prod = num1 * num2
calc_div = num1 / num2 if num2 != 0 else "Ділення на нуль неможливе"

print(f"Сума: {num1} + {num2} = {calc_sum}")
print(f"Різниця: {num1} - {num2} = {calc_diff}")
print(f"Добуток: {num1} * {num2} = {calc_prod}")
print(f"Частка: {num1} / {num2} = {calc_div}")
