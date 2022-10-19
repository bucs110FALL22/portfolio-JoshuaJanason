def multiply(number, num):
  result = 0
  for i in range(number):
    result = result + number
  return result

def exponent(number, num): 
  result = 1
  for i in range(number):
    result = result * number 
  return result

def square(number):
  value = multiply(number, number)
  return value

def main():
  one_res = multiply(2, 2)
  print(one_res)
  two_res = exponent(2, 2)
  print(two_res)
  three_res = square(4)
  print(three_res)

main()