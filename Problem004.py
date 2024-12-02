#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009=91x99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def palCheck(p):
    #slice operator
    if str(p)==str(p[::-1]):
        return True;
    else:
        return False;


def largestPalFind():
    largestPal=0;
    for i in range(100,1000):
        for j in range(100,1000):
            n=i*j;
            if palCheck(str(n)) and n>largestPal:
                largestPal=n;
    return largestPal;
     
print('The largest palindrome made from the product of two 3-digit numbers is:',largestPalFind());
