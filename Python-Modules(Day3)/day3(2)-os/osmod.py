import os

# 1. os.getcwd()  => Get Current Working Directory
print(os.getcwd())

# 2. os.mkdir() => Create a New Directory
os.mkdir("new_folder")

# 3. os.makedirs() => Create Directory with Subfolders
os.makedirs("parent/child/grandchild")

# 4. os.chdir() => Change Directory
os.chdir("C:/Users/pc/Documents")
print(os.getcwd())

# 5. os.listdir() => List Files and Folders in Directory
files = os.listdir()
print(files)

# 6. os.rename() => Rename File or Folder
os.rename("old_name.txt", "new_name.txt")

# 8. os.rmdir() => Remove an Empty Folder
os.rmdir("empty_folder")
