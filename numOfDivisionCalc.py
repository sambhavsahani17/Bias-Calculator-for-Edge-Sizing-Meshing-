import math

#Input Patameters
min_req = 1E-6                  #first cell height
max_req = 5e-5                  #last Cell  Height
length = 3.6818e-3              #length along which division is done

#Calculation
bias = max_req / min_req
lc = 1
num_div = 2

while True:
  factor = 10**(math.log(bias, 10) / (num_div-1))
  sum_factor = ((factor**num_div)-1) / (factor-1)
  least = length / sum_factor
  if least <= min_req:
    break;
  num_div = num_div + lc

print('******************************************************')
print ('Desired First Cell:', min_req)
print('Desired Last cell:', max_req)
print('******************************************************')

print('Input Parameters')
print('No of Divisons:', num_div)
print('Bias:', bias, 1 / bias)
print('******************************************************')

actual = length / (((factor)**(num_div) - 1) / (factor - 1))
  
print('Actual first cell:', actual)
print('Actual Last cell height:', actual * bias)
print('******************************************************')

print('Growth Factor:', factor)
print('******************************************************')

