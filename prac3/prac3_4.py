float_num = float(input("\nВведіть дробове число: "))
precision = int(input("Скільки знаків після коми залишити? "))


formatted_output = f"{float_num:.{precision}f}"
print(f"Відформатований результат: {formatted_output}")