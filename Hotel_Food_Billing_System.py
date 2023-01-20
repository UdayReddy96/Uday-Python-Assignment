# Hotel Food Billing System

# Menu items and prices
menu = {
    'idly': 20,
    'dosa': 30,
    'chapathi': 25,
    'poori': 35,
    'vada': 20,
    'sambar': 10,
    'curd': 15,
    'coffee': 20,
    'tea': 10,
}

# Function to display menu and take order


def take_order():
    print("Welcome to our hotel! Here is our menu:")
    for item, price in menu.items():
        print(f"{item}: Rs.{price}")

    order = {}
    while True:
        item = input(
            "Enter the item you want to order (Enter 'done' when finished): ")
        if item.lower() == 'done':
            break
        elif item in menu:
            qty = int(input("Enter the quantity: "))
            order[item] = qty
        else:
            print("Invalid item. Please enter a valid item from the menu.")

    return order

# Function to calculate total bill


def calculate_bill(order):
    total = 0
    for item, qty in order.items():
        price = menu[item]
        total += price * qty

    return total

# Main function


def main():
    order = take_order()
    total = calculate_bill(order)
    print(f"Your total bill is Rs.{total}")


if __name__ == '__main__':
    main()
