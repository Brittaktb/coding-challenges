# Show in a range of 100 numbers, who are divided by 3 =Fizz and for numbers divisible by 5 = Buzz


for i in range (1,101):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")    
    else:
        print(i)
        