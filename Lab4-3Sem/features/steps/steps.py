from behave import given, when, then
from main import ProductFactory, ProductCategory, Order, Customer, PaymentAdapter, LegacyPaymentSystem


@given('клиент с именем "{name}" и email "{email}"')
def step_given_customer(context, name, email):
    context.customer = Customer(name, email)


@given('заказ для этого клиента')
def step_given_order(context):
    context.order = Order(context.customer)
    context.products = []  # Инициализируем здесь


@given('продукт категории "{category}" с названием "{name}" и ценой {price:f}')
def step_given_product(context, category, name, price):
    category_enum = {
        'электроника': ProductCategory.ELECTRONICS,
        'одежда': ProductCategory.CLOTHING,
        'книги': ProductCategory.BOOKS
    }[category]

    product = ProductFactory.create_product(category_enum, name, price)

    # Проверяем и инициализируем products если нужно
    if not hasattr(context, 'products'):
        context.products = []

    context.products.append(product)


@when('пользователь добавляет все продукты в заказ')
def step_when_add_products(context):
    for product in context.products:
        context.order.add_product(product)


@when('обрабатывает заказ через платежную систему')
def step_when_process_order(context):
    legacy_system = LegacyPaymentSystem()
    payment_adapter = PaymentAdapter(legacy_system)
    context.payment_result = context.order.process_order(payment_adapter)


@then('общая сумма заказа должна быть {total_amount:f}')
def step_then_total_amount(context, total_amount):
    assert context.order.total_amount == total_amount, \
        f"Ожидалось {total_amount}, получено {context.order.total_amount}"


@then('статус заказа должен быть "{status}"')
def step_then_order_status(context, status):
    assert context.order.status == status, \
        f"Ожидался статус '{status}', получен '{context.order.status}'"


@then('платеж должен быть успешно обработан')
def step_then_payment_success(context):
    assert context.payment_result == True, "Платеж не был обработан успешно"


@then('заказ должен содержать {count:d} продуктов')
def step_then_product_count(context, count):
    assert len(context.order.products) == count, \
        f"Ожидалось {count} продуктов, получено {len(context.order.products)}"