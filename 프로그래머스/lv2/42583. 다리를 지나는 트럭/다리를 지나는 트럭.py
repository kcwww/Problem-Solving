from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    waiting = deque(truck_weights)
    bridge = deque()
    done = deque()
    on_bridge = 0
    while waiting:
        truck = waiting.popleft()
        on_bridge += truck
        if on_bridge > weight:
            on_bridge -= truck
            waiting.appendleft(truck)
        else:
            bridge.append((truck, answer))
        answer += 1
        if bridge and answer - bridge[0][1] == bridge_length:
            d = bridge.popleft()
            on_bridge -= d[0]
            done.append(d)
            
    while bridge:
        answer += 1
        if bridge and answer - bridge[0][1] == bridge_length:
            d = bridge.popleft()
            done.append(d)

    return answer + 1