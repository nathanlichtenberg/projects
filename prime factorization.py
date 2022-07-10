import time
import math


counter = 0

while counter == 0:
    number = int(input("Your Number: "))
    primefac = []
    startTime = time.time()
    if number == 1:
        print("[1]")
        continue

    elif number == 0:
        print("[0]")
        continue

    elif number < 0:
        print("[no.]")
        continue
            
    else:
        for i in range(2, int(math.sqrt(number))):
            if number % i == 0:
                prime = True
                if prime:
                    primefac.append(i)
                    number //= i

        primefac.append(number)

    print(primefac)
    counter += 1

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))

