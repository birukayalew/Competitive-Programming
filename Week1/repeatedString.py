def repeatedString(s, n):
    count=0
    remainder=0
    result=0
    for i in s:
        if i=='a':
            count+=1
    result=((n//len(s))*count)
    remainder=n%len(s)-1
    while remainder>=0:
        if s[remainder-1]=='a':
            result+=1
            remainder-=1
    return result 
print(repeatedString('aba',10))
