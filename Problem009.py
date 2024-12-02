#A Pythagorean triplet is a set of three natural numbers, a<b<c, for which, a**2+b**2=c**2. For example 3**2+4**2=25=5**2. There exists exactly one Pythagorean triplet for which a+b+c=1000. Find the product a*b*c.



import time;

def pythagorean_triplet (abc_sum):
    for a in range (1,1000):
        for b in range(a,1000):
            c=((a**2)+(b**2))**0.5;
            if a+b+c==abc_sum:
                return [int(a),int(b),int(c)];
                
triplet=pythagorean_triplet (1000)    
trip_prod=triplet[0]*triplet[1]*triplet[2]
print('The Pythagorean triplet for which a+b+c=1000 is a='+ str(triplet[0])+', b='+str(triplet[1]),'and c='+str(triplet[2])+'. The product of these numbers is '+str(trip_prod));              
