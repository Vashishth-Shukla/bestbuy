from promotion import Promotion


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
        self.promotion: Promotion = None  # Initialize with no promotion

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

    def get_promotion(self) -> Promotion:
        """
        Returns the current promotion applied to the product.

        Returns:
            Promotion: The promotion applied to the product.
        """
        return self.promotion

    def set_promotion(self, promotion: Promotion):
        """
        Sets the promotion for the product.

        Args:
            promotion (Promotion): The promotion to apply to the product.
        """
        self.promotion = promotion

    def __str__(self) -> str:
        """
        Returns a string representation of the product, including promotion details if any.

        Returns:
            str: A string that represents the product.
        """
        promotion_info = ""
        if self.promotion:
            promotion_info = f" (Promotion: {self.promotion.__class__.__name__})"
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}{promotion_info}"

    def __gt__(self, other: "Product") -> bool:
        """
        Compares the price of this product with another product.

        Args:
            other (Product): The other product to compare.

        Returns:
            bool: True if this product is more expensive than the other product, otherwise False.
        """
        return self.price > other.price

    def __lt__(self, other: "Product") -> bool:
        """
        Compares the price of this product with another product.

        Args:
            other (Product): The other product to compare.

        Returns:
            bool: True if this product is less expensive than the other product, otherwise False.
        """
        return self.price < other.price

    def __eq__(self, other: "Product") -> bool:
        """
        Checks if this product is equal to another product based on name and price.

        Args:
            other (Product): The other product to compare.

        Returns:
            bool: True if the products have the same name and price, otherwise False.
        """
        return self.name == other.name and self.price == other.price

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product and updates the quantity. Applies promotion if available.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total price of the purchase after applying the promotion.

        Raises:
            ValueError: If the quantity to buy is less than or equal to 0, if the product is inactive,
                        or if the requested quantity is more than available.
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

        total_price = self.price * quantity
        if self.promotion:
            total_price = self.promotion.apply_promotion(self.price, quantity)

        return total_price


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

    def __str__(self) -> str:
        """
        Returns a string representation of the non-stocked product.

        Returns:
            str: A string representing the non-stocked product.
        """
        return f"{self.name}, Price: ${self.price} (Non-stocked)"


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

    def __str__(self) -> str:
        """
        Returns a string representation of the limited product.

        Returns:
            str: A string representing the limited product.
        """
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Max per order: {self.maximum}"
