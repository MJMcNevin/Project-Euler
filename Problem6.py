#The sum of the squares of the first ten natural numbers is, 1^2+2^+...10^2=385.
#The square of the sum of the first ten natural numbers is, (1+2+...10)^2=55^2=3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import time;

#Finds the sum of the squares of natrual numbers a->z.  
def sumOfSquares(a,z):
    i=0;
    n=0;    
    for x in range(a,z+1):
        i=x**2;
        n=n+i;
    return n;  
    
#Finds the square of the sum of natrual numbers a->z.    
def squareOfSum(a,z):
    n=0;    
    for x in range(a,z+1):
        n=n+x;
        
    n=n**2;
    return n;

frstNumber=int(input('Start number to check: '));
lstNumber=int(input('End number to check: '));
start=time.time(); 
print('The sum of the squares of the natural numbers between ',frstNumber,' and ', lstNumber,' is ',sumOfSquares(frstNumber,lstNumber),'.')
print('The square of the sum of the natural numbers between ',frstNumber,' and ', lstNumber,' is ',squareOfSum(frstNumber,lstNumber),'.')
print('The difference between the sum of the squares of ',frstNumber,' and ', lstNumber,' and the square of the sum is ',squareOfSum(frstNumber,lstNumber)-sumOfSquares(frstNumber,lstNumber),'.')

end = time.time();
duration = float(end) - float(start);
print('It took',duration,'to run the program');
