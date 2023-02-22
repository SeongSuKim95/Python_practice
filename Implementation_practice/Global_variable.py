N = 5
map_ = [[1] * N for  _ in range(N)]
array = [1] * N 

def change(map_,array):

    map_ = [[0] * N for  _ in range(N)]
    array = [0] * N 

    return map_,array
map_,array = change(map_,array)
print(map_)
print(array)