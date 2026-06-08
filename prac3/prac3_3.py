raw_input = input("\nВведіть числа через кому (наприклад, 1, 2, 3): ")
string_list = raw_input.split(",") 


numbers_list = [float(item.strip()) for item in string_list]
total_list_sum = sum(numbers_list)
list_average = total_list_sum / len(numbers_list)

print(f"Отриманий список чисел: {numbers_list}")
print(f"Сума елементів: {total_list_sum}")
print(f"Середнє значення: {list_average}")
