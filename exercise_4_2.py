num1 = float(input("Please type any number and press enter: "))
num2 = float(input("Please type any number and press enter: "))
num3 = float(input("Please type any number and press enter: "))

print("Three Number are =",num1,",",num2,"and",num3)

if num1 < num2:
  min_num = num1
else:
  min_num = num2

if num3 < min_num:
  min_num = num3

print("Minimum number is =",min_num)