class Envelope:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def __eq__(self, other):
        return (self.__width == other.__width and
                self.__height == other.__height) or \
               (self.__width == other.__height and
                self.__height == other.__width)

    def __gt__(self, other):
        return (self.__width > other.__width and
                self.__height > other.__height) or \
               (self.__width > other.__height and
                self.__height > other.__width)

    def __lt__(self, other):
        return (self.__width < other.__width and
                self.__height < other.__height) or \
               (self.__width < other.__height and
                self.__height < other.__width)
