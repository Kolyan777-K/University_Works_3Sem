from operator import itemgetter


class Department:
    """Кафедра"""

    def __init__(self, id, name, faculty_id):
        self.id = id
        self.name = name
        self.faculty_id = faculty_id


class Faculty:
    """Факультет"""

    def __init__(self, id, name, budget):
        self.id = id
        self.name = name
        self.budget = budget


class FacultyDepartment:
    """Связь многие-ко-многим между Факультетами и Кафедрами"""

    def __init__(self, faculty_id, department_id):
        self.faculty_id = faculty_id
        self.department_id = department_id


def main():
    # Тестовые данные - Факультеты
    faculties = [
        Faculty(1, 'Факультет компьютерных наук', 5000000),
        Faculty(2, 'Факультет экономики', 4500000),
        Faculty(3, 'Факультет лингвистики', 4000000),
        Faculty(4, 'Факультет математики', 4800000),
    ]

    # Тестовые данные - Кафедры
    departments = [
        Department(1, 'Кафедра математического анализа', 4),
        Department(2, 'Кафедра вычислительной техники', 1),
        Department(3, 'Кафедра иностранных языков', 3),
        Department(4, 'Кафедра физики', 4),
        Department(5, 'Кафедра информационных систем', 1),
        Department(6, 'Кафедра программной инженерии', 1),
    ]

    # Тестовые данные - связи многие-ко-многим
    faculties_departments = [
        FacultyDepartment(1, 2),
        FacultyDepartment(1, 5),
        FacultyDepartment(1, 6),
        FacultyDepartment(2, 1),
        FacultyDepartment(2, 3),
        FacultyDepartment(3, 3),
        FacultyDepartment(4, 1),
        FacultyDepartment(4, 4),
        FacultyDepartment(4, 5),
    ]

    print("=" * 60)
    print("РУБЕЖНЫЙ КОНТРОЛЬ №1")
    print("Вариант 29: Кафедра - Факультет")
    print("=" * 60)

    # Соединение данных один-ко-многим
    one_to_many = [
        (d.name, d.faculty_id, f.name, f.budget)
        for f in faculties
        for d in departments
        if d.faculty_id == f.id
    ]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [
        (f.name, fd.faculty_id, fd.department_id)
        for f in faculties
        for fd in faculties_departments
        if f.id == fd.faculty_id
    ]

    many_to_many = [
        (d.name, faculty_name)
        for faculty_name, faculty_id, department_id in many_to_many_temp
        for d in departments if d.id == department_id
    ]

    print("\nЗАДАНИЕ А1")
    print("Список всех связанных кафедр и факультетов (один-ко-многим),")
    print("отсортированный по факультетам:")
    print("-" * 50)

    res_a1 = sorted(one_to_many, key=itemgetter(2))  # Сортировка по названию факультета
    for dep_name, _, fac_name, budget in res_a1:
        print(f"{fac_name:.<30} {dep_name} (бюджет: {budget:,} руб.)")

    print("\nЗАДАНИЕ А2")
    print("Список факультетов с средним бюджетом на кафедру,")
    print("отсортированный по убыванию среднего бюджета:")
    print("-" * 50)

    res_a2_unsorted = []
    for f in faculties:
        # Находим кафедры факультета
        f_deps = list(filter(lambda i: i[2] == f.name, one_to_many))
        if f_deps:
            # Вычисляем средний бюджет на кафедру
            avg_budget = f.budget / len(f_deps)
            res_a2_unsorted.append((f.name, avg_budget, len(f_deps)))

    # Сортировка по убыванию среднего бюджета
    res_a2 = sorted(res_a2_unsorted, key=itemgetter(1), reverse=True)

    for fac_name, avg_budget, dep_count in res_a2:
        print(f"{fac_name:.<30} {avg_budget:>12,.2f} руб. ({dep_count} кафедр)")

    print("\nЗАДАНИЕ А3")
    print("Список всех кафедр, у которых в названии есть 'кафедра',")
    print("и факультетов, с которыми они связаны:")
    print("-" * 50)

    res_a3 = {}
    for d in departments:
        if 'кафедра' in d.name.lower():
            # Находим факультеты для этой кафедры
            d_faculties = list(filter(lambda i: i[0] == d.name, many_to_many))
            if d_faculties:
                faculty_names = [faculty for _, faculty in d_faculties]
                res_a3[d.name] = faculty_names

    for dep_name, faculty_list in res_a3.items():
        print(f"\n{dep_name}:")
        for faculty in faculty_list:
            print(f"  └── {faculty}")

    print("\n" + "=" * 60)
    print("ВЫПОЛНЕНИЕ ЗАВЕРШЕНО")
    print("=" * 60)


if __name__ == '__main__':
    main()