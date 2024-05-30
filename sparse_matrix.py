class SparseMatrix:
    def __init__(self):
        self.data = {}
        self.numRows = 0
        self.numCols = 0

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('rows='):
                    self.numRows = int(line.split('=')[1])
                elif line.startswith('cols='):
                    self.numCols = int(line.split('=')[1])
                else:
                    # Parse the line and add the data to the matrix
                    row, col, value = map(int, line.strip('()\n').split(', '))
                    self.data[(row, col)] = value

    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix to multiply")

        result = SparseMatrix()
        result.numRows = self.numRows
        result.numCols = other.numCols

        for i in range(self.numRows):
            for j in range(other.numCols):
                sum = 0
                for k in range(self.numCols):
                    sum += self.data.get((i, k), 0) * other.data.get((k, j), 0)
                if sum != 0:
                    result.data[(i, j)] = sum

        return result

    def print_matrix(self):
        for key, value in self.data.items():
            print(f'Row: {key[0]}, Column: {key[1]}, Value: {value}')

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(f'rows={self.numRows}\ncols={self.numCols}\n')
            for key, value in self.data.items():
                f.write(f'({key[0]}, {key[1]}, {value})\n')

# Load matrices from files
matrix1 = SparseMatrix()
matrix1.load_from_file(r"C:\Users\HP\Downloads\sample_input_for_students-20240530T200252Z-001\sample_input_for_students\easy_sample_01_2.txt")
print(f'Matrix 1 dimensions: {matrix1.numRows} rows, {matrix1.numCols} columns')

matrix2 = SparseMatrix()
matrix2.load_from_file(r"C:\Users\HP\Downloads\sample_input_for_students-20240530T200252Z-001\sample_input_for_students\easy_sample_01_3.txt")
print(f'Matrix 2 dimensions: {matrix2.numRows} rows, {matrix2.numCols} columns')

# Perform operations
try:
    result = matrix1.multiply(matrix2)
    print("Multiplication result:")
    result.print_matrix()
    result.save_to_file('multiply_result.txt')
except ValueError as e:
    print(e)
