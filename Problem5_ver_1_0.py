#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from to 1 to 20? 232792560

import time;

def smallestMultipleCheck(n):
    for j in range(frstNumber,lstNumber):
        if n%j != 0:
            return False;
        continue;
    return True;  
  
                                
frstNumber=int(input('Start number to check: '));
lstNumber=int(input('End number to check: '));
i=frstNumber;

start=time.time();

while smallestMultipleCheck(i)==False:  
    i=i+1;
else:
    #print(searchList);
    print('The smallest number that can be divided by each of the numbers from ', frstNumber,' to ',lstNumber,' without any remainder is ',i,'.');
    end = time.time();
    duration = float(end) - float(start);
    print('It took',duration,'to run the program');
