'''
expected length of a bingo game
'''

import random
import numpy as np
import matplotlib.pyplot as plt

def make_card():
    card = np.zeros([5,5])
    for col in range(5):
        card[:,col] = np.random.choice(range(1,16), 5, replace = False) + col*15
    return card

class Card:
    def __init__(self):
         self.card = make_card()
         self.ticked = np.zeros_like(self.card)
         self.balls = list(np.random.choice(range(1,76),75,replace=False))
         self.ball_idx = 0

         self.ticked[2,2] = 1
         self.card[2,2] = 0
         return
    
    def update(self, n):
        self.ticked[np.where(self.card == n)] = 1
        return

    def check_win(self):
        for i in range(5):
            if sum(self.ticked[i,:]) == 5:
                return True
            
            if sum(self.ticked[:,i]) == 5:
                return True

            if sum(np.diag(self.ticked)) == 5:
                return True

            if sum(np.diag(np.fliplr(self.ticked))) == 5:
                return True

            return False

    def draw_ball(self):
        ball = self.balls[self.ball_idx]
        self.ball_idx += 1
        return ball

    def __str__(self):
        return str(self.card) + '\n\n' +  str(self.ticked) + '\n\n' + str(self.balls)


repeats = 10000
results = []

for i in range(repeats):
    card = Card()

    while not card.check_win():
        ball = card.draw_ball()
        card.update(ball)

    results.append(card.ball_idx)

plt.hist(results, bins = np.arange(5,75,1) - 0.5)
plt.plot([np.mean(results), np.mean(results)], [0,50])
plt.show()
