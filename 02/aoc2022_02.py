
def evaluate_game(p1, p2):
    points = get_points_for_chosing(p2)
    transformed_sign = chr(ord(p2)-23)
    if(p1 == transformed_sign ):
        points += 3
    elif (p1 == 'A' and transformed_sign == 'B') or (p1 == 'B' and transformed_sign == 'C') or (p1 == 'C' and transformed_sign == 'A'):
        points += 6
    return points

def get_points_for_chosing(sign):
    if sign == 'X':
        return 1
    elif sign == 'Y':
        return 2
    else:
        return 3

def play_lose_game(p1):
    if p1 == 'A':
        return 'Z'
    elif p1 == 'B':
        return 'X'
    else:
        return 'Y'
def play_draw_game(p1):
    if p1 == 'A':
        return 'X'
    elif p1 == 'B':
        return 'Y'
    else:
        return 'Z'

def play_win_game(p1):
    if p1 == 'A':
        return 'Y'
    elif p1 == 'B':
        return 'Z'
    else:
        return 'X'

def chose_sign(p1, sign):
    if sign == 'X':
        return play_lose_game(p1)
    elif sign == 'Y':
        return play_draw_game(p1)
    else:
        return play_win_game(p1)


def main():
    with open('input.txt') as file:
        lines = file.read()
        games = lines.split('\n')
        points = 0
        for game in games:
            p1, p2 = game.split()
            points += evaluate_game(p1, chose_sign(p1, p2))
    print(points)

if(__name__ == "__main__"):
    main()