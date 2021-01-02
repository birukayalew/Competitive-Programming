def Tsum(num1,num2):
    carry=0
    ans=""
    if len(num1)<len(num2):
        num1=(len(num2)- len(num1))*"0"+ num1
    elif len(num1)>len(num2):
        num2=(len(num1)- len(num2))*"0"+ num2
    for i in range(len(num1)-1,-1,-1):
        result=str(int(num1[i])+int(num2[i]) + carry)
        if len(result)!=2:
            result="0"+result
        if i!=0:
            ans=result[1]+ans
            carry=int(result[0])
        else:
            ans=result+ans
    if ans.lstrip('0')=="":
        return '0'
    else:
        return ans.lstrip('0')
num1=input()
num2=input()
print(Tsum(num1,num2))
