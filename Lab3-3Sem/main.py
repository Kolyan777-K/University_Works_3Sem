import os
import sys

# Добавляем src в путь для импорта
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))


def run_all_tests():
    """Запуск всех тестов"""
    print("=" * 50)
    print("ЗАПУСК ВСЕХ ТЕСТОВ ЛАБОРАТОРНОЙ РАБОТЫ")
    print("=" * 50)

    # Импортируем и запускаем каждый модуль
    from src import field, gen_random, unique, sort, print_result, cm_timer, process_data

    print("\n1. Тестирование field:")
    import src.field

    print("\n2. Тестирование gen_random:")
    import src.gen_random

    print("\n3. Тестирование unique:")
    import src.unique

    print("\n4. Тестирование sort:")
    import src.sort

    print("\n5. Тестирование print_result:")
    import src.print_result

    print("\n6. Тестирование cm_timer:")
    import src.cm_timer

    print("\n7. Тестирование process_data:")
    import src.process_data


if __name__ == "__main__":
    run_all_tests()