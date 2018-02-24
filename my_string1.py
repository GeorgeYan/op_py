def onlyCharNum(s,oth=''):
    s2 = s.lower()
    format = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for i in s2:
        if not i in format:
            s = s.replace(i,"")
    return s

print onlyCharNum("a000 aa-b")
