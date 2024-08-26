class Product:
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
        elif quantity == 0:
            self.quantity == 0
            self.deactivate()
        else:
            self.quantity = quantity
            self.activate()

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
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Active Status: {self.active}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product and updates the quantity.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity to buy is less than or equal to 0.
            Exception: If the product is inactive or if the requested quantity is more than available.
        """
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero.")
        if not self.active:
            raise Exception("Product is not active.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())


if __name__ == "__main__":
    main()
