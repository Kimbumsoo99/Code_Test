from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    bridge_count = []
    tmp = 0
    while True:
        answer += 1
        for i in range(len(bridge_count)):
            bridge_count[i] += 1
        if len(bridge_count) > 0 and bridge_count[0] == bridge_length + 1:
            bridge.popleft()
            bridge_count.pop(0)
            if len(bridge_count) == 0 and len(truck_weights) == 0:
                return answer

        if len(truck_weights) > 0:
            tmp = truck_weights[0]

        if len(truck_weights) > 0 and sum(bridge) + tmp <= weight:
            bridge.append(truck_weights.pop(0))
            bridge_count.append(1)
