import random

def roll_die():
    return random.randint(1, 6)

def player_turn(player_name, total_score):
    turn_score = 0
    while True:
        roll = roll_die()
        print(f"{player_name} rolled: {roll}")
        if roll == 1:
            print("You rolled a 1. Turn over!")
            return 0
        else:
            turn_score += roll
            print(f"Your current score this turn: {turn_score}")
            choice = input("Do you want to roll again? (yes/no): ").lower()
            if choice != 'yes':
                total_score += turn_score
                return total_score

def pig_game():
    players = int(input("Enter the number of players: "))
    player_scores = [0] * players
    player_names = [input(f"Enter name for player {i+1}: ") for i in range(players)]
    winning_score = 50

    while all(score < winning_score for score in player_scores):
        for i, player in enumerate(player_names):
            print(f"\n{player}'s turn (Current Score: {player_scores[i]})")
            player_scores[i] = player_turn(player, player_scores[i])
            if player_scores[i] >= winning_score:
                print(f"\n{player} wins with {player_scores[i]} points!")
                return

if __name__ == "__main__":
    pig_game()
