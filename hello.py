#print("Hello Git")

players = [
    {"name": "Player1", "kills": 20},
    {"name": "Player2", "kills": 15},
    {"name": "Player3", "kills": 30}
]

best_player = max(players, key=lambda p: p["kills"])
worst_player = min(players, key=lambda p: p["kills"])
avg_kills = sum(p["kills"] for p in players) / len(players)
top_players = sorted(players, key=lambda p: p["kills"], reverse=True)

for p in top_players[:3]:
    print(f"{p['name']} - {p['kills']}")
print(f"Best player: {best_player['name']} ({best_player['kills']} kills) and Worst player: {worst_player['name']} ({worst_player['kills']} kills)")
print(f"Average kills: {avg_kills}")