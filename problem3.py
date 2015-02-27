'''
number = 600851475143

while divisor > 1:
    if number % divisor == 0:
        print(divisor)
    else:
        divisor -= 1


def large(number):    
    for x in range(number//2,0,-2):
        for x in range(number):
            if x**2 < number:
                print(x)
            if number % x == 0:
                return x
'''


def large(number):
    count = 2
    while count ** 2 < number:
        while number % count == 0:
            number = number / count
        count += 1
    return number


def main():
    print(large(600851475143))

main()
