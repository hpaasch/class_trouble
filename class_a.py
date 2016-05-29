
class ClassnameA:

    def __init__(self):
        self.car = 0

    def method_one(self):
        self.car = 100
        return self.car


# -----------------------------
# below is output testing only

heptest = ClassnameA()
print(heptest.car)  # >>> prints 0 >>> original value, before method runs
print(heptest.method_one())  # >>> prints 100 >>> value returned by method


