def Capitalize():
    a = input()
    s = a.split()
    res = ''
    for i in range(len(s)):
        res += (s[i][0].upper() + s[i][1:len(s[i])].lower()) + ' '
    return res
print(Capitalize())