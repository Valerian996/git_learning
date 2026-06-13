#print("Hello Git")

players = [
    {"name": "Player1", "kills": 20},
    {"name": "Player2", "kills": 15},
    {"name": "Player3", "kills": 30}
]

best_player = max(players, key=lambda p: p["kills"])

print(f"Best player: {best_player['name']} ({best_player['kills']} kills)")
