# Shipping Cost Calculator

## Input Package Weight and Shipping Rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate Shipping Cost
shipping_cost = weight * rate

## Display the Result
print(f"Shipping Cost: {shipping_cost} USD")
