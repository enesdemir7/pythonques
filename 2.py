#Soru 2.

def sum(number):
  previous_fib_number = 0
  current_fib_number = 1
  sumof_fib_numbers = 0
  while current_fib_number < number:
    if current_fib_number % 2 == 0:
      sumof_fib_numbers += current_fib_number
    next_fib_number = previous_fib_number + current_fib_number
    previous_fib_number = current_fib_number
    current_fib_number = next_fib_number
  return sumof_fib_numbers

# Test the function with a limit of 4 million
print(sum(4000000))
