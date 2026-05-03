import random


def line(symbol, size):
    print(symbol * size)


def swap(a, b):
    return b, a


def play_innings(batting_team, bowling_team, total_overs, target=None):
    batsman_runs = [0] * 11
    batsman_balls = [0] * 11
    bowler_runs = [0] * 11
    bowler_balls = [0] * 11
    bowler_wickets = [0] * 11

    wicket = 0
    live_score = 0
    striker = 0
    non_striker = 1
    next_player = 2
    current_over = 0
    current_ball = 0
    bowler_index = 10

    print("Enter runs (0-6) or 'W' for wicket.\n")

    while wicket < 10 and current_over < total_overs:
        if target and live_score >= target:
            break

        if target:
            balls_remaining = (total_overs * 6) - (current_over * 6 + current_ball)
            print(f"\nOver {current_over}.{current_ball} | Score: {live_score}/{wicket} | "
                  f"Need: {target - live_score} off {balls_remaining} | "
                  f"Batsmen: {batting_team[striker]} {batsman_runs[striker]}({batsman_balls[striker]}) "
                  f"& {batting_team[non_striker]} {batsman_runs[non_striker]}({batsman_balls[non_striker]}) | "
                  f"Bowler: {bowling_team[bowler_index]}")
        else:
            print(f"\nOver {current_over}.{current_ball} | Score: {live_score}/{wicket} | "
                  f"Batsmen: {batting_team[striker]} {batsman_runs[striker]}({batsman_balls[striker]}) "
                  f"& {batting_team[non_striker]} {batsman_runs[non_striker]}({batsman_balls[non_striker]}) | "
                  f"Bowler: {bowling_team[bowler_index]}")

        user_input = input(">> ").strip().upper()

        if user_input == 'W':
            print(f"{batting_team[striker]} OUT!")
            wicket += 1
            batsman_balls[striker] += 1
            bowler_wickets[bowler_index] += 1
            bowler_balls[bowler_index] += 1
            current_ball += 1
            if next_player < 11:
                striker = next_player
                next_player += 1
            else:
                break

        elif user_input in '0123456':
            run = int(user_input)
            live_score += run
            batsman_runs[striker] += run
            bowler_runs[bowler_index] += run
            batsman_balls[striker] += 1
            bowler_balls[bowler_index] += 1
            current_ball += 1
            if run % 2 == 1:
                striker, non_striker = swap(striker, non_striker)
        else:
            print("Invalid input! Enter 0-6 or W.")
            continue

        if current_ball == 6:
            current_over += 1
            current_ball = 0
            striker, non_striker = swap(striker, non_striker)
            bowler_index = (bowler_index - 1 + 11) % 11
            print(f"---- End of Over {current_over} ----")

    return {
        "score": live_score,
        "wickets": wicket,
        "overs": current_over,
        "balls": current_ball,
        "batsman_runs": batsman_runs,
        "batsman_balls": batsman_balls,
        "bowler_runs": bowler_runs,
        "bowler_balls": bowler_balls,
        "bowler_wickets": bowler_wickets,
    }


def print_scorecard(batting_team, bowling_team, innings_data):
    print(f"\n{'Batting:'}")
    print(f"{'Batsman':<40}{'Runs':<15}{'Balls':<15}")
    for i in range(11):
        print(f"{batting_team[i]:<40}{innings_data['batsman_runs'][i]:<15}{innings_data['batsman_balls'][i]:<15}")

    print(f"\n{'Bowling:'}")
    print(f"{'Bowler':<40}{'Overs':<15}{'Runs':<15}{'Wickets':<15}")
    for i in range(11):
        if innings_data['bowler_balls'][i] > 0:
            overs_str = f"{innings_data['bowler_balls'][i] // 6}.{innings_data['bowler_balls'][i] % 6}"
            print(f"{bowling_team[i]:<40}{overs_str:<15}{innings_data['bowler_runs'][i]:<15}{innings_data['bowler_wickets'][i]:<15}")


