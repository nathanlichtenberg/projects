num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

if num1 > num2:
   big = num1
else:
   big = num2

while True:
   if big % num1 == 0 and big % num2 == 0:
       lcm = big
       break
   big += 1

print(lcm)



