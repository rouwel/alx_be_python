def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        try:
            result = num/den
            return f"The result is {result}"
            return "Error: Cannot divide be zero."
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."






    
        

