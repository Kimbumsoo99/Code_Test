from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    bridge_count = deque()
    while True:
        answer += 1
        tmp = truck_weights[0] if len(truck_weights) > 0 else 0
        for i in range(len(bridge_count)):
            bridge_count[i] += 1
        if len(bridge) != 0 and sum(bridge) + tmp > weight:
            if bridge_count[0] > bridge_length:
                bridge.popleft()
                bridge_count.popleft()
                answer -= 1
                if len(truck_weights) == 0 and len(bridge_count) < 1:
                    break
        else:
            for i in range(len(bridge_count)):
                bridge_count[i] += 1
            if len(bridge) != 0 and bridge_count[0] > bridge_length:
                bridge.popleft()
                bridge_count.popleft()
            if tmp > 0:
                bridge.append(truck_weights.pop(0))
                bridge_count.append(1)
        print(bridge, bridge_count)
        print(truck_weights)

    return answer - 1

print(solution(2, 10, [7,4,5,6]))