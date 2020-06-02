print("Welcome to the grade Calculator")
math = int(input("Please enter your maths mark: "))
chem = int(input("Please enter your chemistry mark: "))
phys = int(input("Please enter your physics mark: "))

total_mark = math + chem + phys
percentage = total_mark/3
print(percentage)
print("Your Percentage score is: "+str(percentage)+"%")

if percentage < 40: 
    print("You Failed.")
elif percentage >= 40 and percentage < 50: 
    print("Your scored a grade of: D")
elif percentage >= 50 and percentage < 60: 
    print("Your scored a grade of: C")
elif percentage >= 60 and percentage < 70: 
    print("Your scored a grade of: B")
elif percentage >= 70: 
    print("Your scored a grade of: A")
else:
    print("something went wrong")

