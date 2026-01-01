import random

def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)


if __name__ == "__main__":
    print("Тест gen_random:", list(gen_random(8, 1, 78)))