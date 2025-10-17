def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        if den == 0:
            return "Error: Cannot divide be zero."
        
        result = num/den
        return f"The result is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."






    
        

