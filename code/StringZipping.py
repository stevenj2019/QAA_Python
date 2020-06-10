
def zip(word1, word2):
    list1 = list(word1)
    list2 = list(word2)
    result = list()
    for i in range(0, len(word1)-1):
        result.append(list1[i])
        result.append(list2[i])
    return "".join(result)
