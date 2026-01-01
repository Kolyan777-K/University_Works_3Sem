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
    """Связь многие-ко-многим"""

    def __init__(self, faculty_id, department_id):
        self.faculty_id = faculty_id
        self.department_id = department_id


# --- Данные (глобальные, чтобы их видели и функции, и тесты при импорте) ---
faculties = [
    Faculty(1, 'Факультет компьютерных наук', 5000000),
    Faculty(2, 'Факультет экономики', 4500000),
    Faculty(3, 'Факультет лингвистики', 4000000),
    Faculty(4, 'Факультет математики', 4800000),
]

departments = [
    Department(1, 'Кафедра математического анализа', 4),
    Department(2, 'Кафедра вычислительной техники', 1),
    Department(3, 'Кафедра иностранных языков', 3),
    Department(4, 'Кафедра физики', 4),
    Department(5, 'Кафедра информационных систем', 1),
    Department(6, 'Кафедра программной инженерии', 1),
]

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


# --- Функции с логикой (для тестирования) ---

def get_one_to_many(facs, deps):
    """Соединение данных один-ко-многим"""
    return [
        (d.name, d.faculty_id, f.name, f.budget)
        for f in facs
        for d in deps
        if d.faculty_id == f.id
    ]


def get_many_to_many(facs, deps, links):
    """Соединение данных многие-ко-многим"""
    many_to_many_temp = [
        (f.name, fd.faculty_id, fd.department_id)
        for f in facs
        for fd in links
        if f.id == fd.faculty_id
    ]

    return [
        (d.name, faculty_name)
        for faculty_name, faculty_id, department_id in many_to_many_temp
        for d in deps if d.id == department_id
    ]


def task_a1(one_to_many):
    """Решение задания А1"""
    return sorted(one_to_many, key=itemgetter(2))


def task_a2(facs, one_to_many):
    """Решение задания А2"""
    res = []
    for f in facs:
        f_deps = list(filter(lambda i: i[2] == f.name, one_to_many))
        if f_deps:
            avg_budget = f.budget / len(f_deps)
            res.append((f.name, avg_budget))

    return sorted(res, key=itemgetter(1), reverse=True)


def task_a3(many_to_many, keyword):
    """Решение задания А3"""
    res = {}
    # Ищем уникальные кафедры
    all_departments = set([d_name for d_name, _ in many_to_many])

    for d_name in all_departments:
        if keyword in d_name.lower():
            d_faculties = list(filter(lambda i: i[0] == d_name, many_to_many))
            if d_faculties:
                faculty_names = [faculty for _, faculty in d_faculties]
                res[d_name] = faculty_names
    return res


# --- Основной запуск программы ---

def main():
    one_to_many = get_one_to_many(faculties, departments)
    many_to_many = get_many_to_many(faculties, departments, faculties_departments)

    print("Задание А1")
    for i in task_a1(one_to_many):
        print(i)

    print("\nЗадание А2")
    for i in task_a2(faculties, one_to_many):
        print(i)

    print("\nЗадание А3")
    print(task_a3(many_to_many, 'кафедра'))


if __name__ == '__main__':
    main()