import unittest
from unittest.mock import Mock
from main import PaymentAdapter, LegacyPaymentSystem, Order, Customer, ProductFactory, ProductCategory


class TestOrderSystemMocks(unittest.TestCase):

    def test_payment_adapter_with_mock(self):
        mock_legacy_system = Mock(spec=LegacyPaymentSystem)
        mock_legacy_system.process_payment_legacy.return_value = {
            "transaction_id": "TXN_12345",
            "status": "completed",
            "amount_processed": 1000.0,
            "customer": "test@mail.com"
        }

        adapter = PaymentAdapter(mock_legacy_system)
        result = adapter.process_payment(1000.0, "test@mail.com")

        self.assertIn("TXN_12345", result)
        mock_legacy_system.process_payment_legacy.assert_called_once_with(1000.0, "test@mail.com")

    def test_order_processing_with_mock_payment(self):
        customer = Customer("Тест Клиент", "test@mail.com")
        order = Order(customer)

        product = ProductFactory.create_product(ProductCategory.ELECTRONICS, "Телефон", 10000)
        order.add_product(product)

        mock_payment_processor = Mock()
        mock_payment_processor.process_payment.return_value = "Платеж успешно обработан"

        result = order.process_order(mock_payment_processor)

        self.assertTrue(result)
        mock_payment_processor.process_payment.assert_called_once_with(10000, "test@mail.com")


if __name__ == '__main__':
    unittest.main()