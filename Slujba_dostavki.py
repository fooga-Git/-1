"""Ввод данных."""
weights_robots = list(map(int, input().split()))
limit_mass = int(input())


def need_plats(mass_robots: list, limit: int):
    """Метод определения минимального количества платформ."""
    mass_robots.sort()
    mass_left: int = 0
    mass_right: int = len(mass_robots) - 1
    result: int = 0
    """Условие выполнения задачи."""
    for i in mass_robots:
        if i > limit:
            print('Вес отдельного робота не может превышать limit.')
            return 'Задача не выполнима.'

    while mass_left <= mass_right:
        if mass_robots[mass_left] + mass_robots[mass_right] <= limit:
            mass_left = mass_left + 1
        mass_right = mass_right - 1
        result = result + 1
        if mass_left == mass_right:
            result = result + 1
            break
    return result


print(need_plats(weights_robots, limit_mass))
