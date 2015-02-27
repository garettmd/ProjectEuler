working = True
number = 2

while working:
    results = [number % x for x in range(1,11)]
    if results.count(0) != 10:
        number += 1
        print("Number is now ", str(number))
    else:
        working = False
            
print("The smallest number is ", str(number))
