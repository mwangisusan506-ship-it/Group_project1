try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)

except ZeroDivisionError:
    print("You cannot divide by zero!")

except ValueError:
    print("Please enter a valid number.")

finally:
    print("Program finished.")


# name = input("Enter your name: ")
# print("Hello,", name)
