import math
def triangle_area(side):
    """Вычисляет площадь равностороннего треугольника по длине его стороны"""
    return (math.sqrt(3) / 4) * side**2
def hexagon_area(side):
    """Вычисляет площадь правильного шестиугольника по длине его стороны"""
    return 6 * triangle_area(side)
side = float(input("Введите длину стороны шестиугольника: "))
print(f"Площадь правильного шестиугольника со стороной {side} равна {hexagon_area(side)}")

