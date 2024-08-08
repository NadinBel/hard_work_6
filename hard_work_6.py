import math
from tkinter import *
from tkinter import ttk

class Figure:
    sides_count = 0
    filled = True
    def __init__(self, __color, *__sides):
        self.__sides = [*__sides]
        if self.__is_valid_color(*__color):
            self.__color = [*__color]
            return self.__color
        else:
            self.__color = [0] * 3
    @ staticmethod
    def __is_valid_color(r, g, b):
        rgb_list = [r, g, b]
        if all([type(x) is int and 0 <= x <= 255 for x in rgb_list]):
            return True
        else:
            return False
    def __is_valid_sides(self, __sides):
        self.__sides = [*__sides]
        if len(self.__sides) == self.sides_count and all([type(x) is int and 0 < x for x in self.__sides ]):
            return True
        else:
            return False
    def get_color(self):
        return self.__color
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            return self.__color
        else:
            print('Введите целые числа от 0 до 255')
    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = []
            for i in new_sides:
                self.__sides.append(i)
            return (self.__sides)
        else:
            self.__sides = [1] * self.sides_count

    def __len__(self):
        return sum(self.__sides)
    @ staticmethod
    def get_rgb(r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'
    def color_rgb(self):
        if self.filled:
            rgb__color = self.get_rgb(*self.__color)
            return rgb__color
        else:
            return 'white'
class Circle(Figure):
    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides)
        self.sides_count = 1
        self.__radius = len(self) / 2 / math.pi
    def get_square(self):
        squere_circle = math.pi * self.__radius ** 2
        print(squere_circle)
        return squere_circle
class Triangle(Figure):
    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides)
        self.sides_count = 3
        p = len(self) / 2
        self.max_side = max(__sides)
        self.__height = 2 * (p*(p - __sides[0])*(p - __sides[1])*(p - __sides[2]))**0.5 / self.max_side
    def get_square(self):
        squere_triangle = self.max_side * self.__height / 2
        return squere_triangle
class Cube(Figure):
    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides)
        self.sides_count = 12
        self.__sides = [*__sides]
        self.filled = False
        if len(self.__sides) == 1:
            self.__sides = [*self.__sides] * self.sides_count
        else:
            self.__sides = [1] * self.sides_count
    def set_sides(self, *new_sides):
        self.__sides = [*new_sides]
        if len(self.__sides) == 1:
            self.__sides = [*self.__sides] * 12
            return self.__sides
    def get_sides(self):
        return self.__sides
    def get_volume(self):
        cube_volume = self.__sides[0] ** 3
        return cube_volume


circle1 = Circle((255, 255, 255), 10)
circle1.set_color(130, 166, 77)
print(circle1.get_color())
print(circle1.get_sides())
circle1.set_sides(15, 56)
print(circle1.get_sides())
print(len(circle1))
print(circle1.get_square())
triangle1 = Triangle((245, 178, 134), 7, 8, 9)
print(triangle1.get_sides())
triangle1.set_sides(3, 4, 5, 3)
print(triangle1.get_sides())
print(triangle1.get_square())
cube1 = Cube((222, 35, 130), 6)
cube1.set_color(30, 170, 150)
print(cube1.get_sides())
print(cube1.get_color())
cube1.set_sides(5)
print(cube1.get_sides())
print(cube1.get_volume())
class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.master.title("Рисуем фигуры")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_oval(10, 10, 80, 80, outline="black",
            fill=circle1.color_rgb(), width=1)
        points = [50, 180, 150, 100, 250, 180]

        canvas.create_polygon(
            points, outline='black',
            fill=triangle1.color_rgb(), width=1)
        canvas.pack(fill=BOTH, expand=1)
        canvas.create_rectangle(230, 120, 290, 60,
            outline="black", fill=cube1.color_rgb(), width=1)
        points_1 = [230, 60, 260, 40, 320, 40, 290, 60]
        canvas.create_polygon(
            points_1, outline='black',
            fill=cube1.color_rgb(), width=1)
        points_2 = [320, 40, 290, 60, 290, 120, 320, 100]
        canvas.create_polygon(points_2, outline='black', fill=cube1.color_rgb(), width=1)
def main():
    root = Tk()
    ex = Example()
    root.geometry("400x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()