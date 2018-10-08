

def is_unique(st):

    st = st.lower()

    count = dict()
    for s in st:
        if count.get(s)==None:
            count[s] = 1
        else:
            return False
    return True


print(is_unique("asdf"))

print(is_unique("eagle"))

#If we cannot use an additional data structure, we could use an array for
#ascii characters
