#Abbas Rahimi
#M02 Lab-Case Study: If...else and while

print(" Welcome to the Ivytech student qualification")
print("Enter ZZZ as the last name to quit")

while True:
    last_name = input("Enter the student last name")
    if last_name == 'zzz':
        print("quitting the app")
        break    

    first_name = input("Enter the student first name")
    GPA = float(input("Enter the student GPA"))

    if GPA >= 3.5:
        print(f"{first_name} {last_name} has made the dean list")
    
    elif GPA >= 3.25: 
        print(f"{first_name} {last_name} has made the honor roll")

    else:
        print(f"{first_name} {last_name} does not qualify for any recognition")

