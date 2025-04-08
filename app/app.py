# class Datamatrix:
#     def __init__(self, data, size):
#         self.data = data
#         self.size = size
#
#     def __repr__(self):
#         self.string_to_binary()
#         self.grid_builder()
#
#
#     def string_to_binary(self) -> list[tuple]:
#         list_of_tuples = []
#         for i in self.data:
#             list_of_tuples.append(tuple(format(ord(i), '08b')))
#         return list_of_tuples
#
#     def grid_builder(self) -> list[list]:
#         gird = [[0] * self.size for _ in range(self.size)]
#
#         for i in range(self.size):
#             gird[i][0] = 1
#         gird[-1] = [1] * self.size
#
#         for i in range(0, self.size, 2):
#             gird[0][i] = 1
#             if i + 1 < self.size:
#                 gird[i + 1][-1] = 1
#         return gird
class Datamatrix:
    def __init__(self, data: str, size:int):
        self.data = data
        self.size = size

    def __repr__(self):
        list_of_tuples = self.string_to_binary()

    def __str__(self):
        grid = self.grid_builder()
        return '\n'.join(' '.join(str(cell) for cell in row) for row in grid)

    def string_to_binary(self) -> list[tuple]:
        list_of_tuples = []
        for i in self.data:
            list_of_tuples.append(tuple(format(ord(i), '08b')))
        return list_of_tuples

    def grid_builder(self) -> list[list]:
        grid = [[0] * self.size for _ in range(self.size)]

        for i in range(self.size):
            grid[i][0] = 1
        grid[-1] = [1] * self.size

        for i in range(0, self.size, 2):
            grid[0][i] = 1
            if i + 1 < self.size:
                grid[i + 1][-1] = 1
        return grid
