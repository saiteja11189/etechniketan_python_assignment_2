stored_password = "secret_password"
attempts_left = 3

# Prompt user for password with max 3 attempts
while attempts_left > 0:
    user_input = input("Enter password: ")
    if user_input == stored_password:
        print("Access granted")
        break
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Wrong password. You have {attempts_left} attempts left.")
        else:
            print("Access denied")
