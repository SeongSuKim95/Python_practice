

test = { 'a' : 1, 'b': {'c' : 2,'d': {'e':3} }}


result = []
for key, value in test.items():
    if isinstance(value,int):
        result.append(key)
        result.append(value)
    else :
        temp = value
        while not isinstance(temp,int):
            result.append(key)
            for nest_key,nest_value in temp.items():
                temp = nest_value
        result.append(temp)
    result.append('_')
print(result)