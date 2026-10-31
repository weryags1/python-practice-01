# main.py — Вариант 4: Расчёт стоимости покупки (несколько товаров)
def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Ошибка: значение должно быть положительным. Попробуйте снова.")
                continue
            return value
        except ValueError:
            print("Ошибка: введите корректное число.")


def get_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Ошибка: значение должно быть положительным. Попробуйте снова.")
                continue
            return value
        except ValueError:
            print("Ошибка: введите корректное целое число.")


def get_non_empty_string(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if not value:
            print("Ошибка: название товара не должно быть пустым.")
            continue
        return value


def ask_yes_no(prompt: str) -> bool:
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("да", "yes", "y", "д"):
            return True
        if answer in ("нет", "no", "n", "н"):
            return False
        print("Ошибка: введите 'да' или 'нет'.")


def main():
    print("=== Расчёт стоимости покупки ===")
    products = []

    while True:
        name = get_non_empty_string("Введите название товара: ")
        price = get_positive_float("Введите цену: ")
        quantity = get_positive_int("Введите количество: ")

        total = price * quantity
        products.append((name, price, quantity, total))
        print(f"Товар '{name}' добавлен. Стоимость: {total:.2f}")

        if not ask_yes_no("Добавить ещё один товар? (да/нет): "):
            break

    print("\n=== Чек ===")
    grand_total = 0.0
    for name, price, quantity, total in products:
        print(f"{name}: {price} x {quantity} = {total:.2f}")
        grand_total += total

    discount = grand_total * 0.05
    final_total = grand_total - discount

    print(f"\nОбщая стоимость: {grand_total:.2f}")
    print(f"Скидка 5%: {discount:.2f}")
    print(f"Итого к оплате: {final_total:.2f}")


if __name__ == "__main__":
    main()