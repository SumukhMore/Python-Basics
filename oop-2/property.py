class Student:
    def __init__(self, phy, chem, math):
        self._phy = phy          # Protected attribute
        self._chem = chem        # Protected attribute
        self._math = math        # Protected attribute

    @property
    def percentage(self):
        return str((self._phy + self._chem + self._math) / 3) + "%"
    
stu = Student(85, 90, 95)
print(stu.percentage)

stu._phy = 95  # Modifying protected attribute
print(stu.percentage)