def welcome_user():
  name = input("What is your name? ")
  age = input("What is your age? ")
  print(f"Hello {name}! How can I help you today?")
  options = ["Option 1", "Option 2", "Option 3", "Exit"]
  for i, option in enumerate(options, 1):
    print(f"{i}. {option}")
  choice = int(input("Choose an option: "))
  if choice == 1:
    # execute option 1
    pass
  elif choice == 2:
    # execute option 2
    pass
  elif choice == 3:
    # execute option 3
    pass
  elif choice == 4:
    print("Goodbye! Have a great day.")
  else:
    print("Invalid choice")
welcome_user()
