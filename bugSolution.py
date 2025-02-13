def function_with_uncommon_error(a, b):
    try:
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("Operands must be numeric")
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        result = a / b
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

# Example usage:
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero, None
print(function_with_uncommon_error(10, "2"))  # Output: Error: Operands must be numeric, None
print(function_with_uncommon_error("10",2)) # Output: Error: Operands must be numeric, None