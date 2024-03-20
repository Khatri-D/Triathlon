
# Get input for swimming, cycling, and running times
swimming = input("Enter swimming time (minutes): ")
cycling = input("Enter cycling time (minutes): ")
running = input("Enter running time (minutes): ")

# Convert the input from the user into integer
swimming_time = int(swimming)
cycling_time = int(cycling)
running_time = int(running)

# Calculate total time for the triathlon
total_time = swimming_time + cycling_time + running_time

# Determine the award based on the total time
if total_time <= 100:
    print(f"Your total time is {total_time} minutes, you receive 'Provincial Colours.'")
elif total_time <= 105:
    print(f"Your total time is {total_time} minutes, you receive 'Provincial Half Colours.'")
elif total_time <= 110:
    print(f"Your total time is {total_time} minutes, you receive 'Provincial Scroll.'")
else:
    print(f"Your total time is {total_time} minutes, you receive 'No award.'")


