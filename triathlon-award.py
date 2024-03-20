# Get input for swimming, cycling, and running times
swimming = input("Enter swimming time (minutes): ")  # Prompt the user to input swimming time
cycling = input("Enter cycling time (minutes): ")    # Prompt the user to input cycling time
running = input("Enter running time (minutes): ")    # Prompt the user to input running time

# Convert the input from the user into integer
swimming_time = int(swimming)    # Convert swimming time input to an integer
cycling_time = int(cycling)      # Convert cycling time input to an integer
running_time = int(running)      # Convert running time input to an integer

# Calculate total time for the triathlon
total_time = swimming_time + cycling_time + running_time  # Add the three times to get the total time

# Determine the award based on the total time
if total_time <= 100:
    print(f"Your total time is {total_time} minutes, you receive 'Provincial Colours.'")  # Award for total time <= 100 minutes
elif total_time <= 105:
    print(f"Your total time is {total_time} minutes, you receive 'Provincial Half Colours.'")  # Award for total time <= 105 minutes
elif total_time <= 110:
    print(f"Your total time is {total_time} minutes, you receive 'Provincial Scroll.'")  # Award for total time <= 110 minutes
else:
    print(f"Your total time is {total_time} minutes, you receive 'No award.'")  # No award for total time > 110 minutes
