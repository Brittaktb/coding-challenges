#Iterative Sum for number 5


#Iterative Sum for number a given number = num


num =int(input("Enter a positive number :"))
sum = 0
for i in range(num,0, -1): 
   sum = sum + i
   
print(f"Iterative Sum for {num} = " + str(sum))