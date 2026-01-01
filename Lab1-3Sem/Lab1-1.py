import sys
import math


class CoefficientReader:
    def __init__(self):
        self.coefficients = []

    def read_coefficient(self, index, prompt):
        while True:
            try:
                if len(sys.argv) > index:
                    coef_str = sys.argv[index]
                    print(f"Коэффициент из командной строки: {coef_str}")
                else:
                    print(prompt)
                    coef_str = input()

                coefficient = float(coef_str)
                self.coefficients.append(coefficient)
                return coefficient
            except ValueError:
                print("Ошибка: введите корректное действительное число")
                if len(sys.argv) > index:
                    print("Некорректный параметр командной строки. Введите значение заново.")


class QuadraticSolver:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.discriminant = self._calculate_discriminant()

    def _calculate_discriminant(self):
        return self.b * self.b - 4 * self.a * self.c

    def solve(self):
        roots = []

        if self.discriminant == 0.0:
            roots.append(-self.b / (2.0 * self.a))
        elif self.discriminant > 0.0:
            sqD = math.sqrt(self.discriminant)
            roots.append((-self.b + sqD) / (2.0 * self.a))
            roots.append((-self.b - sqD) / (2.0 * self.a))

        return roots


class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.roots = []
        self._solve()

    def _solve(self):
        if self.a == 0:
            self._handle_special_case()
            return

        # Решаем относительно y = x^2
        quadratic_solver = QuadraticSolver(self.a, self.b, self.c)
        intermediate_roots = quadratic_solver.solve()

        # Для каждого корня y находим корни x
        for y in intermediate_roots:
            if y > 0:
                root_x = math.sqrt(y)
                self._add_unique_roots([root_x, -root_x])
            elif y == 0:
                self._add_unique_roots([0.0])

    def _handle_special_case(self):
        if self.b == 0:
            if self.c == 0:
                self.roots = ["бесконечно много решений"]
            else:
                self.roots = []
        else:
            # Решаем b*x^2 + c = 0
            if -self.c / self.b >= 0:
                root = math.sqrt(-self.c / self.b)
                self.roots = [root, -root]

    def _add_unique_roots(self, new_roots):
        for root in new_roots:
            if root not in self.roots:
                self.roots.append(root)
        self.roots.sort()

    def get_roots(self):
        return self.roots

    def get_roots_count(self):
        if not self.roots or self.roots[0] == "бесконечно много решений":
            return 0
        return len(self.roots)

    def display_equation(self):
        return f"{self.a}*x^4 + {self.b}*x^2 + {self.c} = 0"

    def display_solution(self):
        if not self.roots:
            return "Действительных корней нет"
        elif self.roots[0] == "бесконечно много решений":
            return "Уравнение имеет бесконечно много решений"
        else:
            result = f"Найдено корней: {len(self.roots)}\n"
            for i, root in enumerate(self.roots, 1):
                result += f"Корень {i}: {root:.6f}\n"
            return result.strip()


class BiquadraticSolverApp:
    def __init__(self):
        self.coefficient_reader = CoefficientReader()
        self.equation = None

    def run(self):
        print("=== РЕШЕНИЕ БИКВАДРАТНОГО УРАВНЕНИЯ (ООП стиль) ===")
        print("Уравнение вида: A*x^4 + B*x^2 + C = 0")

        a = self.coefficient_reader.read_coefficient(1, 'Введите коэффициент А:')
        b = self.coefficient_reader.read_coefficient(2, 'Введите коэффициент B:')
        c = self.coefficient_reader.read_coefficient(3, 'Введите коэффициент C:')

        # Создаем и решаем уравнение
        self.equation = BiquadraticEquation(a, b, c)

        print(f"\nУравнение: {self.equation.display_equation()}")
        print(self.equation.display_solution())


def main_oop():
    app = BiquadraticSolverApp()
    app.run()


if __name__ == "__main__":
    main_oop()