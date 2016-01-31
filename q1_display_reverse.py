##q1_display_reverse.py

print("NUMBER REVERSAL")

x=True
while x:
    try:
    
        n=int(input("Enter an integer here:"))
        print(str(n)[::-1])
        
        boolean=True
        while boolean:
            again=input("Would you like to try again (yes/no)?")
            if again=="yes":
                break
                continue
            elif again=="no":        
                boolean=False
                x=False
                print("Thank you and have a nice day!")
            else:
                print("Invalid Input")
##        if try_again()==False:
##            x=False
##            print("Thank you and have a nice day!")

    except ValueError:
        print("Invalid input. Please try again!")
    
        

    
      
