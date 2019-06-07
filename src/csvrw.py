import csv

class CSVRW:
    def __init__(self, path, delimiter):
        self.path = path
        self.delimiter = delimiter

    def read(self):
        ls = []
        with open(self.path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=self.delimiter)
            for row in reader:
                ls.append(row)
        return ls

    def write(self, table):
        with open(self.path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=self.delimiter)
            for row in table:
                writer.writerow(row) # needs work