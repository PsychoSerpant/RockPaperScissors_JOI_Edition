import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "win"
    else:
        return "loss"

def random_task(task_list):
    return random.choice(task_list)

def play_game():
    while True:
        win_count = 0
        loss_count = 0
        tie_count = 0
        rounds_played = 0
        
        victory_tasks = ["Slowly stroke your cock for 10 seconds.", "Gently massage your balls for 15 seconds.", "Alternate between fast and slow strokes for 20 seconds.", "Focus on the tip, stroking it gently for 15 seconds.", "Use your other hand to tug on your balls while jerking off.", "Stop for 5 seconds, then resume stroking at a medium pace.", "Jerk off with one hand while using the other to play with your balls.", "Change hands and jerk off with the other hand for 10 seconds.", "Slowly stroke the shaft while gently tugging on your balls.", "Stop for 10 seconds, then quickly jerk at high pace."]
        defeat_tasks = ["Hold your breath for 10 seconds while stroking your cock.", "Stroke your cock slowly for 15 seconds, then hold your breath for 5 seconds.", "Alternate between fast and slow strokes for 20 seconds, holding your breath for 5 seconds.", "Focus on the tip, stroking it gently for 15 seconds, then hold your breath for 10 seconds.", "Use your other hand to tug on your balls while jerking off, holding your breath for 10 seconds.", "Stop for 5 seconds, then resume stroking at a medium pace, holding your breath for 10 seconds.", "Jerk off with one hand while using the other to play with your balls, holding your breath for 15 seconds.", "Change hands and jerk off with the other hand for 10 seconds, holding your breath for 10 seconds.", "Slowly stroke the shaft while gently tugging on your balls, holding your breath for 15 seconds.", "Stop for 10 seconds, then quickly jerk off to finish while holding your breath for 10 seconds."]
        tie_tasks = ["Stop jerking off and focus on your balls for 30 seconds.", "Use your other hand to play with your nipples while jerking off.", "Change the pace of your strokes randomly for 20 seconds.", "Stop for 10 seconds, then resume jerking off with a faster pace.", "Focus on the tip of your cock for 15 seconds.", "Use your other hand to tug on your balls while jerking off.", "Stop for 5 seconds, then quickly jerk off to finish.", "Alternate between fast and slow strokes for 20 seconds.", "Use both hands to jerk off for 15 seconds."]
        surrender_tasks = ["Eat your own cum after you've finished jerking off. Stay in bondage hands and legs tied up for 2 hours.", "Eat your own cum after you've finished jerking off. Hold your breath for 20 seconds while jerking off, repeat for 5 rounds.", "Eat your own cum after you've finished jerking off. Stop jerking off and stay still for 2 hours.", "Eat your own cum after you've finished jerking off. Use your other hand to tug on your balls while jerking off, repeat for 5 rounds.", "Eat your own cum after you've finished jerking off. Stay in bondage hands and legs tied up for 2 hours, then jerk off with one hand tied behind your back."]
        bonus_tasks = ["Hold your breath for 15 seconds while stroking your cock slowly.", "Stroke your cock quickly for 10 seconds, then hold your breath for 10 seconds.", "Alternate between fast and slow strokes for 20 seconds, holding your breath for 10 seconds.", "Focus on the tip, stroking it gently for 15 seconds, then hold your breath for 15 seconds.", "Use your other hand to tug on your balls while jerking off, holding your breath for 15 seconds.", "Stop for 5 seconds, then resume stroking at a medium pace, holding your breath for 15 seconds.", "Jerk off with one hand while using the other to play with your balls, holding your breath for 15 seconds.", "Change hands and jerk off with the other hand for 10 seconds, holding your breath for 15 seconds.", "Slowly stroke the shaft while gently tugging on your balls, holding your breath for 15 seconds.", "Stop for 10 seconds, then quickly jerk off to finish while holding your breath for 15 seconds."]
        
        low_intensity_tasks = ["Stay in bondage hands and legs tied up for 15 minutes.", "Hold your breath for 5 seconds while jerking off, repeat for 5 rounds.", "Stop jerking off and stay still for 15 minutes."]
        medium_intensity_tasks = ["Eat your own cum after you've finished jerking off. Stay in bondage hands and legs tied up for Half hour.", "Eat your own cum after you've finished jerking off. Hold your breath for 10 seconds while jerking off, repeat for 5 rounds.", "Eat your own cum after you've finished jerking off. Stop jerking off and stay still for Half hour."]
        high_intensity_tasks = ["Eat your own cum after you've finished jerking off. Stay in bondage hands and legs tied up for 2 hours.", "Eat your own cum after you've finished jerking off. Hold your breath for 15 seconds while jerking off, repeat for 5 rounds.", "Eat your own cum after you've finished jerking off. Stop jerking off and stay still for 2 hours."
]
        
        while True:
            player_choice = input("Enter your choice (rock/r, scissors/s, paper/p, surrender/pre cum, bonus/cum): ").strip().lower()
            
            if player_choice in ["rock", "r"]:
                player_choice = "rock"
            elif player_choice in ["scissors", "s"]:
                player_choice = "scissors"
            elif player_choice in ["paper", "p"]:
                player_choice = "paper"
            elif player_choice in ["surrender", "pre cum"]:
                print("You surrendered! Punishment task:", random_task(surrender_tasks))
                break
            elif player_choice in ["bonus", "cum"]:
                if rounds_played < 5:
                    print("Bonus round is only allowed after 5 rounds!")
                    continue
                break
            else:
                print("Invalid choice. Try again.")
                continue
            
            computer_choice = get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            result = determine_winner(player_choice, computer_choice)
            
            if result == "win":
                win_count += 1
                print("You won! Task:", random_task(victory_tasks))
            elif result == "loss":
                loss_count += 1
                print("You lost! Task:", random_task(defeat_tasks))
            else:
                tie_count += 0.5
                print("It's a tie! Task:", random_task(tie_tasks))
            
            rounds_played += 1
        
        if player_choice in ["bonus", "cum"]:
            total_score = win_count + tie_count - loss_count
            win_rate = (win_count / rounds_played) * 100 if rounds_played > 0 else 0
            
            print("BONUS ROUND TASK:", random_task(bonus_tasks))
            
            if win_rate > 70:
                print("{LOW INTENSITY} Additional task:", random_task(low_intensity_tasks))
            elif win_rate > 50:
                print("{MEDIUM INTENSITY} Additional task:", random_task(medium_intensity_tasks))
            else:
                print("{HIGH INTENSITY} Additional task:", random_task(high_intensity_tasks))
            
        print("Game Over! Press 'y' to restart or any other key to exit.")
        restart = input("Restart? (y/n): ").strip().lower()
        if restart != 'y':
            break

if __name__ == "__main__":
    play_game()
