import time

# Current time in seconds
print("Epoch time:", time.time())

# Delay for 2 seconds
print("Wait for 2 seconds...")
time.sleep(2)
print("Resumed!")

# Local time
local = time.localtime()
print("Local time tuple:", local)
print("Formatted:", time.strftime("%Y-%m-%d %H:%M:%S", local))

# Convert string to time
time_str = "2025-07-16 11:00:00"
parsed = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
print("Parsed time tuple:", parsed)

# Readable time from timestamp
print("CTime:", time.ctime())