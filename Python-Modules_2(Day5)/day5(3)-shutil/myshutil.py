import shutil
import os

# Copy a file
# shutil.copy("file.txt", "backup.txt")

# # Copy file with metadata
# shutil.copy2("source.txt", "backup_with_meta.txt")

# # Move a file
# shutil.move("backup.txt", "folder1/backup.txt")

# # Delete a directory
shutil.rmtree("folder1")

# # Create a ZIP archive of a folder
# shutil.make_archive("d1", "zip", "folder1")
# 
# # Extract archive
# shutil.unpack_archive("d1.zip", "restored_folder")

# Get disk usage
usage = shutil.disk_usage("/")
print(f"Total: {usage.total}, Used: {usage.used}, Free: {usage.free}")
