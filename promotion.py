from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for promotions.
    """

    @abstractmethod
    def apply_promotion(self, price: float, quantity: int) -> float:
        """
        Applies the promotion to the price based on quantity.

        Args:
            price (float): The original price of the product.
            quantity (int): The quantity of the product being purchased.

        Returns:
            float: The total price after applying the promotion.
        """
        pass


class PercentageDiscountPromotion(Promotion):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_promotion(self, price: float, quantity: int) -> float:
        return price * quantity * (1 - self.percentage / 100)


class SecondItemHalfPricePromotion(Promotion):
    def apply_promotion(self, price: float, quantity: int) -> float:
        if quantity <= 1:
            return price * quantity
        # Full price for the first item, half price for the second
        return price + (price / 2) * (quantity - 1)


class Buy2Get1FreePromotion(Promotion):
    def apply_promotion(self, price: float, quantity: int) -> float:
        # Buy 2, get 1 free means pay for 2 for every 3 items
        free_items = quantity // 3
        items_to_pay = quantity - free_items
        return price * items_to_pay
