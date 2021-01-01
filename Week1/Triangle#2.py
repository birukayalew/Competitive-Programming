#Christmas triangle
row=eval(input())
for i in range(row):
    print(((row-i)-1)*" " + ((2*i)+1)*'*')
