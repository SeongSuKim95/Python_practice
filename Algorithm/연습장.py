def find_parent(parent,x):
    if parent[x] != x :
        x = find_parent(parent, parent[x])
    return x 

def union(parent,a,b):
    
    parent_a, parent_b = find_parent(parent,a), find_parent(parent,b)
    
    if parent_a < parent_b :
        parent[parent_b] = parent_a
    elif parent_b < parent_a :
        parent[parent_a] = parent_b

v,e = list(map(int,input().split()))

# root table 만들기
parent = [i for i in range(0,v+1)]

for _ in range(e):
    a,b = list(map(int,input().split()))
    union(parent,a,b)

for i in range(1,v+1):
    print(find_parent(parent,i),end = ' ')
    
print(*parent)

# print(find_parent(parent,7))
# print(find_parent(parent,2))
# union(parent,2,7)
# print(find_parent(parent,7))
# print(find_parent(parent,2))