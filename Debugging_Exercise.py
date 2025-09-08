def calculate_discount(price, discount_rate, product_name=None):

    try:
        price_f = float(price)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid price for'{product_name or '<unknown>'}': {repr(price)}")

    try:
        rate_f = float(discount_rate)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid discount rate for '{product_name or '<unknown>'}': {repr(discount_rate)}")

    # Turns whole numbers into percentages
    if rate_f > 1:
        if 1 < rate_f <= 100:
            rate_f = rate_f / 100.0
        else:
            raise ValueError(f"Invalid discount rate for '{product_name or '<unknown>'}': {rate_f}")

    if price_f < 0:
        raise ValueError(f"Negative price for '{product_name or '<unknown>'}: {price_f}")
    if not (0 <= rate_f <= 1):
        raise ValueError(f"Invalid discount rate for '{product_name or '<unknown>'}': {rate_f}")

    discount_amount = price_f * rate_f
    return round(discount_amount, 2)

def apply_discount(price, discount_amount, product_name=None):
    try:
        price_f = float(price)
        discount_f = float(discount_amount)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid price for '{product_name or '<unknown>'}'")

    if discount_f < 0:
        raise ValueError(f"Negative discount for '{product_name or '<unknown>'}'")

    final_price = price_f - discount_f
    if final_price < 0:
        raise ValueError(f"Discount ({discount_f}) > price ({price_f}) for '{product_name or '<unknown>'}'")

    return round(final_price, 2)

def main():
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05},
    ]

    print("Processing products:\n")
    for product in products:
        name = product.get("name", "<unknown>")
        price = product.get("price")
        discount_rate = product.get("discount_rate")
        try:
            discount_amount = calculate_discount(price, discount_rate, product_name=name)
            final_price = apply_discount(price, discount_amount, product_name=name)
            print(f"Product: {name}")
            print(f"  Original Price: ${float(price):.2f}")
            print(f"  Discount Amount: ${discount_amount:.2f}")
            print(f"  Final Price: ${final_price:.2f}\n")
        except Exception as e:
            print(f"Error processing product '{name}': {e}\n")

if __name__ == '__main__':
    main()
