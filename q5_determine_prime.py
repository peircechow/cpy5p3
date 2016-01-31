i=2
n=2
counter=0
start_function=input("Are you ready to find the first 1000 primes?(yes/no)").lower()
if start_function=="yes":
    x=True
    while x:       
        if n%i==0 and i<n:
            n+=1
            i=2
        elif i<n:
            i+=1
        else:
            print("{0:<6}".format(n), end=" ")
            counter+=1
            n+=1
            i=2
            if counter==1000:
                x=False
            elif counter%10==0:
                print("\n")
else:
    print("Bye!")
        


        
