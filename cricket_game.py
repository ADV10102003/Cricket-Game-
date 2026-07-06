import random
import time

class CricketGame:
    def __init__(self):
        self.teams = ["India", "Australia"]  # You can change teams
        self.overs = 5  # Small game - 5 overs each
        self.wickets = 2  # Small team size for simplicity
    
    def play_innings(self, batting_team, bowling_team, target=None):
        print(f"\n--- {batting_team} Batting ---")
        score = 0
        wickets_lost = 0
        balls = 0
        max_balls = self.overs * 6
        
        while balls < max_balls and wickets_lost < self.wickets:
            print(f"\nBall {balls + 1}/{max_balls} | Score: {score}-{wickets_lost}")
            
            # Player choices
            if batting_team == "You":  # Player batting
                print("Choose your shot:")
                print("1. Defensive")
                print("2. Aggressive")
                print("3. Big Hit")
                print("4. Scoop")
                choice = input("Enter choice (1-4): ").strip()
            else:
                choice = str(random.randint(1, 4))  # Computer random
            
            # Bowling outcome (simple randomness)
            bowl_type = random.choice(["fast", "spin", "slow"])
            outcomes = {
                1: [0, 1, 2, 0, 1],      # Defensive
                2: [0, 1, 2, 4, 3, 0],   # Aggressive
                3: [0, 4, 6, 2, -1],     # Big Hit ( -1 = out)
                4: [1, 2, 4, 6, -1]      # Scoop
            }
            
            runs = random.choice(outcomes[int(choice)])
            
            if runs == -1:
                wickets_lost += 1
                print("OUT! ", end="")
                if wickets_lost < self.wickets:
                    print(f"{wickets_lost} wicket down.")
                else:
                    print("All out!")
            else:
                score += runs
                print(f"{runs} runs! ", end="")
                if runs == 4:
                    print("FOUR!")
                elif runs == 6:
                    print("SIX!")
            
            balls += 1
            time.sleep(0.8)
        
        print(f"\n{batting_team} innings ended. Score: {score}-{wickets_lost}")
        return score
    
    def play_game(self):
        print("=== Mini Cricket Game ===")
        print("You are batting first!\n")
        
        # First Innings - Player batting
        player_score = self.play_innings("You", self.teams[1])
        
        print(f"\nTarget for {self.teams[1]}: {player_score + 1}")
        
        # Second Innings - Computer batting
        computer_score = self.play_innings(self.teams[1], "You", player_score + 1)
        
        print("\n" + "="*40)
        if computer_score > player_score:
            print(f"{self.teams[1]} wins by {computer_score - player_score} runs!")
        elif computer_score < player_score:
            print("You win by", player_score - computer_score, "runs!")
        else:
            print("It's a tie!")
        print("="*40)

if __name__ == "__main__":
    game = CricketGame()
    game.play_game()
    
    while input("\nPlay again? (y/n): ").lower() == 'y':
        game = CricketGame()
        game.play_game()
