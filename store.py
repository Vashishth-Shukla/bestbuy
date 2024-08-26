from typing import List, Tuple


class Store:
    """
    The Store class manages a collection of products, allowing the user to
    add, remove, and order products.
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
            shopping_list (List[Tuple[Product, int]]): A list of tuples where each tuple
                                                       contains a product and the quantity to order.

        Returns:
            float: The total price of the order.

        Raises:
            Exception: If any product in the shopping list is not available or the requested
                       quantity is more than available.
        """
        total_price = 0.0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price
