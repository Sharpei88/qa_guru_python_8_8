"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1500) is False
    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(500)
        assert product.quantity == 500

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1500)

@pytest.fixture
def cart():
    cart = Cart()
    return cart


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_cart_add_product(self, product, cart):
        """
        Проверка метода add_product на добавление продукта в корзину
        """
        cart.add_product(product, 500)
        assert product in cart.products
        assert cart.products[product] == 500

    def test_cart_add_existing_product(self, product, cart):
        """
        Проверка метода add_product на увеличение количества продукта в корзине
        """
        cart.add_product(product, 500)
        cart.add_product(product, 300)
        assert cart.products[product] == 800


    def test_cart_remove_product(self, product, cart):
        """
        Проверка метода remove_product на удаление продукта из корзины
        """
        cart.add_product(product, 500)
        cart.remove_product(product)
        assert product not in cart.products

    def test_cart_remove_non_existing_product(self, product, cart):
        """
        Проверка метода remove_product на попытку удалить несуществующий продукт
        """
        with pytest.raises(ValueError):
            cart.remove_product(product)

    def test_cart_clear(self, product, cart):
        """
        Проверка метода clear на очистку корзины
        """
        cart.add_product(product, 500)
        cart.clear()
        assert len(cart.products) == 0

    def test_cart_get_total_price(self, product, cart):
        """
        Проверка метода get_total_price на правильное вычисление общей стоимости продуктов в корзине
        """
        cart.add_product(product, 500)
        assert cart.get_total_price() == product.price * 500

    def test_cart_buy(self, product, cart):
        """
        Проверка метода buy на покупку продуктов с достаточным количеством
        """
        cart.add_product(product, 500)
        cart.buy()
        assert product.quantity == 500

    def test_cart_buy_more_than_available(self, product, cart):
        """
        Проверка метода buy на попытку купить больше, чем есть в наличии
        """
        cart.add_product(product, 1500)
        with pytest.raises(ValueError):
            cart.buy()