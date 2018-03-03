class List_Triangles:
    def __init__(self):
        self.list_triangles = []

    def add_triangle9(self, triangle):
        self.list_triangles.append(triangle)

    def sort_all_triangles(self):
        self.list_triangles = sorted(self.list_triangles,
                                     key=lambda x: x.square, reverse=True)
        i = 0
        print('============= Triangles list:==============')
        for triangle in self.list_triangles:
            i += 1
            print('{}. {}'.format(i, triangle))
