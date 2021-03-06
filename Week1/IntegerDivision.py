def sub(num1,num2):
    if len(num1)==len(num2):
        if num1< num2:
            num1,num2=num2,num1
    else:
        if len(num2)>len(num1):
            num1,num2=num2,num1
        num2=(len(num1)-len(num2))*"0" + num2
    result=""
    borrowed=False
    for i in range(len(num1)-1,-1,-1):
        if i !=0:
            if borrowed:
                num=int(num1[i])-1
            else:
                num=int(num1[i])
            if (num-int(num2[i]))<0:
                if num1[i]=='0':
                    if borrowed:
                        result=str(9-int(num2[i])) + result
                    else:
                        result=str(10-int(num2[i])) + result
                else:
                    
                    if borrowed:
                        result=str(int('1'+str((int(num1[i])-1)))-int(num2[i])) + result
                    else:
                        result=str(int('1'+str((int(num1[i]))))-int(num2[i])) + result
                borrowed=True
            else:
                result=str(num-int(num2[i]))+result
                borrowed=False
        else:
            if borrowed:
                result=str((int(num1[0])-1) - int(num2[i])) + result
            else:
                 result=str(int(num1[0])-int(num2[i])) + result
    if result.lstrip('0')=="":
        return '0'
    else:
        return result.lstrip('0')
def Tsum(num1,num2):
    sign=0
    if (num1[0]=='-') and (num2[0]=='-'):
        sign=1
        num1=num1[1:]
        num2=num2[1:]
    if (num1[0]=='-' and num2[0]!='-') or (num1[0]!='-' and num2[0]=='-'):
        if num1[0]=='-':
            if len(num1[1:])==len(num2):
                if num1[1:]> num2:
                    sign=1
            elif len(num1[1:])>len(num2):
                sign=1
            final=sub(num1[1:],num2)
        else:
            if len(num2[1:])==len(num1):
                if num2[1:]> num1:
                    sign=1
            elif len(num2[1:])>len(num1):
                sign=1
            final=sub(num1,num2[1:])
            
        if sign==0:
            return final
        else:
            return '-'+final
    if num1[0]=='-':
        num1=num1[1:]
    if num2[0]=='-':
        num2=num2[1:]
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
    if sign==1:
        return '-'+ans[1:]
    else:
        if ans.lstrip('0')=="":
            return '0'
        else:
            return ans.lstrip('0')
def multiply(num1,num2):
    sign=0
    if (num1[0]=='-' and num2[0]!='-') or (num2[0]=='-' and num1[0]!='-'):
        sign=1
    if (num1[0]=='-'):
        num1=num1[1:]
    if (num2[0]=='-'):
        num2=num2[1:]
    if num1=='0' or num2=='0':
        return "0"
    carry=0
    zero=0
    send="0"
    result=0
    Summation=0
    for i in range(len(num1)-1,-1,-1):
        Ttemp=""
        for j in range(len(num2)-1,-1,-1):
            result=str((int(num1[i])*int(num2[j]))+carry)
            if (len(result))!=2:
                result="0"+result
            if j!=0:
                carry=int(result[0])
                Ttemp=result[1]+Ttemp
            else:
                carry=0
                Ttemp=result+Ttemp
        Ttemp=Ttemp+zero*"0"
        zero+=1
        if(len(send)<len(Ttemp)):
           send=(len(Ttemp)-len(send))*"0" + send
        Summation=Tsum(Ttemp,send)
        send=Summation
    if sign ==1:
        return '-'+Summation
    else:
        return Summation.lstrip('0')
def division(num1,num2):
    remainder=0
    ans=""
    curr=num1[0]
    index=0
    temp=0
    m=''
    indicator=False
    try:
        while index<len(num1):
            if ((int(curr)%int(num2))!=0) and (int(curr)<int(num2)):
                if (index+1)<len(num1):
                    indicator=True
                    while (int(curr) < int(num2))==True:
                        curr= curr + num1[index+1:index+2]
                        index+=1
            temp=str(int(curr)//int(num2))
            if indicator:
                ans=ans+'0'+str(temp)
            else:
                ans=ans+str(temp)
            #print(ans)
            indicator=False
            m=multiply(num2,temp)
            r=int(sub(curr,m))
            if r!=0:
                if (index+1)<len(num1):
                    index+=1
                    curr=str(r)+num1[index]
                else:
                    remainder=r
                    break
            else:
                if (index+1)<len(num1):
                    index+=1
                    curr=num1[index]
                else:
                    break
        if ans.lstrip('0')=="":
            return '0',remainder
        else:
            return ans.lstrip('0'),remainder
    except ZeroDivisionError:
        return 'undefined'
num1=input()
num2=input()
print(division(num1,num2))
