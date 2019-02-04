class Analyzer:
    def calculate_maxmimum(self, x):
        max = x[0]
        for i in x[1:]:
            if i > max:
                max = i

        return max

    def calculate_sum(self, x):
        sum = 0
        for i in x:
            sum += i

        return sum

    def calculate_mean(self, x):
        sum = self.calculate_sum(x)
        n = self.get_len(x)

        return sum / n

    def calculate_variance(self, x):
        mean = self.calculate_mean(x)
        square = ((i - mean) ** 2 for i in x)
        sum_of_squares = self.calculate_sum(square)

        return sum_of_squares / self.get_len(x)

    def calculate_standard_deviation(self, x):
        return self.calculate_variance(x) ** (1 / 2)

    def get_len(self, x):
        n = 0
        for i in x:
            n += 1

        return n
