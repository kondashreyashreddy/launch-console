name = input("What's your name? ")
print(f"Welcome {name} to Shreyash's Launch Console!")

print("1) About Me")
print("2) My Goals")
print("3) 26-27 Coursework @ High School")
print("4) Exit")
choice = input("Pick 1-4: ")

if choice == "1":
  print("I am Shreyash Reddy Konda, a freshman student at Round Rock High School in Round Rock, Texas.")
elif choice == "2":
  print("My goals are to have a degree in Computer Engineering and to master taekwondo.")
elif choice == "3":
  print("My STEM coursework for the 2026-2027 school year at Round Rock High School is AP Computer Science Principles, Honors Algebra II, Honors Biology, and Introduction to Engineering Design.")
elif choice == "4":
  print("Goodbye!")
else:
  print("Please pick 1, 2, 3, or 4.")
