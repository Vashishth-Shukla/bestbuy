from products import Product
from promotion import (
    Buy2Get1FreePromotion,
    PercentageDiscountPromotion,
    SecondItemHalfPricePromotion,
)
from store import Store


def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\nWelcome to Best Buy Store!")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def handle_user_choice(store: Store, choice: str):
    """
    Handles the user's menu choice.

    Args:
        store (Store): The store object containing the inventory of products.
        choice (str): The user's choice from the menu.
    """
    if choice == "1":
        list_products(store)
    elif choice == "2":
        show_total_quantity(store)
    elif choice == "3":
        process_order(store)
    elif choice == "4":
        print("Thank you for visiting Best Buy Store! Goodbye!")
        return False
    else:
        print("Invalid choice. Please select a valid option.")
    return True


def list_products(store: Store):
    """
    Lists all active products in the store.

    Args:
        store (Store): The store object containing the inventory of products.
    """
    products = store.get_all_products()
    if products:
        print("\nAvailable Products:")
        for product in products:
            print(product.show())
    else:
        print("\nNo active products available in the store.")


def show_total_quantity(store: Store):
    """
    Shows the total quantity of all products in the store.

    Args:
        store (Store): The store object containing the inventory of products.
    """
    total_quantity = store.get_total_quantity()
    print(f"\nTotal amount of items in store: {total_quantity}")


def process_order(store: Store):
    """
    Processes an order from the user.

    Args:
        store (Store): The store object containing the inventory of products.
    """
    shopping_list = []
    products = store.get_all_products()

    if not products:
        print("\nNo active products available for ordering.")
        return

    print("\nAvailable Products:")
    for index, product in enumerate(products):
        print(f"{index + 1}. {product.show()}")

    while True:
        try:
            product_index = int(
                input("\nEnter the product number you want to buy (or 0 to finish): ")
            )
            if product_index == 0:
                break

            selected_product = products[product_index - 1]
            quantity = int(input(f"Enter the quantity for {selected_product.name}: "))

            if quantity > 0:
                shopping_list.append((selected_product, quantity))
            else:
                print("Quantity must be greater than zero.")
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")

    if shopping_list:
        try:
            total_price = store.order(shopping_list)
            print(f"\nOrder placed successfully! Total price: {total_price} dollars.")
        except Exception as error:
            print(f"\nFailed to place order: {str(error)}")
    else:
        print("\nNo items were ordered.")


def start(store: Store):
    """
    Starts the user interface for interacting with the store.

    Args:
        store (Store): The store object containing the inventory of products.
    """
    while True:
        display_menu()
        choice = input("Please select an option (1-4): ")
        if not handle_user_choice(store, choice):
            break


def setup_store():
    """
    Sets up the initial inventory with promotions.
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    # Setting promotions
    product_list[0].set_promotion(
        PercentageDiscountPromotion(10)
    )  # 10% off on MacBook Air M2
    product_list[1].set_promotion(
        SecondItemHalfPricePromotion()
    )  # Second item at half price for Bose Earbuds
    product_list[2].set_promotion(
        Buy2Get1FreePromotion()
    )  # Buy 2, get 1 free for Google Pixel 7

    return Store(product_list)


if __name__ == "__main__":
    # Setup initial stock of inventory with promotions
    best_buy = setup_store()

    # Start the user interface
    start(best_buy)
