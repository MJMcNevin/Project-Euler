#The sum of the primes below 10 is 2+3+5+7=17. Find the sum of all the primes below two million.



import time;

def primeCheck(number):    
    # Check if n is less than 2, as numbers less than 2 are not prime
    if number <= 1:
        return False        
    # Check divisibility from 2 to the square root of n
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # numer is divisible by i, so it's not prime    
    return True  # number is prime if no divisors were found


#Builds a list of all prime numbers between 'a' and 'z'.
def build_primes_List(a, z):
    primes=[];
    for i in range (a,z+1):
        if primeCheck(i)==True:
            primes.append(i);
        else:
            continue;
    return primes;
    
#Finds the sum of the numbers in a list.           
def sum_list(n):
    list_sum=0;
    for x in n:
        list_sum=list_sum+x;
    return list_sum;
    
start=time.time();
range_min=int(input('Start number to check: '));
range_max=int(input('Last number to check: '));
build_primes_List(range_min, range_max);
stop=time.time();
runtime=stop-start;
print(len(build_primes_List(range_min, range_max)),'prime numbers were found from,',range_min,'to',range_max);
print('It took,',runtime,'secs to build the list.');
print('The sum of the prime numbers found is',sum_list(build_primes_List(range_min, range_max)));
