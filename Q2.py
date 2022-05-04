binary_number=[]
num=int(input("enter the decimal number: "))
x=num
while x !=0:
    remind=x%2
    binary_number.append(remind)
    x= x//2
    binary_number.reverse()
    out=""
    for i in binary_number:
        out=out+str(i)
    print(out)
print(binary_number)
    
    
        
