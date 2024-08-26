import pytest

from products import Product


def test_create_product():
    """
    Test that creating a normal product works.
    """
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.get_quantity() == 100
    assert product.is_active() == True


def test_create_product_invalid_name():
    """
    Test that creating a product with an empty name raises a ValueError.
    """
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)


def test_create_product_negative_price():
    """
    Test that creating a product with a negative price raises a ValueError.
    """
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_quantity_zero_deactivates():
    """
    Test that when a product reaches 0 quantity, it becomes inactive.
    """
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)
    assert product.get_quantity() == 0
    assert not product.is_active()


def test_product_purchase_modifies_quantity():
    """
    Test that product purchase modifies the quantity and returns the correct total price.
    """
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(5)
    assert total_price == 1450 * 5
    assert product.get_quantity() == 95


def test_buying_more_than_available_raises_exception():
    """
    Test that buying a larger quantity than exists raises an Exception.
    """
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        product.buy(150)
