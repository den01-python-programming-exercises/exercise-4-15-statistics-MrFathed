class Statistics:
    def __init__(self):
        self.count = 0
        self.sum = 0

    def add_number(self, number):
        self.count += 1
        self.sum += number

    def get_count(self):
        return self.count

    def sum(self):
        return self.sum

    def average(self):
        return self.sum / self.count