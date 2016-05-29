from class_a import ClassnameA


class ClassnameB:
    def __init__(self):
        self.classname_a = ClassnameA()
        self.new_car_variable = self.classname_a.car
        self.new_car_method_value = self.classname_a.method_one()

    def method_two(self):
        newest_price = self.new_car_method_value + 50
        return newest_price

    def method_four(self):
        biggest_price = ClassnameA.method_three(self.classname_a)
        return biggest_price


# ------------------------
# below is only for output testing

heptest_b = ClassnameB()
print(heptest_b.new_car_variable)  # >>> prints 0
print(heptest_b.new_car_method_value)  # >>> prints 100
print(heptest_b.method_two())  # >>> prints 150
print(heptest_b.method_four())  # >>> prints 10,000

