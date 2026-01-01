def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        field_name = args[0]
        for item in items:
            if field_name in item and item[field_name] is not None:
                yield item[field_name]
    else:
        for item in items:
            result = {}
            for field_name in args:
                if field_name in item and item[field_name] is not None:
                    result[field_name] = item[field_name]
            if result:
                yield result


if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'title': None, 'price': 3000},
        {'price': 2500}
    ]

    print("Тест field:")
    print("Один аргумент:", list(field(goods, 'title')))
    print("Несколько аргументов:", list(field(goods, 'title', 'price')))