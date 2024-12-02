#By listing the first six prime numbers: 2,3,5,7,11 and 13 we can see that the 6th prime is 13.
#What is the 10,001st prime number.
import time;

#Checks if 'number' is a prime number.
def primeCheck(number):
    
    # Check if n is less than 2, as numbers less than 2 are not prime
    if number <= 1:
        return False
        
    # Check divisibility from 2 to the square root of n
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # n is divisible by i, so it's not prime    
    return True  # n is prime if no divisors were found

def primeCounter(n):
    allCount=1;
    primeCount=0
    prime=2
    while primeCount<n:
        if (primeCheck(allCount)==True and allCount>1):
            prime=allCount;
            primeCount=primeCount+1;           
            allCount=allCount+1;
        else:
            allCount=allCount+1;
                
    return prime;
                

num=int(input('The cardinal number of the ordinal prime you would like to find: '));

start=time.time(); 
print('The',num,'th prime number is', primeCounter(num),'.');

end = time.time();
duration = float(end) - float(start);
print('It took',duration,'to run the program');
