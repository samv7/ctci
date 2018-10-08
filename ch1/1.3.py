

def URLify(st):

    output = [s if s is not " " else "%20" for s in st]
    return "".join(output)


print(URLify("Mr John Smith    "))
