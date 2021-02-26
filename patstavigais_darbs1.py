i=0
while i < 100:
    i += 1
    if i%5==0 and i%7==0:
        print("FizzBuzz")
    elif i%7==0:
            print("Buzz")
    elif i%5==0:
            print("Fizz")
    else:
        print(i)