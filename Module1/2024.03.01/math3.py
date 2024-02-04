import random

player1 = random.randint(1, 6)
print(f"Res1: {player1}")
player2 = random.randint(1, 6)
print(f"Res2: {player2}")

if player1 > player2:
    print("Player 1 won!")
elif player2 > player1:
    print("Player 2 won!")
else:
    print("Its a draw!")