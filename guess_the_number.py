import random

# Game title
print("#" * 35)
print("𝐆𝐮𝐞𝐬𝐬 𝐭𝐡𝐞 𝐧𝐮𝐦𝐛𝐞𝐫 𝐛𝐞𝐭𝐰𝐞𝐞𝐧 𝟏 𝐚𝐧𝐝 𝟏𝟎𝟎!")
print("#" * 35)


# Generate a random secret number
def number_generation():
    return random.randint(1, 100)


# Get a valid number from the player
def get_player_guess():
    while True:
        try:
            number = int(input("𝗘𝗻𝘁𝗲𝗿 𝗻𝘂𝗺𝗯𝗲𝗿: "))
            return number
        except ValueError:
            print("𝐏𝐥𝐞𝐚𝐬𝐞 𝐞𝐧𝐭𝐞𝐫 𝐚 𝐯𝐚𝐥𝐢𝐝 𝐧𝐮𝐦𝐛𝐞𝐫!")


# Compare the player's guess with the secret number
def check_guess(secret_number, player_guess):
    if secret_number > player_guess:
        return "𝐓𝐨𝐨 𝐥𝐨𝐰!"
    elif secret_number < player_guess:
        return "𝐓𝐨𝐨 𝐡𝐢𝐠𝐡!"
    else:
        return "𝐘𝐨𝐮 𝐠𝐮𝐞𝐬𝐬𝐞𝐝 𝐢𝐭!"


# Initialize game variables
secret_number = number_generation()
attempts = 0


# Main game loop
while True:
    player_guess = get_player_guess()
    attempts += 1

    result = check_guess(secret_number, player_guess)
    print(result)

    # Player guessed correctly
    if result == "𝐘𝐨𝐮 𝐠𝐮𝐞𝐬𝐬𝐞𝐝 𝐢𝐭!":
        print(f"𝐘𝐨𝐮 𝐠𝐮𝐞𝐬𝐬𝐞𝐝 𝐢𝐭 𝐢𝐧 {attempts} 𝐚𝐭𝐭𝐞𝐦𝐩𝐭𝐬!")
        print(f"𝐈𝐭 𝐰𝐚𝐬 𝐭𝐡𝐞 𝐧𝐮𝐦𝐛𝐞𝐫: {secret_number}")

        # Ask the player if they want to play again
        while True:
            choice = input("𝗣𝗹𝗮𝘆 𝗮𝗴𝗮𝗶𝗻? (𝘆𝗲𝘀/𝗻𝗼): ").lower()

            if choice == "yes":
                print("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐧𝐞𝐰 𝐠𝐚𝐦𝐞...")
                secret_number = number_generation()
                attempts = 0
                break

            elif choice == "no":
                print("𝗧𝗵𝗮𝗻𝗸𝘀 𝗳𝗼𝗿 𝘁𝗵𝗲 𝗴𝗮𝗺𝗲!")
                exit()

            else:
                print("𝐏𝐥𝐞𝐚𝐬𝐞 𝐞𝐧𝐭𝐞𝐫 𝐲𝐞𝐬 𝐨𝐫 𝐧𝐨.")
