import random

x=True
while x:
    try:
        n=int(input("Enter the size of matrix:"))

        for a in range(n):
            for b in range(n):        
                #print("{0}".format(m), end ==" ")
                print(random.randint(0,1), end=" ")#end=" " means end with space
            print("\n")#print next line
        #extras
        boolean=True
        while boolean:
            try_again=input("Would you like to try again?(yes/no)")
            if try_again=="yes":
                boolean=False
            elif try_again=="no":
                boolean=False
                x=False
                print("Bye!")
            else:
                print("invalid option")
    except ValueError:
        print("Please enter an integer!")
