#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from to 1 to 20? 232792560

import time;

#Checks if 'number' is a prime number.
def primeCheck(number):
    i=2;
    while i<number:
        if (number%i)==0:              
            return False;                
        i=i+1;
    return True;
    
#Builds a list of all prime numbers between 'a' and 'z'.
def buildPrimeList(a, z):
    for i in range (a,z+1):
        if primeCheck(i)==True and i != 1:
            primeList.append(i);

#Raises each prime number in 'primeList' to the highest power that results in a number less than 'lastNumber'
def calcSmallestMultiple():
    smallestMultiple=1;
    for x in range(len(primeList)): 
        y=1;
        while primeList[x]**y<lstNumber:          
            y=y+1;
        else:
            primeList[x]=primeList[x]**(y-1);
    for i in primeList:        
        smallestMultiple=smallestMultiple*i;        
    return smallestMultiple;
    
     
frstNumber=int(input('Start number to check: '));
lstNumber=int(input('End number to check: '));
start=time.time(); 
i=frstNumber;
primeList=[];


buildPrimeList(frstNumber, lstNumber);
print('The smallest number that can be divided by each of the numbers from ',frstNumber,' to ', lstNumber, ' without any remainder is ',calcSmallestMultiple(),'.')

end = time.time();
duration = float(end) - float(start);
print('It took',duration,'to run the program');
