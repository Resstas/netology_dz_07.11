def parse_date(date_string):
    formats = [
        "%A, %B %d, %Y",
        "%A, %d.%m.%y",
        "%A, %d %B %Y"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    print("Не удалось распознать формат даты. Попробуйте другой формат.")
    return None


def main():
    print("Введите дату (или 'exit' для выхода):")

    while True:
        user_input = input("Введите дату: ")

        if user_input.lower() == 'exit':
            break

        date_object = parse_date(user_input)
        if date_object:
            print(f"Дата: {date_object}")

main()