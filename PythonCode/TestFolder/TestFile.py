
var = 5
print(f"This is the table of {var}")

while True:
    for i in range(1, 11):
        print(f"{var} x {i} = {i * var}")

    choice = input("Do you want to continue for another table (Yes / No): ").strip().lower()

    if(choice == "yes"):
        var = int(input("Enter the value within 1-100: "))
        if( 1 > var) or (var > 100):
            print(f"Your input {var} is out of range 1 - 100")
            break
    else:
        break

print("End of Application")
