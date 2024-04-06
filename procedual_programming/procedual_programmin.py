# Define the bill dictionary with items and prices
bill = {
    "item1": 10.00,
    "item2": 15.00,
    "item3": 20.00
}
def subtotal_bill(bill):
    total = 0.00;
    for k, v in bill.items():
        total += v
    return total;
subtotal = subtotal_bill(bill)

def calculate_tax(subtotal):
    tax = round(subtotal * 0.15,2)
    return tax
tax_from_subtotal = calculate_tax(subtotal)

print("Subtotal:", subtotal, 'tax:', tax_from_subtotal)


