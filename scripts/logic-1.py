# Setting the variable user to true.
user = True
# Setting the variable ops_manager to true.
ops_manager = True
# Setting the variable line_manager to false.
line_manager = False
# A variable that is set to true.
hr_officer = True
# A variable that is set to true.
Coo = True
# Representing 1 week.
time = True   


# This is a nested if statement. It is a if statement within a if statement.
if user:
    if time:
        print("Managers deciding")
        if ops_manager and line_manager:
            print("Request denied")
        elif (ops_manager == True and line_manager) or (ops_manager and line_manager == True):
            print("Hr officer to decide")
            if hr_officer:
                print("Request denied")
            else:
                print("request granted")
        else:
            print("Error in the system")
    else: 
        print("Taking it to the COO")
        if Coo:
            print("Request granted")
        else:
            print("Request denied")
else:
    print("Um you do not want to leave")