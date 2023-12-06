def menu():
  print("Welcome to the menu!")
  print("1. Option 1")
  print("2. Option 2")
  print("3. Exit")

  user_input = input("Enter your selection: ")

  if user_input == "1":
    # Do something for option 1
    pass
  elif user_input == "2":
    # Do something for option 2
    pass
  elif user_input == "3":
    # Exit the program
    exit()
  else:
    # Invalid input
    print("Invalid input. Please try again.")

while True:
  menu()
  
  
  