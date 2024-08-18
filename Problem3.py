#The prime factors of 13195 are 5,7,13 and 29.
#What is the largest prime factor of the number 600851475143.

isPrime=False;

def largestPrimeFactor(number):
    factors=[]
    for i in range(2,number):
        if primeCheck(i):
            if number%i==0:
                factors.append(i);
    return factors[-1];
    
    
    
   # largestPrimeNum=2;
    # if number > 1:
        # for i in range(2,number+1):
            # if primeCheck(i)==True:
                # largestPrimeNum=i;                    
    # else:
        # print("No prime number found");

    # print(largestPrimeNum);'''
    
    
def primeCheck(number):
    global isPrime;
    if number > 1:
        for i in range(2,number):
            if (number%i)==0:
                isPrime=False;                
                #print (number, 'is not a prime number.');
                return isPrime;
        else:
            isPrime=True;
            primeNum=number;
            #print (number, 'is a prime number.');
            return isPrime;
            
             
    else:
        isPrime=False;
        print (number, 'is not a prime number.');



number=input('Number to check: ');
number=int(number);
print (largestPrimeFactor(number));