from typing import List, Tuple


class Store:
    def __init__(self, products: List["Product"]):
        """
        Initializes a new Store instance with a list of products.

        Args:
            products (List[Product]): A list of products to be stored in the store.
        """
        self.products = products

    def add_product(self, product: "Product"):
        """
        Adds a product to the store.

        Args:
            product (Product): The product to add to the store.
        """
        self.products.append(product)

    def remove_product(self, product: "Product"):
        """
        Removes a product from the store.

        Args:
            product (Product): The product to remove from the store.
        """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products in the store.

        Returns:
            int: The total quantity of all products.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List["Product"]:
        """
        Returns a list of all active products in the store.

        Returns:
            List[Product]: A list of active products.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple["Product", int]]) -> float:
        """
        Processes an order for multiple products and returns the total cost.

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of tuples where each tuple contains a product and the quantity to purchase.

        Returns:
            float: The total price of the order.

        Raises:
            Exception: If any product in the shopping list cannot fulfill the order.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


# Example usage:
if __name__ == "__main__":
    from products import Product

    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))
