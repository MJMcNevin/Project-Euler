#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from to 1 to 20? 232792560

import time;

def smallestMultipleCheck(n):
    for j in primeFactors:
        if n%j != 0:
            return False;
        continue;
    return True;  

def buildSearchList(a, z):
    for j in range(a, z+1):
        primeFactors.append(j);

frstNumber=int(input('Start number to check: '));
lstNumber=int(input('End number to check: '));
i=lstNumber;
primeFactors=[];
count=0

buildSearchList(frstNumber, lstNumber);


start = time.time();
while smallestMultipleCheck(i)==False:  
    i=i+1;
else:
    print(primeFactors);
    print(i);
    end = time.time();
    duration = float(end) - float(start); 
    print(duration);
