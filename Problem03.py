#The prime factors of 13195 are 5,7,13 and 29.
#What is the largest prime factor of the number 600851475143.

import time;

def timed (n):
    start = time.time();
    result = largestPrimeFactor(int(n));
    end = time.time();
    duration = float(end) - float(start); 
    if result==None:
        print(n,'has no prime factor.');
    else:
        print('Largest prime factor of {} is {}. Execution: {}.'.format(n, result,duration));    
 
def largestPrimeFactor(number):
    if number>1 and primeCheck(number)==False:
        for i in range(int(number**0.5),1,-1):
            if number%i==0 and primeCheck(i):
                number_pair=number/i;
                if number_pair>i and primeCheck(number_pair):
                    return number_pair;
                else:
                    return i;
    elif number>1 and primeCheck(number):
        return number;
    else:
        return None;

    
def primeCheck(number):
    i=2;
    while i<number:
        if (number%i)==0:              
            return False;                
        i=i+1;
    return True;
    


number=input('Number to check: ');
timed(number);
