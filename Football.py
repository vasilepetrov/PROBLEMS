n = int(input())
team_one_goals = []
team_two_goals = []
for i in range(n):
    current_goal = input()
    if i == 0:
        team_one_goals.append(current_goal)
    else:
        if current_goal in team_one_goals:
            team_one_goals.append(current_goal)
        elif current_goal not in team_one_goals:
            team_two_goals.append(current_goal)

goal_diff = len(team_one_goals) - len(team_two_goals)
if goal_diff < 0:
    print(team_two_goals[0])
else:
    print(team_one_goals[0])


