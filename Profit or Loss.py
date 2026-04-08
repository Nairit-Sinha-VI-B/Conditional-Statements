# Ask Prices First

Actual_Price = float(input("Enter the Actual price: "))

Selling_Price = float(input("Enter the Selling price: "))

# Check if profit or loss

amount = Selling_Price - Actual_Price

if amount > 0:
    print("Profit of {0}".format(amount))

else:
    print("Loss Only!!!")