import random

# Input Variables

Number = random.randint(1,101)
max_attempts = 5

# Operations and Validations
for attempt in range(1,max_attempts +1):
    User_input = int(input("Enter a number between 1 and 100"))

    if User_input == Number:
     print(" You're spot on!")
     break

    elif User_input < Number:
        print("Too Low")

    else: 
        print('Too High')   
else: 
   print(f"Out of attempts! The number was {Number}")
