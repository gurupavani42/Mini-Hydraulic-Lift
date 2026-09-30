# Mini-Hydraulic-Lift
# Mini Hydraulic Lift Simulation

height = 0
max_height = 100

while True:
    print("\n--- MINI HYDRAULIC LIFT ---")
    print("1. Raise Lift")
    print("2. Lower Lift")
    print("3. Check Height")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        if height < max_height:
            height += 10
            print("Lift is UP")
            print("Height:", height, "cm")
        else:
            print("Lift reached maximum height!")

    elif choice == "2":
        if height > 0:
            height -= 10
            print("Lift is DOWN")
            print("Height:", height, "cm")
        else:
            print("Lift is at minimum height!")

    elif choice == "3":
        print("Current Height:", height, "cm")

    elif choice == "4":
        print("Lift stopped.")
        break

    else:
        print("Invalid choice!")
