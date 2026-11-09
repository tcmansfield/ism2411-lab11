print("exercise 1")
customer = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "tier": "gold",
    "ytd_spend": 12400
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

print("exercise 2")
customer["phone"] = "813-555-1234"

print(customer)
customer["tier"] = "platinum"

print(customer)
del customer["email"]

print(customer)

print(customer.get("email", "Email not found"))

print("exercise 3")

print(customer.get("email", "no email on file"))

# try:
#     print(customer["email"])
# except KeyError as error:
#     print(f"KeyError Caught: {error}")

print("exercise 4")

for key, value in customer.items():
    print(f"Key {key}: Value {value}")

for item in customer:
    print(item)

print("exercise 5")

tier_discounts = {
    "bronze": 0,
    "silver": .05,
    "gold": .10,
    "platinum": .15
}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate * 100:.0f}%")
print(f"Final Price: ${final_price:.2f}")

print("exercise 6")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Alice", "tier": "gold", "ytd_spend": 8750},
    {"name": "Charlie", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discouint = 300 * rate
    print(f"Customer: {record['name']}, Tier: {record['tier']}, Discount: ${discouint:.2f} on $300 purchase")

print("exercise 7")
catalog = {
    "Widget A" : {"price": 9.99, "stock": 150},
    "Gadget C" : {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left in stock!")

print("exercise 8")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]
print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"Region: {region}, Total Sales: ${sales_by_region[region]:.2f}")
