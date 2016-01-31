##q3_find_gcd.py

def gcd(m,n):
    i=n
    x=True
    while x:
        if n%i==0 and m%i==0:
            print("The GCD of {0} and {1} is {2}.".format(m,n,i))
            x=False
        else:
            i-=1

gcd(24, 16)
gcd(255, 25)
