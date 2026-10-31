# main.py — версия из практической работы №1
def main():
    try:
        name = input("Введите название товара: ")
        price = float(input("Введите цену: "))
        quantity = int(input("Введите количество: "))

        total = price * quantity
        discount = total * 0.05
        final = total - discount

        print(f"Товар: {name}")
        print(f"Цена: {price}")
        print(f"Количество: {quantity}")
        print(f"Стоимость: {total}")
        print(f"Скидка 5%: {discount}")
        print(f"Итого: {final}")
    except ValueError:
        print("Ошибка: некорректный ввод.")

if __name__ == "__main__":
    main()