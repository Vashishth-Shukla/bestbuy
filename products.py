class Product:
    """
    The Product class represents a product in a store, including its name, price, and quantity.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a new Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.

        Raises:
            ValueError: If the name is empty, or if price or quantity are negative.
        """
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        """
        Returns the current quantity of the product.

        Returns:
            float: The current quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Sets the quantity of the product.

        Args:
            quantity (int): The new quantity of the product.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Checks if the product is active.

        Returns:
            bool: True if the product is active, otherwise False.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def show(self) -> str:
        """
        Returns a string representation of the product.

        Returns:
            str: A string that represents the product.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product and updates the quantity.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity to buy is less than or equal to 0 or if the requested quantity is more than available.
            ValueError: If the product is inactive.
        """
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero.")
        if not self.active:
            raise ValueError("Product is not active.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock.")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity


class NonStockedProduct(Product):
    """
    Represents a non-stocked product, such as a digital license.
    """

    def __init__(self, name: str, price: float):
        """
        Initializes a NonStockedProduct instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
        """
        super().__init__(name, price, quantity=0)
        self.activate()  # Non-stocked products are always active

    def set_quantity(self, quantity: int):
        """
        Prevents changing the quantity of a non-stocked product.

        Args:
            quantity (int): The new quantity of the product.

        Raises:
            Exception: Always raises an exception as non-stocked products do not have a quantity.
        """
        raise Exception("Cannot set quantity for non-stocked products.")

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the non-stocked product.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity to buy is less than or equal to 0.
        """
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero.")
        return self.price * quantity

    def show(self) -> str:
        """
        Returns a string representation of the non-stocked product.

        Returns:
            str: A string representing the non-stocked product.
        """
        return f"{self.name}, Price: {self.price} (Non-stocked)"


class LimitedProduct(Product):
    """
    Represents a product with a purchase limit, such as a shipping fee.

    Attributes:
        maximum (int): The maximum quantity that can be purchased in a single order.
    """

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """
        Initializes a LimitedProduct instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product available in the store.
            maximum (int): The maximum quantity that can be purchased in a single order.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the limited product.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity to buy is more than the maximum allowed per order.
        """
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of this product.")
        return super().buy(quantity)

    def show(self) -> str:
        """
        Returns a string representation of the limited product.

        Returns:
            str: A string representing the limited product.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Max per order: {self.maximum}"
