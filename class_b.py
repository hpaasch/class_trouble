from class_a import ClassnameA


class ClassnameB:
    def __init__(self):
        self.classname_a = ClassnameA()
        self.newcar = ClassnameA.method_one()
        self.newboat = ClassnameA.method_two()
        self.newhouse = ClassnameA.method_three()
        self.tools = []

    def method_four(self):
        self.tools = ['hammer', 'nails', 'saw']
        return self.tools

    def method_five(self):
        ClassnameA.method_one()
        newest_price = self.newcar() + 50
        return newest_price




# ------------------------
# below is only for output testing

heptest_b = ClassnameB()
print(heptest_b.method_five())
# print(heptest_b.newcar)
# print(heptest_b.method_four())

