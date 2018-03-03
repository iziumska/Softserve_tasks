class Triangle:
    def __init__(self, name, first_side, second_side, third_side):
        self.__name = name
        self.__first_side = first_side
        self.__second_side = second_side
        self.__third_side = third_side
        self.square = float()
        self.perimeter = float()

    def calculation_perimeter_triangle(self):
        self.perimeter = self.__first_side + self.__second_side + \
                         self.__third_side
        return self.perimeter

    def calculation_square_triangle(self):
        perimeter = self.perimeter / 2
        self.square = round(((perimeter *
                              (perimeter - self.__first_side) *
                              (perimeter - self.__second_side) *
                              (perimeter - self.__third_side)) ** 0.5), 2)
        return self.square

    def __repr__(self):
        return '{} : {} cm'.format(self.__name, self.square)

    # @staticmethod
    # def sort_all_triangles(all_triangles):
    #     all_triangles = sorted(all_triangles,
    #                            key=lambda x: x.square, reverse=True)
    #     i = 0
    #     print('============= Triangles list:==============')
    #     for triangle in all_triangles:
    #         i += 1
    #         print('{}. {}'.format(i, triangle))
