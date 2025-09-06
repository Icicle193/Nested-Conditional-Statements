medical_cause = input("Did you have a medical cause, Y or N?")
attendance = int(input("What was your attendance?"))

if medical_cause == 'y':
    print("You are allowed")
else:
    if attendance>=75:
        print("Allowed")
    else:
        print("Not allowed")