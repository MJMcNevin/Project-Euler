#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below the provided parameter value number.
def multiplesOf3Or5(number):
    total=0
    i=0
    while i<number:
        if i%3==0 or i%5==0:
            total=total+i;
    
            #print(total);
        i=i+1;
    print (total);

number=input('Number to check: ');
multiplesOf3Or5(int(number));