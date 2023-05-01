answers = []
def compare_id(u_id, b_id, b_idx, possible_id):
    
    for str_u,str_b in zip(u_id,b_id):
        if str_b == "*" or str_u == str_b :
            continue
        return possible_id
    
    possible_id[b_idx].add(u_id)
    return possible_id

def count(idx,possible_id,visited):
    global answers
    if idx == len(possible_id):
        temp = set()
        for v,k in visited.items():
            if k :
                temp.add(v)
        answers.append(tuple(temp))
        return 
    
    for id in possible_id[idx]:
        if not visited[id] :
            visited[id] = True
            count(idx+1,possible_id,visited)
            visited[id] = False

def solution(user_id, banned_id):
    global answers
    possible_id = [set() for bid in banned_id]
    
    for b_idx,b_id in enumerate(banned_id):
        
        for u_id in user_id:
            
            if len(b_id) != len(u_id):
                continue
            
            possible_id = compare_id(u_id,b_id,b_idx,possible_id)
            
    temp_id = [list(elem) for elem in possible_id]
    visited = {id : False for id in user_id}
    count(0,temp_id,visited)
    
    return len(set(answers))