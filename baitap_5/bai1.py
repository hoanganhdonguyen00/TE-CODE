# def num ():  
#     while true: 
#         number = int(input("hãy nhập số: "))
#         if number == (""):
#             break
# num()    

#for l in range(len(l)):
l = [55,74,10,25]
def x (l):
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[i] > l[j]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
    #return(l)
x(l)            
print((l))