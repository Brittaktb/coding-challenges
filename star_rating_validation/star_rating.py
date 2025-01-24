'''Flowchart to Python Code Star Rating Validation

The aim of this Python challenge is to validate a user input using a range check.
In this program, the user will be asked to enter a star rating by entering a number value between 0 and 5.
This could for instance be used to rate a movie
(5 Stars = Excellent , 0 Star = Disappointing).'''


starRating = int(input("Enter a star rating between 0 and 5 :"))

while (starRating < 0) or (starRating > 5):
    print("Invalid Star Rating - Try again!")
    starRating = int(input("Enter a star rating between 0 and 5 :"))
print("Thank you!")
