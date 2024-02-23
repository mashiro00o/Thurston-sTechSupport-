# Calculate factorial of 5
num = 5
if num < 0:
  print("Factorial is not defined for negative numbers")
elif num == 0:
  print(1)
else:
  result = 1
  for i in range(1, num + 1):
    result *= i
  print(result)
