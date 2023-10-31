import pyperclip

def add_text_to_clipboard(text):
    pyperclip.copy(text)

print("Pyperclip is successfully started.\n")

while True:
    # Заранее вписанный первый блок кода
    first_block_code = "Напиши мне описание для игры "

    # Ввод пользователем второго блока кода
    second_block_code = input("Enter the name of the game: ")

    # Заранее вписанный последний блок кода
    last_block_code = " . Оно должго состоять с 3-4 предложений. Оно должно быть на русском языке. В нём обязательно должно быть словосочетание 'купить " + second_block_code + "'. Оно должно описывать элементы геймплея и общие достоинства игры."

    # Объединение всех блоков кода
    final_code = first_block_code + second_block_code + last_block_code

    # Добавление кода в буфер обмена
    add_text_to_clipboard(final_code)
    print("Text have successfully added to clipboard.\n")