def main():
    # ---- Enter Team Names and Players ----
    team_one_name = input("Enter the name of the first team: ").strip()
    print("Enter the names of players:")
    team1 = []
    for i in range(11):
        player = input(f"{i+1}.\t").strip()
        team1.append(player)

    team_two_name = input("Enter the name of the second team: ").strip()
    print("Enter the names of players:")
    team2 = []
    for i in range(11):
        player = input(f"{i+1}.\t").strip()
        team2.append(player)

    # ---- Display Players Side by Side ----
    line('-', 100)
    print(f"{'':}{team_one_name:<50}{team_two_name:<50}")
    line('-', 100)
    print()
    for i in range(11):
        print(f"{team1[i]:<50}{team2[i]:<50}")

    # ---- Toss ----
    toss = random.randint(0, 1)  # 0 = Heads, 1 = Tails

    team1_call = input(f"\n{team_one_name}: Heads or Tails?\nPress 'H' for Heads and 'T' for Tails: ").strip().upper()

    if team1_call not in ['H', 'T']:
        print("ERROR! Invalid input.")
        return

    team2_call = 'T' if team1_call == 'H' else 'H'
    print(f"{team_one_name} has called {'Heads' if team1_call == 'H' else 'Tails'}.")
    print(f"{team_two_name} has called {'Heads' if team2_call == 'H' else 'Tails'}.")
    print(f"Toss result: {'Heads' if toss == 0 else 'Tails'}")

    team_one_won_toss = (toss == 0 and team1_call == 'H') or (toss == 1 and team1_call == 'T')

    if team_one_won_toss:
        print(f"{team_one_name} has won the toss!\n{team_one_name} will bat first.")
        batting_team = team1
        bowling_team = team2
        batting_team_name = team_one_name
        bowling_team_name = team_two_name
    else:
        print(f"{team_two_name} has won the toss!\n{team_two_name} will bat first.")
        batting_team = team2
        bowling_team = team1
        batting_team_name = team_two_name
        bowling_team_name = team_one_name

    # ---- Number of Overs ----
    total_overs = int(input("Enter number of overs: "))

    # ---- First Innings ----
    print()
    line('-', 43)
    print("FIRST INNINGS")
    line('-', 43)
    print()

    first_innings = play_innings(batting_team, bowling_team, total_overs)
    target = first_innings["score"] + 1

    line('-', 39)
    print("FIRST INNINGS SCORECARD")
    line('-', 39)
    print_scorecard(batting_team, bowling_team, first_innings)
    print(f"\nTARGET: {target}\n")

    # ---- Second Innings ----
    line('-', 43)
    print("SECOND INNINGS")
    line('-', 43)
    print()

    second_innings = play_innings(bowling_team, batting_team, total_overs, target)

    print()
    line('-', 38)
    print("SECOND INNINGS SCORECARD")
    line('-', 38)
    print_scorecard(bowling_team, batting_team, second_innings)

    # ---- Match Summary ----
    print()
    line('-', 43)
    print("MATCH SUMMARY")
    line('-', 43)
    print()

    chasing_team_name = bowling_team_name
    defending_team_name = batting_team_name

    print(f"\n{'TEAM':<20}{'SCORE':<15}{'WICKETS':<10}{'OVERS':<10}")
    line('-', 60)
    print(f"\n{batting_team_name:<20}{first_innings['score']:<15}{first_innings['wickets']:<10}"
          f"{first_innings['overs']}.{first_innings['balls']}")
    print(f"{chasing_team_name:<20}{second_innings['score']:<15}{second_innings['wickets']:<10}"
          f"{second_innings['overs']}.{second_innings['balls']}")
    line('-', 60)
    print()

    score2 = second_innings["score"]
    wicket2 = second_innings["wickets"]

    if score2 >= target:
        print(f"{chasing_team_name} won by {10 - wicket2} wickets.")
    elif score2 == target - 1:
        print("Match tied.")
    else:
        print(f"{defending_team_name} won by {target - 1 - score2} runs.")

    # ---- Man of the Match ----
    best_runs = -1
    mom = ""

    if score2 >= target:
        for i in range(11):
            if second_innings["batsman_runs"][i] > best_runs:
                best_runs = second_innings["batsman_runs"][i]
                mom = bowling_team[i]
    else:
        for i in range(11):
            if first_innings["batsman_runs"][i] > best_runs:
                best_runs = first_innings["batsman_runs"][i]
                mom = batting_team[i]

    print(f"\nMAN OF THE MATCH: {mom} ({best_runs} runs)")


if __name__ == "__main__":
    main()
