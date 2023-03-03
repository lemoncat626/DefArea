from classes import Rectangle, Square, Circle

#создадим 2 прямоугольника
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

#вывод площади прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

#квадраты
square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

#круги
cirle_1 = Circle(3)
cirle_2 = Circle(8)

print(cirle_1.get_area_circle(),
      cirle_2.get_area_circle())


#перенос объектов в единую коллекцию
figures = [rect_1, rect_2, square_1, square_2, cirle_1, cirle_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_area_circle())