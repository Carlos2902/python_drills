# nested loops with time complexity

import time
start_time = time.time()

for x in range(10):
    for y in range(10):
        print(0, end=" ")
    print()

print(round((time.time()-start_time), 3))