from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class ProductCategory(Enum):
    ELECTRONICS = "электроника"
    CLOTHING = "одежда"
    BOOKS = "книги"


class Product(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def calculate_discount(self) -> float:
        pass


class ElectronicsProduct(Product):
    def get_description(self) -> str:
        return f"Электроника: {self.name} - {self.price} руб."

    def calculate_discount(self) -> float:
        return self.price * 0.9


class ClothingProduct(Product):
    def get_description(self) -> str:
        return f"Одежда: {self.name} - {self.price} руб."

    def calculate_discount(self) -> float:
        return self.price * 0.8


class BooksProduct(Product):
    def get_description(self) -> str:
        return f"Книги: {self.name} - {self.price} руб."

    def calculate_discount(self) -> float:
        return self.price * 0.85

#Порождающий патерн(Фабричный метод)
class ProductFactory:
    @staticmethod
    def create_product(category: ProductCategory, name: str, price: float) -> Product:
        if category == ProductCategory.ELECTRONICS:
            return ElectronicsProduct(name, price)
        elif category == ProductCategory.CLOTHING:
            return ClothingProduct(name, price)
        elif category == ProductCategory.BOOKS:
            return BooksProduct(name, price)
        else:
            raise ValueError(f"Неизвестная категория: {category}")

#Структурный патерн(Адаптер)
class LegacyPaymentSystem:
    def process_payment_legacy(self, amount: float, customer_id: str) -> dict:
        return {
            "transaction_id": f"TXN_{customer_id}",
            "status": "completed",
            "amount_processed": amount,
            "customer": customer_id
        }


class IPaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float, customer_email: str) -> str:
        pass


class PaymentAdapter(IPaymentProcessor):
    def __init__(self, legacy_system: LegacyPaymentSystem):
        self.legacy_system = legacy_system

    def process_payment(self, amount: float, customer_email: str) -> str:
        legacy_result = self.legacy_system.process_payment_legacy(amount, customer_email)
        return f"Платеж {legacy_result['transaction_id']}: {legacy_result['status']}"

#Поведенческий патерн(Наблюдатель)
class OrderObserver(ABC):
    @abstractmethod
    def update(self, order_id: int, status: str):
        pass


class Customer(OrderObserver):
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def update(self, order_id: int, status: str):
        print(f"Клиент {self.name} получил уведомление: Заказ #{order_id} - {status}")


class Warehouse(OrderObserver):
    def update(self, order_id: int, status: str):
        if status == "обработан":
            print(f"Склад: начать сборку заказа #{order_id}")


class OrderSubject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: OrderObserver):
        self._observers.append(observer)

    def detach(self, observer: OrderObserver):
        self._observers.remove(observer)

    def notify(self, order_id: int, status: str):
        for observer in self._observers:
            observer.update(order_id, status)


class Order(OrderSubject):
    _order_counter = 0

    def __init__(self, customer: Customer):
        super().__init__()
        Order._order_counter += 1
        self.order_id = Order._order_counter
        self.customer = customer
        self.products = []
        self.status = "создан"
        self.total_amount = 0.0

        self.attach(customer)
        self.attach(Warehouse())

    def add_product(self, product: Product):
        self.products.append(product)
        self.total_amount += product.price
        self.status = "обновлен"
        self.notify(self.order_id, self.status)

    def process_order(self, payment_processor: IPaymentProcessor):
        try:
            payment_result = payment_processor.process_payment(self.total_amount, self.customer.email)
            print(f"Платеж обработан: {payment_result}")

            self.status = "обработан"
            self.notify(self.order_id, self.status)
            return True
        except Exception as e:
            self.status = "ошибка оплаты"
            self.notify(self.order_id, self.status)
            return False

    def get_order_info(self) -> str:
        products_info = "\n".join([f"  - {product.get_description()}" for product in self.products])
        return f"""Заказ #{self.order_id}
Клиент: {self.customer.name}
Статус: {self.status}
Общая сумма: {self.total_amount} руб.
Товары:
{products_info}"""


def main():
    print("=== СИСТЕМА УПРАВЛЕНИЯ ЗАКАЗАМИ ===\n")

    customer = Customer("Иван Петров", "ivan@mail.com")
    order = Order(customer)

    laptop = ProductFactory.create_product(ProductCategory.ELECTRONICS, "Ноутбук", 50000)
    tshirt = ProductFactory.create_product(ProductCategory.CLOTHING, "Футболка", 1500)
    book = ProductFactory.create_product(ProductCategory.BOOKS, "Python Programming", 1200)

    order.add_product(laptop)
    order.add_product(tshirt)
    order.add_product(book)

    legacy_system = LegacyPaymentSystem()
    payment_adapter = PaymentAdapter(legacy_system)

    print("Обработка заказа...")
    order.process_order(payment_adapter)

    print("\n" + "=" * 50)
    print(order.get_order_info())


if __name__ == "__main__":
    main()