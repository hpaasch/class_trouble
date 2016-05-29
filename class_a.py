
class ClassnameA:

    def __init__(self):
        self.car = 0
        self.boat = 0
        self.house = 0

    def method_one(self):
        self.car = 100
        return self.car

    def method_two(self):
        self.boat = 200
        return self.boat

    def method_three(self):
        self.house = 300
        return self.house

# -----------------------------
# below is output testing only
# heptest = ClassnameA()
# heptest.method_one()
# print(heptest.car) >>> to print the variable, must first run the method.
# print(heptest.method_one())  # >>> calling the method will get you the value.
# print(heptest.method_two())
# print(heptest.method_three())


