# Define a list of stock prices
stock=[13,14,2,5,18,1]
# Initialize the minimum price to infinity
minimum=float('inf')
# Initialize the spread to 0
s=0
# Loop through each price in the stock list
for i in stock:
    # If the current price is less than the minimum, update the minimum
    if i<minimum:
        minimum=i
    # If the current price is greater than the minimum and the difference between the current price and the minimum is greater than the spread, update the spread
    if i>minimum and (i-minimum)>s:
        s=i-minimum
# Print the spread
print(s)  