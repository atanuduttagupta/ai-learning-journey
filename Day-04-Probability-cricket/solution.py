import random
import numpy as np

runs_needed = 30
balls = 12

outcomes = [0,1,2,3,4,5]


def simulate_match(runs_to_win, balls):
    runs = 0
    for _ in range(balls):
        score = random.choice(outcomes)
        runs +=  score
        if runs >= runs_to_win:
            return "Win"
    return "Loss"

def estimate_probabilty(target, balls, simulate=1000):
    probabilities = []
    for _ in range(simulate):
        probabilities.append(simulate_match(target, balls))

    win_cnt = probabilities.count("Win")
    return win_cnt/len(probabilities)

history = []

target = 30
balls_left = 12

for ball in range(1,13):
    run = random.choice(outcomes)
    target -= run
    balls_left -= 1

    if target > 0 and balls_left > 0:
        prob = estimate_probabilty(target, balls_left, 500)
    else:
        prob = 1.0 if target <= 0 else 0.0

    history.append([ball, target, run, balls_left, prob])
    print(f'Ball {ball}, run {run}, balls_left {balls_left}, target {target}, Probability {prob:.2f}')
    

    if target <= 0:
        print("Match Win")
        break
    if target > 0 and balls_left == 0:
        print("Match Lost")