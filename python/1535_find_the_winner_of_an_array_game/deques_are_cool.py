from collections import deque

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        victor = None
        wins = 0
        game = deque(arr)
        victor = game.popleft()
        game.appendleft(victor)
        while wins < k:
            first = game.popleft()
            second = game.popleft()
            winner = max(first, second)
            loser = min(first, second)
            if victor == winner:
                wins += 1
            else:
                victor = winner
                wins = 1
            if wins > len(arr):
                break
            game.appendleft(winner)
            game.append(loser)
        return victor
 
