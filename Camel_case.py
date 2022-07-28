def to_camel_case(underscore_str):
    
    words = underscore_str.strip('_').split('_')
    
    # only one word in input
    if len(words) == 1:
        word = words[0]
        if len(word):   # in case word = ''
            word.replace(word[0], word[0].lower())
        return word

    # more than one words in input
    camelcase_str = ''
    for i, word in enumerate(words):
        word = word.lower()
        if i > 0:
            word = word.capitalize() # 문자열의 첫글자만을 대문자로 바꿔줌
        camelcase_str += word
        
    return camelcase_str

test_str = 'geeks_for_geeks_is_best'
print(to_camel_case(test_str))
