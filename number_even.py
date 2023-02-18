#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 7264
#Print the number of even digits in the variable "var_int".
answer = 0

x1 = var_int % 10
answer += x1 % 2      #   (4 + 1) % 2     answer = answer + (x1 + 1) % 2
var_int //= 10

x2 = var_int % 10
answer += x2 % 2      #   (6 + 1) % 2
var_int //= 10

x3 = var_int % 10
answer += x3 % 2      #   (2 + 1) % 2
var_int //= 10

x4 = var_int % 10
answer += x4 % 2      #   (7 + 1) % 2

print(answer)