try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Invalid age!")
        denominator = int(input("Enter the denominator"))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")


#Value Error occurs when no numbers are entered
#ZeroDivisionError occurs when the numbers entered can't be divided

