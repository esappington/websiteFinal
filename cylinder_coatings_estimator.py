
import math

def get_nonnegative_float_from_user(prompt):
    while True:
        try:
            input_value = float(input(prompt))
            if (input_value < 0):
                print("Only nonnegative values are allowed. Please re-enter the value.")
                continue
            break
        except ValueError:
            print("Please enter a nonnegative numerical value.")
            continue
    return input_value

def perform_calculation():
        # Get information about the cylinder from the user
        radius = get_nonnegative_float_from_user("Enter the cylinder's radius: ")
        height = get_nonnegative_float_from_user("Enter the cylinder's height: ")
        cost = get_nonnegative_float_from_user("Enter the cost per pint: ")
        

        # Calculate the volume of the cylinder
        # dont think this volume is needed
        #volume = math.pi * radius ** 2 * height

        # Calculate the area of the cylinder
        surface_area = (2 * math.pi * radius * height) + (2 * math.pi * radius ** 2)

        number_of_pints = math.ceil(surface_area / 50)
        # Calculate the Cost of the pints needed
        total = cost * math.ceil(number_of_pints)


        # Output the surface area
        print("\nThe cylinder's surface area is", surface_area)

        # Output the number of pints
        print("\nThe number of pints required is", number_of_pints)

        # Output the total cost
        print("\nThe cost total is", "$", round(total, 2),"\n")

        # Output the ending statement to tell the user
     
        print(number_of_pints , "pints are required costing ", "$", round(total, 2))

def main():
        print("This program calculates the surface area of a cylinder.\n")
        while True:
                perform_calculation()
                response = input("Would you like to perform another calculation (y/n)? ")
                if (response == "y"):
                        print("")
                        continue
                else:
                        break
                
main()
