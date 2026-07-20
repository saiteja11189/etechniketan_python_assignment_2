# Read starting number from user
num = int(input("Enter starting number for countdown: "))

# Perform countdown using a while loop and if-else
while num >= 0:
    if num == 0:
        print("Blast!")
    else:
        print(num)
    num -= 1
