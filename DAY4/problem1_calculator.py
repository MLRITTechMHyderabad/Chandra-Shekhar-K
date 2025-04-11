def calculator(a, b, operator):
    """
    Performs a calculation based on the given operator.
    
    :param a: First number (int/float)
    :param b: Second number (int/float)
    :param operator: String representing an operation (+, -, *, /, %, **)
    :return: Computed result or error message
    """
    try:
        
        if operator=="+":
            return a + b
        elif operator=="-":
            return a-b
        elif operator=="*":
            return a*b
        elif operator=="/":
            return a/b
        elif operator=="%":
            return a%b
        elif operator=="**":
            return a**b
        else:
            raise ValueError

            #print("operator not in the list")

    
        # TODO: Implement operation handling and raise exceptions for invalid cas # if b=0 goes to divison by zero erro
    except ZeroDivisionError as e  :
        print(e) # TODO: Handle division by zero
    except ValueError as e  :
        print(e) # TODO: Handle invalid numbers
    except TypeError as e :
        print(e) # TODO: Handle non-numeric input
    except Exception as e:
        print(e) # TODO: Handle any unexpected exceptions

# Example Usage:
print(calculator(10, 0, "/"))  # Should return: "Error: Division by zero"
print(calculator(10, "five", "+"))  # Should return: "Error: Invalid input type"
print(calculator(10, 5, "$"))  # Should return: "Error: Unsupported operator"
