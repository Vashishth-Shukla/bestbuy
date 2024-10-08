from typing import List, Tuple

from products import Product


class Store:
    """
    Manages a collection of products in a store, allowing adding, removing, ordering products, and combining stores.

    Attributes:
        products (List[Product]): A list of products in the store.
    """

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
            int: The total quantity of all products in the store.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List["Product"]:
        """
        Returns a list of all active products in the store.

        Returns:
            List[Product]: A list of all active products in the store.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple["Product", int]]) -> float:
        """
        Processes an order based on a shopping list of products and quantities.

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of tuples where each tuple contains a product and the quantity to order.

        Returns:
            float: The total price of the order.

        Raises:
            Exception: If any product in the shopping list is not available or the requested quantity is more than available.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

    def __contains__(self, product: "Product") -> bool:
        """
        Checks if a product exists in the store.

        Args:
            product (Product): The product to check.

        Returns:
            bool: True if the product exists in the store, otherwise False.
        """
        return product in self.products

    def __add__(self, other: "Store") -> "Store":
        """
        Combines the products from this store with another store.

        Args:
            other (Store): The other store to combine with.

        Returns:
            Store: A new store instance containing products from both stores.
        """
        combined_products = self.products + other.products
        return Store(combined_products)
