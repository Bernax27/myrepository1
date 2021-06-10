import csv
import numpy as np
import matplotlib.pyplot as plt


class Csv_handler:

    def __init__(self, road, new_road):
        self.road = road
        self.results = []
        self.line = 0
        self.column = 0
        self.new_road = new_road

    def reader_csv_file(self):
        """Reads a CSV file and print it as a list of rows."""
        with open(self.road, newline='', encoding='utf-8') as file:
            inp = csv.reader(file, delimiter=';', quotechar=',', quoting=csv.QUOTE_NONE)
            for row in inp:
                self.line += 1
                self.column = 0
                for number in row:
                    self.column += 1
                    number = int(float(number))
                    self.results.append(number)

    def finder_max(self):
        maximum = np.amax(self.results)
        return maximum

    def finder_min(self):
        minimum = np.amin(self.results)
        return minimum

    def graph(self):
        x_list = list(range(0, len(self.results)))
        y1_list = list(self.results)
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.set_title('Демонстрация заполения матрицы')
        ax.set_ylabel('Числа матрицы')
        plt.plot(x_list, y1_list)
        plt.ylabel("", fontsize=14, fontweight="bold")
        plt.show()

    def transpose(self):
        matrix = np.asarray(self.results).reshape(-1, self.column)
        matrix = matrix.transpose()
        with open(self.new_road, "w", newline='') as f:
            for row in matrix:
                print(' '.join(map(repr, row)), file=f)
