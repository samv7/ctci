

def is_permutation(str1, str2):

    count1 = letter_count(str1)
    count2 = letter_count(str2)

    if len(count1) != len(count2):
        return False

    for s in count1.keys():
        if count1[s] != count2[s]:
            return False

    return True

def letter_count(str1):
    count = dict()
    for s in str1:
        if count.get(s)==None:
            count[s] = 1
        else:
            count[s] = count[s] + 1
    return count

print(is_permutation("asdf", "fsad"))
print(is_permutation("asdf", "fsadoo"))
