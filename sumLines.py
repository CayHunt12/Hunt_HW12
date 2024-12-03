import sys

def read_numbers_from_file(filename):
  try:
    with open(filename, 'r') as file:
      lines = file.readlines()
    numbers = []
    for line in lines:
      for num in line.split():
        numbers.append(int(num))
    return numbers
  except FileNotFoundError:
    print(f"Error: File not found")
    sys.exit(1)
  except ValueError:
    print(f"Error: File contains non-integer values")

def compute_sum(numbers):
  total = 0
  for num in numbers:
    total += num 
  return total

def main():
  if len(sys.argv) != 2:   
    print("Usage: python3 sumLines.py <filename>")
    sys.exit(1)
  
  filename = sys.argv[1]
  numbers = read_numbers_from_file(filename)
  total_sum = compute_sum(numbers)
  num_elements = len(numbers)
  average = total_sum / num_elements if num_elements > 0 else 0

  print(f"{total_sum} {num_elements} {average}")

if __name__ == "__main__":
  main()
