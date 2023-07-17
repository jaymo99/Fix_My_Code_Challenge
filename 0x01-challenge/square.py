#!/usr/bin/python3
""" Module defines Square class """


class Square():
    """ Represents a gemetrical square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializes a square """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimiter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation of square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Test Square class """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimiter_of_my_square())

    s = Square(width=10)
    print(s)
    print(s.area_of_my_square())
    print(s.perimiter_of_my_square())

    s = Square(height=10)
    print(s)
    print(s.area_of_my_square())
    print(s.perimiter_of_my_square())

    s = Square(10)
    print(s)
    print(s.area_of_my_square())
    print(s.perimiter_of_my_square())

    s = Square()
    print(s)
    print(s.area_of_my_square())
    print(s.perimiter_of_my_square())
