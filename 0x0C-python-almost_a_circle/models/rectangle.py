#!/usr/bin/python3
from models.base import Base
"""reactangle class that inherist from the base class """


class Rectangle(Base):
    """Rectangle class that inherits from the base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets the value for width """
        return self.__width

    @property
    def height(self):
        """gets the value of height """
        return self.__height

    @property
    def x(self):
        """gets the value of x """
        return self.__x

    @property
    def y(self):
        """gets the value of y """
        return self.__y

    @width.setter
    def width(self, value):
        """setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer ")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
<<<<<<< HEAD

    def area(self):
        """returns the area of a rectangle """
        return self.__width * self.__height

    def display(self):
        i = 0
        while i < self.__height:
            print("#" * self.__width)
            i += 1
=======
    
    def __str__(self):
        """prints out the object """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
>>>>>>> ab1abecd7f4325ff3c127f1eb2dec6a5f0f67626
