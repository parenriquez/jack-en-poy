import random


def main():
    """
    Main function to play the Jack en Poy game (Bato, Papel, Gunting) against the computer.
    Tracks and displays the scores of both the computer and player.
    Exits the game when "E" or "e" is entered.
    """
    weapon_names = {1: "Bato", 2: "Papel", 3: "Gunting"}
    terminators = ["E", "e"]
    comp_score = 0
    player_score = 0

    print("Let's play Jack en Poy!")
    print("Bato beats Gunting. Gunting beat Papel. Papel beats Bato.\n")

    while True:
        choice = input("Choose your weapon. [1]Bato [2]Papel [3]Gunting [E/e]End: ")
        if choice.isdigit() and int(choice) in weapon_names:
            new_comp_score, new_player_score = jack_en_poy_rules(
                int(choice), weapon_names
            )
            comp_score += new_comp_score
            player_score += new_player_score
            print(f"Computer: {comp_score} You: {player_score}")

        if choice in terminators:
            print(f"Computer: {comp_score} You: {player_score}")
            print("Thanks for playing!")
            break


def jack_en_poy_rules(choice, weapon_names):
    """
    Determine the outcome of a Jack en Poy game round for a given choice and computer's choice.

    Parameters:
    choice (int) : Player's choice (1 for Bato, 2 for Papel, 3 for Gunting)
    weapon_names (dict) : A dictionary mapping weapon numbers to weapon names

    Returns:
    computer_score (int) : The score earned by the computer (0 or 1)
    player_score (int) : The score earned by the player (0 or 1)
    """
    computer_score = 0
    player_score = 0
    random_comp = random.randint(1, 3)

    result_msg = (
        f"You chose {weapon_names[choice]}. Computer chose {weapon_names[random_comp]}."
    )
    print(result_msg)

    if choice == random_comp:
        print("Draw.")
    elif (choice - random_comp) % 3 == 1:
        print("You win.")
        player_score += 1
    else:
        print("You lose.")
        computer_score += 1

    return computer_score, player_score


if __name__ == "__main__":
    main()
