def lstrip(s):
    space = " "
    counter = 0
    for i in s:
        if s[counter] == space:
            counter+=1
            continue
        else:
            return s[counter:]
        break
