
'''
#Factorial!
We are now going to train our AI:Bot to calculate a factorial 
of a number! Your program will ask for the user to enter a positive integer value and return its factorial value as follows:
''' 

num =int(input("Enter a positive number :"))
sum = 1
for i in range(num,0, -1): 
   sum = sum * i
   #print(f"!{num} = {i} *")
   
print(f"{num}! = 5 * 4 * 3 * 2 * 1 \n{num}! = {sum}")
