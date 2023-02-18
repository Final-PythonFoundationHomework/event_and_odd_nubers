#A four-digit integer is given. Find the sum of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 1659
#Create a variable "sum_odd" and assign it 0.
sum_odd = 0
#Find the sum of the odd digits in the variable "var_int".
x1 = var_int % 10
sum_odd += x1 % 2 *x1     #   (4 + 1) % 2     answer = answer + (x1 + 1) % 2
var_int //= 10

x2 = var_int % 10
sum_odd += x2 % 2 *x2     #   (6 + 1) % 2
var_int //= 10

x3 = var_int % 10
sum_odd += x3 % 2 *x3     #   (2 + 1) % 2
var_int //= 10

x4 = var_int % 10
sum_odd += x4 % 2 *x4     #   (7 + 1) % 2

print(sum_odd)