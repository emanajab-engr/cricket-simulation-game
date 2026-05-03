Overview
A command-line based cricket match simulator that allows two teams to play a complete ODI (One Day International) style cricket match. The program simulates both innings with realistic cricket mechanics including toss, batting, bowling, wickets, and match statistics.
Features

Team Management: Input 11 players for each team
Toss System: Coin toss with team selection (Heads/Tails)
Interactive Innings: Input runs (0-6) or wickets (W) for each ball
Real-time Score Display: Live score updates with current batsmen and bowler information
Complete Scorecard: Detailed batting and bowling statistics for both teams
Match Summary: Final scores, results, and Man of the Match
Target Tracking: Second innings shows required runs and balls remaining

Requirements

Python 3.x
No external libraries required (uses only standard library: random)

Installation

Clone the repository:

bash   git clone https://github.com/yourusername/cricket-simulation-game.git
   cd cricket-simulation-game

Ensure Python 3 is installed:

bash   python --version
How to Run
Execute the script using Python:
bashpython cricket_game.py
Usage Instructions
Step 1: Enter Team Information

Input the name of the first team
Enter 11 player names for team 1
Input the name of the second team
Enter 11 player names for team 2

Step 2: Toss

Team 1 calls Heads (H) or Tails (T)
The system determines toss winner
Toss winner decides who bats first

Step 3: Select Number of Overs

Input the total number of overs (e.g., 50 for ODI, 20 for T20)

Step 4: Play the Match
During each ball, input:

0-6: Runs scored by the batsman
W: Wicket (batsman out)

Live Score Display Shows:

Current over and ball number
Total score and wickets
Current batsmen with runs and balls faced
Active bowler

Step 5: View Results
After both innings:

Detailed scorecards for both teams
Match summary with final scores
Winner announcement (by runs or wickets)
Man of the Match award

Project Structure
cricket-simulation-game/
├── cricket_game.py       # Main game file
└── README.md            # Documentation
Key Functions
play_innings(batting_team, bowling_team, total_overs, target=None)
Simulates one complete innings of cricket.

Parameters:

batting_team: List of 11 batsmen names
bowling_team: List of 11 bowlers names
total_overs: Number of overs to play
target: Optional target score for second innings


Returns: Dictionary with match statistics

print_scorecard(batting_team, bowling_team, innings_data)
Displays formatted batting and bowling statistics.
swap(a, b)
Utility function to swap striker and non-striker after odd runs.
line(symbol, size)
Prints a line separator for visual formatting.
Game Mechanics

Batting: Batsmen score runs (0-6 per ball), with odd runs causing a swap
Bowling: Bowlers accumulate stats (runs conceded, wickets, balls bowled)
Overs: 6 balls = 1 over; bowlers rotate after each complete over
Wickets: When all 10 batsmen are out, innings ends
Match Win: Second team must score more than first team's score
Statistics Tracking: Individual player stats for all 22 players

Example Gameplay
Enter the name of the first team: India
Enter the names of players:
1. Virat Kohli
2. Rohit Sharma
... (9 more players)

Enter the name of the second team: Australia
Enter the names of players:
1. Steve Smith
2. David Warner
... (9 more players)

[Toss] India: Heads or Tails?
Press 'H' for Heads and 'T' for Tails: H

Toss result: Heads
India has won the toss!
India will bat first.

Enter number of overs: 50

[Live scoring begins...]
Over 0.0 | Score: 0/0 | Batsmen: Virat Kohli 0(0) & Rohit Sharma 0(0) | Bowler: Mitchell Starc
>> 4
Over 0.1 | Score: 4/0 | Batsmen: Virat Kohli 4(1) & Rohit Sharma 0(0) | Bowler: Mitchell Starc
>> 3
... (match continues)
Notes

The game is fully text-based and interactive
All player positions are maintained throughout the match
Statistics are calculated in real-time
Man of the Match is awarded to the highest run-scorer from the winning team/batting team

Future Enhancements

Save/load match data
Advanced bowling statistics (economy rate, strike rate)
Team strategy options
Match history tracking
GUI interface

Troubleshooting

Invalid Input Error: Ensure you enter 0-6 for runs or 'W' for wicket
Index Error: Make sure you enter exactly 11 player names for each team
Program Crashes: Verify Python 3.x is installed correctly
