import unittest
from main import ProductFactory, ProductCategory, ElectronicsProduct, Order, Customer


class TestOrderSystemTDD(unittest.TestCase):

    def test_product_factory_creates_correct_type(self):
        electronics = ProductFactory.create_product(
            ProductCategory.ELECTRONICS, "Смартфон", 30000
        )
        self.assertIsInstance(electronics, ElectronicsProduct)

    def test_product_discount_calculation(self):
        clothing = ProductFactory.create_product(
            ProductCategory.CLOTHING, "Джинсы", 2000
        )
        discounted_price = clothing.calculate_discount()
        self.assertEqual(discounted_price, 1600)

    def test_order_total_amount(self):
        customer = Customer("Тест Клиент", "test@mail.com")
        order = Order(customer)

        product1 = ProductFactory.create_product(ProductCategory.ELECTRONICS, "Планшет", 25000)
        product2 = ProductFactory.create_product(ProductCategory.BOOKS, "Книга", 500)

        order.add_product(product1)
        order.add_product(product2)

        self.assertEqual(order.total_amount, 25500)

    def test_order_auto_increment_id(self):
        customer = Customer("Тест Клиент", "test@mail.com")
        order1 = Order(customer)
        order2 = Order(customer)

        self.assertEqual(order1.order_id + 1, order2.order_id)


if __name__ == '__main__':
    unittest.main()