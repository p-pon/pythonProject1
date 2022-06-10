def duplicate_encode(word):
    word = word.lower()
    d = {elem: word.count(elem) for elem in set(word)}
    res = ''
    for i in word:
        if d[i] > 1:
            res += ')'
        else:
            res += '('
    return res


print(duplicate_encode("Ab dVqfBLwld(kJXdBG@RlP"))
