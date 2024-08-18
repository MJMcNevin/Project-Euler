#The prime factors of 13195 are 5,7,13 and 29.
#What is the largest prime factor of the number 600851475143.

import time;
import math;
isPrime=False;

def timed (n):
    start = time.time();
    result = largestPrimeFactor(int(n));
    end = time.time();
    duration = float(end) - float(start);
    print('Largest prime factor of {} is {}. Execution: {} seconds'.format(n, result, duration));

def largestPrimeFactor(number):
    #number=int(number);
    factors=[]
    for i in range(2,int(math.sqrt(number))):
        if primeCheck(i):
            if number%i==0:
                factors.append(i);
    return factors[-1];
    
    
    
  
    
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
timed(number);
