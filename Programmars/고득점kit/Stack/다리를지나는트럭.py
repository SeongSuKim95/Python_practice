def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = [0] * bridge_length
    cur_weight = 0
    while bridge:
        answer += 1
        cur_weight -= bridge.pop(0)
        if truck_weights:
            if truck_weights[0] + cur_weight <= weight:
                cur_truck = truck_weights.pop(0)
                cur_weight += cur_truck
                bridge.append(cur_truck)
            else :
                bridge.append(0)
        # print(answer,bridge)
    return answer