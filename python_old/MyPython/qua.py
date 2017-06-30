import math 
def my_quadratic(a,b,c):
   delta=b*b-4*a*c;
   if delta>=0:
       x1=(math.sqrt(delta)-b)/2*a;
       x2=(-math.sqrt(delta)-b)/2*a
       return x1,x2;
   else:
       x1=(math.sqrt(-delta)*1j-b)/2*a;
       x2=(-math.sqrt(-delta)*1j-b)/2*a;
       return x1,x2;


print(my_quadratic(1,4,9));
