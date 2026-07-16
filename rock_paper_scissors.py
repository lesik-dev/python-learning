import random

def get_player_choice():
    choice = input("Вибери: (камінь/ножиці/папір) ")

    return choice


def get_computer_choice():
    choices = ["камінь", "ножиці", "папір"]
    choice = random.choice(choices)

    return choice

def determine_winner(player, computer):
    if player == "камінь" and computer == "ножиці":
        return "Ти переміг!"
    elif player == "ножиці" and computer == "папір":
        return "Ти переміг!"
    elif player == "папір" and computer == "камінь":
        return "Ти переміг!"
    elif player == computer:
        return "Нічия"
    else:
        return "Комп'ютер переміг!"


def get_result(result, player_score, computer_score):
    if result == "Ти переміг!":
        player_score += 1
    elif result == "Комп'ютер переміг!":
        computer_score += 1

    return player_score, computer_score


player_score = 0
computer_score = 0


while True:
    player = get_player_choice()
    if player not in ["камінь", "ножиці", "папір", "exit"]:
        print("Неправильний вибір!")
        continue
    
    
    
    if player == "exit":
        if player_score > computer_score:
            print("Ти виграв гру!")
        elif player_score < computer_score:
            print("Комп'ютер виграв гру!")
        else:
            print("Загальна нічия")
        break
    computer = get_computer_choice()
    

    result = determine_winner(player, computer)
    

    player_score, computer_score = get_result(
        result,
        player_score,
        computer_score
    )
    
    print(f"Ти: {player}")
    print(f"Комп'ютер: {computer}")
    print(result)

    print("Рахунок:")
    print("==" * 25)
    print(f"Ти: {player_score}")
    print(f"Комп'ютер: {computer_score}")

    if player_score == 3:
        print("Ти переміг у грі")
        break
    if computer_score == 3:
        print("Комп'ютер переміг гру!")
        break