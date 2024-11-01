import keyboard


print("Здравствуйте! Поиграем?")
dictionary = {"яблоко": {"apple", "pome"}, "банан": {"banana"}, "груша": {"pear"}, "апельсин": {"orange"},
              "киви": {"kiwi"}, }
print('Список возможных действий:')
print('Нажмите "ctrl+f" для поиска слова в словаре')
print('Нажмите "+" для добавления в словарь ')
print('Нажмите  "esc" для выхода')
print("-" * 100)
while True:
    if keyboard.is_pressed("ctrl+f"):

        search_word = input("Введите слово, которое хотите найти:")
        if search_word in dictionary:
            print(f"Слово {search_word} найдено в словаре.")
        else:
            print(f"Слово {search_word} не найдено в словаре.")
            print("-" * 100)
    if keyboard.is_pressed("plus"):
        new_word = input("Введите слово, которое хотите добавить:").replace("+","+")
        if new_word in dictionary:
            print(f"Слова {new_word} уже есть в словаре, давайте добавим к нему перевод.")
            translation = dictionary[new_word]
            while True:
                if keyboard.is_pressed("tab"):
                    word = input("Введите перевод:").strip()
                    translation.add(word)
                    print(dictionary)

    if keyboard.is_pressed("esc"):
        print("Выход из игры выполняется")
        break
