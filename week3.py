#  calculate the final price after applying a discount
def calculate_discount(price, discount_percent):

    if discount_percent >= 20:

        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
       
        return price

original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

print(f"The final price after applying the discount is: ${final_price:.2f}" if discount_percent >= 20 else f"No discount applied. The original price is: ${original_price:.2f}")