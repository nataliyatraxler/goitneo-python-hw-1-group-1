def process_command(command):
    if command == "привіт":
        return "Привіт! Як я можу вам допомогти?"
    elif command == "погода":
        return "Зараз сонячно і тепло."
    elif command == "новини":
        return "Останні новини: ..."
    elif command == "допомога":
        return "Ви можете запитати про погоду, новини або просто попрощатися."
    elif command == "прощавай":
        return "До побачення! Будьте здорові."
    else:
        return "Вибачте, я не розумію цієї команди."

def main():
    print("Привіт! Я ваш бот-асистент. Введіть команду або 'прощавай', щоб вийти.")
    while True:
        user_input = input("Введіть команду: ").lower()
        if user_input == "прощавай":
            print(process_command(user_input))
            break
        else:
            print(process_command(user_input))

if __name__ == "__main__":
    main()
