class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        matrix_list = (self.matrix_string).split("\n")
        rows = matrix_list[index-1].split(" ")
        result = list(map(int, rows))
        return result


    def column(self, index):
        matrix_list = (self.matrix_string).split("\n")
        columns = []
        for row in matrix_list:
            digits = row.split(' ')
            columns.append(digits[index - 1])
        result = list(map(int, columns))
        return result
       
