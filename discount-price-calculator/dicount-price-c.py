'''Discount Price Calculator

Shopping during the sales can sometimes be very confusing.
With discounted prices at 10%, 20%, 50% or even 70%!

For this challenge you are going to write a Python script
that prompts the user to enter a price in pounds
(or in your own currency) (e.g. £90) and a discount rate 
to apply (e.g. 20%).

Your program will then calculate and display the discounted price.'''

# price to enter
price = float(input("Enter the price of your item in € :"))
# discount_rate to enter
discount_rate = int(input("Enter your discount rate as number: "))
#calculation of discounted price
discount = price * discount_rate / 100
discounted_price = price - discount
#display of price before and after discount
print(f"Price before discount = {price} €")
print(f"Discount Rate = {discount_rate} %")
print(f"Discount = {discount} €")
print(f"Price after Discount = {discounted_price} €")


