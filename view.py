import text

def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 4:
            return int(choice)
        
def settings():
    print(text.level)
    while True:
        choice = input(text.choice_level)
        if choice.isdigit() and 0 < int(choice) < 6:
            return int(choice)
        
def game():
    name = input('Как вас зовут? ')
    print(f'Привет {name}. Я сейчас загадаю тебе загадку. Отгадаешь, пройдёшь дальше, а если не отгадаешь игра закончится.')
    print(text.first_task)
    while True:
        answear = input('Ваш ответ: ')
        if answear.lower() == text.first_answear:
            print('Ответ верный, поздравляю!')
            break
        else:
            print('Ответ неверный, игра окончена!')
            break
        break