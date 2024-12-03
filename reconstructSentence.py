import sys
import os

def read_file(filename):
    """Reads a file and returns a list of words."""
  if not os.path.exists(filename):
    print(f"Error: File '{filename' not found")
    sys.exit(1)
  with open(filename, 'r') as file:
      content = file.read().strip()  # Remove any leading/trailing whitespace
      words = content.split() 
  if not words:
    print(f"Error: File '{filename}' is empty or contains invalid content.")
    sys.exit(1)
  return words  
def reconstruct_sentence(list1, list2):
  """Reconstruct a sentence by taking words alternately from the end of each
  list."""
  out = []
  while list1 or list2:
    if list1:
      out.append(list1.pop())
    if list2:
      out.append(list2.pop())
  return out

def main()
  if len(sys.argv) != 3
    print("Usage: python3 reconstructSentence.py <input1.txt> <input2.txt>")
    sys.exit(1)
  input1_file = sys.argv[1]
  input2_file = sys.argv[2]

  list1 = read_file(input1_file)
  list2 = read_file(input2_file)

  print(f"list1 is {list1}")
  print(f"list1Length: {len(list1)}")
  print(f"list2 is: {list2}")
  print(f"list2Length: {len(list2)}")

  out = reconstruct_sentence(list1, list2)

  print(f"The list out is: {out}")

  with open("output.txt", "w") as output_file:
    output_file.write(" ".join(out))

  print("Reconstructed sentence has been written to output.txt.")

if __name__ == "__main__":
    main()
    
