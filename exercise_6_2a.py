moin = [3,5,9,6,7,4,1,2]

min = moin[0]

for x in moin[1:]:
  if x < min:
    min = x

print("Minimum = ",min)