import math

num = int(input("enter a number :"))

if num == 2:
    print(num,' is a prime number')
else:
    if num % 2 == 0:
        print(num,' is not a prime number')
    else:
        isPrime = True
        for i in range(3,round(math.sqrt(num)),2):
            if num % i == 0:
                print(num,'is not a prime number')
                isPrime = False
            break
        if isPrime:
            print(num,' is a prime nuumber')
