import unittest
from main import *


class TestRK2(unittest.TestCase):
    def setUp(self):
        """Подготовка тестовых данных перед каждым тестом"""
        self.faculties = [
            Faculty(1, 'F1', 100),
            Faculty(2, 'F2', 200),
        ]
        self.departments = [
            Department(1, 'D1-test', 1),
            Department(2, 'D2', 1),
            Department(3, 'D3-test', 2),
        ]
        self.fac_deps = [
            FacultyDepartment(1, 1),
            FacultyDepartment(1, 2),
            FacultyDepartment(2, 3),
        ]

        self.one_to_many = get_one_to_many(self.faculties, self.departments)
        self.many_to_many = get_many_to_many(self.faculties, self.departments, self.fac_deps)

    def test_task_a1(self):
        """Тест А1: Проверка связи один-ко-многим и сортировки"""
        result = task_a1(self.one_to_many)
        # Ожидаем, что D1 привязан к F1, D2 к F1, D3 к F2
        # И сортировка по имени факультета (F1, F1, F2)
        self.assertEqual(result[0][2], 'F1')
        self.assertEqual(result[2][2], 'F2')
        self.assertEqual(len(result), 3)

    def test_task_a2(self):
        """Тест А2: Проверка расчета среднего бюджета"""
        # У F1 две кафедры (D1, D2), бюджет 100. Среднее = 50.
        # У F2 одна кафедра (D3), бюджет 200. Среднее = 200.
        # Сортировка по убыванию: сначала F2, потом F1.
        result = task_a2(self.faculties, self.one_to_many)

        self.assertEqual(result[0][0], 'F2')
        self.assertEqual(result[0][1], 200.0)

        self.assertEqual(result[1][0], 'F1')
        self.assertEqual(result[1][1], 50.0)

    def test_task_a3(self):
        """Тест А3: Поиск кафедр по названию"""
        # Ищем кафедры, где есть 'test'
        result = task_a3(self.many_to_many, 'test')

        # Должны найтись D1-test и D3-test
        self.assertIn('D1-test', result)
        self.assertIn('D3-test', result)
        self.assertNotIn('D2', result)


if __name__ == '__main__':
    unittest.main()