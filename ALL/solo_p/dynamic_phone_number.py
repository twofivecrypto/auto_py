# This function takes an input phone number and formats it
def format_phone_number(input_number):
    input_number = "".join(filter(str.isdigit, input_number))  # Remove non-numeric characters

    formatted_number = ""  # Create an empty string to store the formatted number
    
    # Check if the input number has at least one digit
    if len(input_number) > 0:
        # Add the first three digits surrounded by parentheses
        formatted_number += "(" + input_number[:3] + ")"
        
        # Check if the input number has more than three digits
        if len(input_number) > 3:
            # Add a space and the next three digits
            formatted_number += " " + input_number[3:6]
            
            # Check if the input number has more than six digits
            if len(input_number) > 6:
                # Add a hyphen and the last four digits
                formatted_number += "-" + input_number[6:10]
    
    # Return the formatted phone number
    return formatted_number


# Test Cases
test_cases = ["1234567890", "123456", "123456789012345", "555-123-4567", "abc123def456"]

# Iterate over the test cases
for number in test_cases:
    # Call the format_phone_number function and store the result in 'formatted'
    formatted = format_phone_number(number)
    
    # Print the original input number and its corresponding formatted number
    print(f"Input: {number}\nFormatted: {formatted}\n")
