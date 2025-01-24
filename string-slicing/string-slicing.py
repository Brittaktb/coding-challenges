# write a username with special criteria

'''
Write a username with special criteria and check the criteria as follows:
1) If the username is less than 6 characters long the program
    should ask the user to enter a valid username. 
2) If the username does not contain the character “_” 
    it should also ask the user to enter a valid username.
3) If the username is valid, the program should decide if the user
    is a member of staff or a student.
4) If they are a student the programme should find out their year group.
5) The program should also display the initial of the student as well as
    their lastname. Finally the program should display whether the user is a Student, a Teacher or an Admin member of staff.
'''



print("\n")
print("Consider the right format of user name : ")
print("\n")
print("1) Year Group: Use two digits (e.g., '07' for year 7 or '00' for staff members)")
print("2) 1 character for their initial (first letter of their firstname)")
print("3) The users lastname")
print("4) 1A 2-digit code: '_S' for students, '_T' for teachers, '_A' for admin staff.")
print("\n")


year_group = ["00","01","02","03", "04","05","06","07","08","09","10","11","12"]

x = False

while x == False:
    username = input("Enter a valid username : ")
    if len(username)<6:
       print("Your username is incorrect: try again: !")
    elif "_" not in username:
        print("Your username doesn't show '_': try again: !")
    elif (username[:2] not in year_group):
        print("Your username doesn't show the right year group': try again: !")
    elif not username.endswith(("_A","_T","_S")):
        print("Your username doesn't show in the end a 2 digit-code _S,_T or _A!")
    else:
        print("\nCongrats! Your user name is given correct!!!!")
        x = True
        
  
year_group = username[:2]
if year_group == "00":
    print(f"Your Year_group identifies you as 'Staff_Member'.")
else:
     print(f"Your Year_group identifies you as 'Student'.")

print(f"Initial of First name: {username[2]}\n")
print(f"Lastname:", username[3:-2], "\n")

if username[-2:] == "_T":
    print("You are a TEACHER\n")
elif username[-2:] == "_S":
    print("You are a STUDENT\n")
else:
    print("You are an ADMIN\n")

    
    



