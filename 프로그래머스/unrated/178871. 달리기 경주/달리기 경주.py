import sys

def solution(players, callings):
    idx_dict = { i : p for i, p in enumerate(players)}
    player_dict = { p : i for i, p in enumerate(players)}
    
    for name in callings:
        i = player_dict[name]
        front_idx = i - 1
        front_name = idx_dict[front_idx]
        
        player_dict[name] -= 1
        player_dict[front_name] += 1
        
        idx_dict[front_idx] = name
        idx_dict[i] = front_name
        
    return list(idx_dict.values())