from products import Product
from store import Store


def start(store: Store):
    """
    Starts the user interface for interacting with the store.

    Args:
        store (Store): The store object containing the inventory of products.
    """
    while True:
        print("\nWelcome to Best Buy Store!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please select an option (1-4): ")

        if choice == "1":
            # List all active products in the store
            products = store.get_all_products()
            if products:
                print("\nAvailable Products:")
                for product in products:
                    print(product.show())
            else:
                print("\nNo active products available in the store.")

        elif choice == "2":
            # Show the total quantity of all products in the store
            total_quantity = store.get_total_quantity()
            print(f"\nTotal amount of items in store: {total_quantity}")

        elif choice == "3":
            # Make an order
            shopping_list = []
            products = store.get_all_products()

            if not products:
                print("\nNo active products available for ordering.")
                continue

            print("\nAvailable Products:")
            for index, product in enumerate(products):
                print(f"{index + 1}. {product.show()}")

            while True:
                try:
                    product_index = int(
                        input(
                            "\nEnter the product number you want to buy (or 0 to finish): "
                        )
                    )
                    if product_index == 0:
                        break

                    selected_product = products[product_index - 1]
                    quantity = int(
                        input(f"Enter the quantity for {selected_product.name}: ")
                    )

                    if quantity > 0:
                        shopping_list.append((selected_product, quantity))
                    else:
                        print("Quantity must be greater than zero.")
                except (ValueError, IndexError):
                    print("Invalid selection. Please try again.")

            if shopping_list:
                try:
                    total_price = store.order(shopping_list)
                    print(
                        f"\nOrder placed successfully! Total price: {total_price} dollars."
                    )
                except Exception as e:
                    print(f"\nFailed to place order: {str(e)}")
            else:
                print("\nNo items were ordered.")

        elif choice == "4":
            # Quit the program
            print("Thank you for visiting Best Buy Store! Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    # Setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    # Start the user interface
    start(best_buy)
