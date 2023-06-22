def solution(players, callings):
    answer = []
    players_num = len(players)
    rank_player = {players[i]: i for i in range(players_num)}

    for i in callings:
        pre, post = rank_player[i], rank_player[i] - 1
        rank_player[players[pre]] = post
        rank_player[players[post]] = pre
        players[pre], players[post] = players[post], players[pre]
    answer = players

    return answer