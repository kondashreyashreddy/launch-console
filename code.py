name = input("What's your name? ")
print(f"Welcome {name} to Shreyash's Launch Console!")

print("1) About me")
print("2) My goals")
print("3) Exit")
choice = input("Pick 1-3: ")

if choice == "1":
  print("I am Shreyash Reddy Konda, a freshman student at Round Rock High School in Round Rock, Texas.")
elif choice == "2":
  print("My goals are to have a degree in Computer Engineering and to master taekwondo.")
elif choice == "3":
  print("Goodbye!")
  running = False
else:
  print("Please pick 1, 2, or 3.")
