import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4")
    else:
        print("Invalid try again")
        
max_score = 30
players_score = [0 for _ in range(players)]

while True:
    
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn just started.!")
        print("Your score is: ", players_score[player_idx],"\n")
        current_score = 0

        while True:
            if current_score  >= max_score:
                print("You have reached the maximum score of", max_score)
                break
            
            should_roll = input("Would you like to roll (y/n): ")
            if should_roll.lower() != "y":
                break   
            
            value = roll()
            if value == 1:
                print("You rolled a 1.! Turn done.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            
            print("You score is : ", current_score)
            
        players_score[player_idx] += current_score
        print("Your score is: ", players_score[player_idx])

        if players_score[player_idx] >= max_score:
            break
    
    if any(score >= max_score for score in players_score):
        break

max_score = max(players_score)
winning_idx = players_score.index(max_score) + 1
print("The winner is player number", winning_idx, "with a score  of:", max_score)        




        




