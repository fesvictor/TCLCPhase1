class Party:
    def __init__(self, _name):
        self.name = _name
        self.negative = 0
        self.positive = 0

    def get_name(self):
        return self.name

    def get_scale(self):
        return [self.negative, self.positive]

    def incre_negative(self):
        self.negative += 1

    def incre_positive(self):
        self.positive += 1

    def __str__(self):
        return f"\nname={self.name}\nnegative={self.negative}\npositive={self.positive}\n"
