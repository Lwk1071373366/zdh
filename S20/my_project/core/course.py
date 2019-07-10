class Course:
    def __init__(self, name, price, period, teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher

    def __str__(self):
        return '%s,%s,%s,%s' % (self.name, self.price, self.period, self.teacher)

    def __repr__(self):
        return self.name