from collections import defaultdict
from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            losses[loser] += 1

        no_loss = []
        one_loss = []

        for player in players:
            if losses[player] == 0:
                no_loss.append(player)
            elif losses[player] == 1:
                one_loss.append(player)

        return [sorted(no_loss), sorted(one_loss)]
