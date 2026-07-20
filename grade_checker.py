print("Welcome to the grade checker program!")

while True:
    try:
        marks = float(input("Enter your marks (0-100): "))
        
        # Validate marks and determine grade
        if 90 <= marks <= 100:
            grade = "A+"
        elif 80 <= marks < 90:
            grade = "A"
        elif 70 <= marks < 80:
            grade = "B"
        elif 60 <= marks < 70:
            grade = "C"
        elif 50 <= marks < 60:
            grade = "D"
        elif 0 <= marks < 50:
            grade = "Fail"
        else:
            print("Invalid marks! Please enter a value between 0 and 100.")
            continue
            
        print(f"Your grade is {grade}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue
    
    # Check if user wants to check another grade
    choice = input("Do you want to check the grade for another marks?: ").strip().lower()
    if choice != 'yes':
        print("Thank you")
        break
