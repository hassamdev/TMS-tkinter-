#############
###########classes and objects


class person:
    z=5
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
    def __str__(self) -> str:
        return self.Name
    def myfunc(self):
        return f"salam, my name is {self.Name}"

class student(person):
    def __init__(self, name, age,year):
        super().__init__(name, age)
        self.grad_Year = year
    def get_year(self):
        return self.grad_Year
    
s1= student("hassam",12,2025)
print(s1.myfunc())


