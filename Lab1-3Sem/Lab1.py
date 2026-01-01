import sys
import math


def get_coef_procedural(index, prompt):
    while True:
        try:
            if len(sys.argv) > index:
                coef_str = sys.argv[index]
                print(f"Коэффициент из командной строки: {coef_str}")
            else:
                print(prompt)
                coef_str = input()

            return float(coef_str)
        except ValueError:
            print("Ошибка: введите корректное действительное число")
            if len(sys.argv) > index:
                print("Некорректный параметр командной строки. Введите значение заново.")


def calculate_discriminant(a, b, c):
    return b * b - 4 * a * c


def solve_quadratic(a, b, c):
    roots = []
    D = calculate_discriminant(a, b, c)

    if D == 0.0:
        roots.append(-b / (2.0 * a))
    elif D > 0.0:
        sqD = math.sqrt(D)
        roots.append((-b + sqD) / (2.0 * a))
        roots.append((-b - sqD) / (2.0 * a))

    return roots


def solve_biquadratic_procedural(a, b, c):
    result = []

    # Особый случай: a = 0
    if a == 0:
        if b == 0:
            if c == 0:
                return ["бесконечно много решений"]
            else:
                return []
        else:
            # Решаем b*x^2 + c = 0
            if -c / b >= 0:
                root = math.sqrt(-c / b)
                result.extend([root, -root])
            return result

    # Решаем относительно y = x^2
    intermediate_roots = solve_quadratic(a, b, c)

    # Для каждого корня y находим корни x
    for y in intermediate_roots:
        if y > 0:
            root_x = math.sqrt(y)
            result.extend([root_x, -root_x])
        elif y == 0:
            result.append(0.0)

    # Удаляем дубликаты и сортируем
    unique_roots = []
    for root in result:
        if root not in unique_roots:
            unique_roots.append(root)

    unique_roots.sort()
    return unique_roots


def display_roots_procedural(roots):
    if not roots:
        print('Действительных корней нет')
    elif roots[0] == "бесконечно много решений":
        print('Уравнение имеет бесконечно много решений')
    else:
        print(f'Найдено корней: {len(roots)}')
        for i, root in enumerate(roots, 1):
            print(f'Корень {i}: {root:.6f}')


def main_procedural():
    print("=== РЕШЕНИЕ БИКВАДРАТНОГО УРАВНЕНИЯ (процедурный стиль) ===")
    print("Уравнение вида: A*x^4 + B*x^2 + C = 0")

    a = get_coef_procedural(1, 'Введите коэффициент А:')
    b = get_coef_procedural(2, 'Введите коэффициент B:')
    c = get_coef_procedural(3, 'Введите коэффициент C:')

    print(f"\nУравнение: {a}*x^4 + {b}*x^2 + {c} = 0")

    roots = solve_biquadratic_procedural(a, b, c)
    display_roots_procedural(roots)


if __name__ == "__main__":
    main_procedural()