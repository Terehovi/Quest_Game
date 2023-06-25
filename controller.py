import view

def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                while True:
                    choice_difficulty = view.settings()
                    match choice_difficulty:
                        case 1:
                            view.game()
                        case 2:
                            pass
                        case 3:
                            pass
                        case 4:
                            pass
                        case 5:
                            break
            case 2:
                pass
            case 3:
                break