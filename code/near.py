def near(word1, word2):
    i = 0 
    while i < len(word1):
        tmp_list = list(word1)
        del tmp_list[i]
        if "".join(tmp_list) == word2:
            return True
        else:
            i=i+1
    return False

print(near("reset", "rest"))
print(near("dragoon", "dragon"))
print(near("sleet", "lets"))