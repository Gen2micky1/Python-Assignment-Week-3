# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate and return the discounted price
        return price * (1 - discount_percent / 100)
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate the final price using the function
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Print the final price
    if discount_percentage >= 20:
        print(f"The final price after a {discount_percentage}% discount is: #{final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for the price and discount percentage.")
