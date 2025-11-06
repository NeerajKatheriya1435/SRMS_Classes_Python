# 1. Reading a File
f = open("data.txt", "r")
content= f.read()
print(content)
f.close()

# 2. Writing to a File
f = open("data.txt", "w")
f.write("Hello, world!")
f.close()

# 3. Appending to a File
f = open("data.txt", "a")
f.write("\nNew line added.")
f.close()

# 4. Read + Write
f = open("data.txt", "r+")
data = f.read()
print(data)
f.write("\nExtra line.")
f.close()

# SOME MORE METHODS IN FILE HANDLING

# 1.readlines() method:
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# 2.writelines() method:
f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()

# Using Loops
f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()

# 3.seek() function:
with open('./file.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)
 
  # Read the next 5 bytes
  data = f.read(5)
  print(data)

# 4.tell() function:
with open('file.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read(10)
 
  # Save the current position
  current_position = f.tell()
 
  # Seek to the saved position
  f.seek(current_position)

# 5.truncate() function:
with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)
 
with open('sample.txt', 'r') as f:
  print(f.read())

