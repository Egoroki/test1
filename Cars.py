class Cars(object):
    produced_cars = []

    def __init__(self, color="Black",  wheels=5):
        self.color = color
        self.produced_cars.append(self)
        if color.lower() != 'red':
            self.wheels = wheels
        else:
            self.wheels = wheels - 1

    def diag(self):
        print(f"I have color of {self.color} and wheels {self.wheels}")

    def total_cars_created(self=None):
        print(f"Total cars created: {len(self.produced_cars)}")


class Crossover(Cars):
    def __init__(self, color="Red"):
        super().__init__(color)
        super().diag()


class Sedan(Cars):
    def __init__(self):
        super().__init__(color='Blue')  # Всегда синие
        super().diag()


ford = Crossover()
ford1 = Sedan()
ford1.total_cars_created()

