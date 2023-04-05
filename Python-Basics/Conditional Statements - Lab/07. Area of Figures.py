figure = input()
if figure == "square":
    square_side = float(input())
    area_square = square_side * square_side
    print(f"{area_square:.3f}")
elif figure == "rectangle":
    rectangle_side = float(input())
    rectangle_width = float(input())
    area_rectangle = rectangle_side * rectangle_width
    print(f"{area_rectangle:.3f}")
elif figure == "circle":
    from math import pi
    radius = float(input())
    area_circle = pi * radius * radius
    print(f"{area_circle:.3f}")
elif figure == "triangle":
    side = float(input())
    height = float(input())
    area_triangle = side * height / 2
    print(f"{area_triangle:.3f}")

