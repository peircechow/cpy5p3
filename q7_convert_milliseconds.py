def convert_ms(n):
    s=n//1000
    hour=0
    minute=0
    if s>=60:
        minute=s//60
        s=s%60
        
        if minute>=60:
            hour=minute//60 #get the quotent
            minute=minute%60
    print("{0}:{1}:{2}".format(hour,minute,s))
n=int(input("Enter ms here:"))    
convert_ms(n)    
