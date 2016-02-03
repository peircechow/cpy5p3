def print_pattern():
    for j in range(m-1,0,-1):
        print(j, end=" "),    
    print("\n")

n=int(input("Enter pattern length here:"))
m=1
if n>=10:
    space=n*2+(n-9)*3
else:    
    space=(n)*2
for i in range(n):
    m+=1
    if i>=9:
        space-=3 #one more space minus off coz 10 has 3 spaces
    else:    
        space-=2

    print(" "*space,end='')
    print_pattern()
##    for j in range(m-1,0,-1):
##        print(j, end=" "),    
##    print("\n")
