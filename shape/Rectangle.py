class Rectangle:
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError("Height cannot be negative.")
        else:
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError("Width cannot be negative.")
        else:
            self._width = width

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width={0}, height={1})".format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return False

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)
