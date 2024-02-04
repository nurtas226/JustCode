import time

star_time = time.time()

print("Pause time...")
print(time.sleep(2))
print("Done!")

end_time = time.time()
print(f"Program was working {int(end_time - star_time)} seconds.")