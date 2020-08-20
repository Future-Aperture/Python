letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {k:v for k, v in zip(letters, points)}

letter_to_points[" "] = 0

def score_word(word):
    score = 0
    for w in word.upper():
        score += letter_to_points.get(w, 0)
    return score


brownie_points = score_word("brownie")

player_to_words = {"player1": ["blue", "tennis", "exit"], "wordNerd": ["earth", "eyes", "machine"], "Lexi Con": ["eraser", "belly", "husky"], "Prof Reader": ["zap", "coma", "period"]}

player_to_points = {}

for k, l in player_to_words.items():
    s = 0
    for w in l:
        s += score_word(w)
    player_to_points[k] = s

print(player_to_points)