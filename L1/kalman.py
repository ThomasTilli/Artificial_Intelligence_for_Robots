from math import *

def gau(mu,sigma2,x):
   return 1/sqrt(2.0*pi*sigma2)*exp(-0.5*(x-mu)**2/sigma2)
  
  
#print gau(10.0,4.0,8.)


def update(mean1, var1, mean2, var2):
   new_mean =1.0/(var1+var2)*(var1*mean2+var2*mean1)
   new_var =1.0/(1.0/var1+1.0/var2)
   return [new_mean, new_var]

print update(10.,8.,13., 2.)


def predict(mean1, var1, mean2, var2):
   new_mean =mean1+mean2
   new_var =var1+var2
   return [new_mean, new_var]

print predict(10., 4., 12., 4.)



measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0
sig = 0.1

for n in range(len(measurements)):
   [mu,sig]=update(mu,sig,measurements[n],measurement_sig)
   print 'update: ',[mu,sig]
   [mu,sig]=predict(mu,sig,motion[n],motion_sig)
   print 'predict: ',[mu,sig]
   
print [mu,sig]   