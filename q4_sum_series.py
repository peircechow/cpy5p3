##q4_sum_series.py

##maximum=int(input("Enter max value here:")
##
##while i<=maximum:
##            i=1
##    for i in range(i):
##        result=i/(i+1)+result
##    i=i+1
                     
maximum=int(input("Enter max value here:"))
i=1
result=0

print("{0:<10}{1}".format('i','m(i)'))
while i<=maximum:
    
    result+=(i/(i+1))
    
    print("{0:<10}{1:.4f}".format(i, result))
    i+=1

